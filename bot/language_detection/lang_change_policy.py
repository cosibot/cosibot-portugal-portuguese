import os
import json
import logging
import typing
from typing import Any, List, Text, Optional

import rasa.utils.io

from rasa.core.domain import Domain #, InvalidDomain
from rasa.core.policies import Policy
from rasa.core.actions.action import ACTION_LISTEN_NAME #don't know if needed

from rasa.core.trackers import DialogueStateTracker
from rasa.core.constants import FALLBACK_POLICY_PRIORITY
from rasa.core.events import UserUttered
from rasa.utils.common import raise_warning

logger = logging.getLogger(__name__)

class LangChangePolicy(Policy):

    def __init__(
        self,
        priority: int = FALLBACK_POLICY_PRIORITY,
        lang_detect_threshold: float = 0.7,
        fallback_action_name: Text = "action_ask_language",
    ) -> None:
        """ Create a Language Detection Fallback Policy:
    
        Args:
            lang_detect_threshold: lower threshold for which to assume 
                language detection prediction reliable above that value.
                If both latest predictions execed this threshold, then 
                incoherence among lastest predictions should trigger 
                fallback action
            fallback_action_name: name of the action to execute as a fallback
        """

        super().__init__(priority=priority)

        self.lang_detect_threshold = lang_detect_threshold
        self.fallback_action_name = fallback_action_name

        logger.debug(f"Adopted LCP threshold: {self.lang_detect_threshold}")
        logger.debug(f"LCP action to fall out: {self.fallback_action_name}")
    
    def train(
        self,
        training_trackers: List[DialogueStateTracker],
        domain: Domain,
        **kwargs: Any,
    ) -> None:
        """Does nothing. This policy is deterministic."""
        pass

    def predict_action_probabilities(self, tracker, domain):

        def get_value_and_confidence(skip=0):
            fetcher = tracker.get_last_event_for(UserUttered, skip=skip)
            if fetcher is not None:
                entities_list = fetcher.as_dict().get("parse_data").get("entities")
                for d in entities_list: # d stands for dictionary...
                    if d['entity'] == 'bot_language_code':
                        lang_value = d['value']
                        lang_conf = d['confidence']
                        value_and_conf = dict(value=lang_value,confidence=lang_conf)
                        return value_and_conf

        def lang_detect_above_threshold_Q(record):
            if record and record is not None: 
                return (record.get('confidence') > self.lang_detect_threshold) 
                    
        latest_lang_record = get_value_and_confidence()
        if get_value_and_confidence(skip=1):
            previous_lang_record = get_value_and_confidence(skip=1)
        elif tracker.get_slot("language_slot"):
            previous_lang_record = dict(value=tracker.get_slot("language_slot"), confidence=1.0)
        else:
            previous_lang_record = None
        
        logger.debug(f"language present record is: {latest_lang_record}")
        logger.debug(f"previous language record is: {previous_lang_record}")
        
        result = self._default_predictions(domain)

        if (
            tracker.latest_action_name == self.fallback_action_name
            and tracker.latest_action_name != ACTION_LISTEN_NAME
        ):
            logger.debug(
                "Predicted 'action_listen' after fallback action '{}'".format(
                    self.fallback_action_name
                )
            )
            result = self._default_predictions(domain)
            idx = domain.index_for_action(ACTION_LISTEN_NAME)
            result[idx] = 1.0

        elif (previous_lang_record is not None and
           all([lang_detect_above_threshold_Q(x) for x in [latest_lang_record, previous_lang_record]]) and
           previous_lang_record.get('value') != latest_lang_record.get('value')):
            
            idx = domain.index_for_action(self.fallback_action_name)
            if idx is None:
                raise_warning(
                    f"LangChangePolicy tried to predict unknown "
                    "action \"{self.fallback_action_name}\". Make sure to map this actions"
                    "in the domain and run it the custom action server.",
                )
            else:
                result[idx] = 1
        
        return result

    def persist(self, path: Text) -> None:
        """Only persists the priority."""

        config_file = os.path.join(path, "langchangepolicy.json")
        meta = {"priority": self.priority,
                "lang_detect_threshold": self.lang_detect_threshold,
                "fallback_action_name": self.fallback_action_name
                }
        rasa.utils.io.create_directory_for_file(config_file)
        rasa.utils.io.dump_obj_as_json_to_file(config_file, meta)

    @classmethod
    def load(cls, path: Text) -> "LangChangePolicy":
        """Returns the class with the configured priority."""

        meta = {}
        if os.path.exists(path):
            meta_path = os.path.join(path, "langchangepolicy.json")
            if os.path.isfile(meta_path):
                meta = json.loads(rasa.utils.io.read_file(meta_path))

        return cls(**meta)