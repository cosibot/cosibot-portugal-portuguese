import os
import json
import typing
from typing import Any, List, Text, Optional

import rasa.utils.io

from rasa.core.domain import Domain, InvalidDomain
from rasa.core.policies import Policy
# from rasa.core.actions.action import ACTION_LISTEN_NAME #don't know if needed

from rasa.core.trackers import DialogueStateTracker
from rasa.core.constants import FALLBACK_POLICY_PRIORITY
from rasa.core.events import UserUttered
from rasa.utils.common import raise_warning

class LangChangePolicy(Policy):

    def __init__(
        self,
        priority: int = FALLBACK_POLICY_PRIORITY
    ):

        super().__init__(priority=priority)
    
    def train(
        self,
        training_trackers: List[DialogueStateTracker],
        domain: Domain,
        **kwargs: Any,
    ) -> None:
        """Does nothing. This policy is deterministic."""

    def predict_action_probabilities(self, tracker, domain):
        
        language_code_rec = tracker.get_latest_entity_values("language_code")
        deep_tracker = tracker.get_last_event_for(UserUttered, skip=1)
        previous_lang = None
        if deep_tracker is not None:
            print(deep_tracker.as_dict().get("parse_data").get("entities"))
            entities_list = deep_tracker.as_dict().get("parse_data").get("entities")
            for dict in entities_list: #could be improved by a lazy search
                if dict['entity'] == 'language_code':
                    previous_lang = dict['value']
        print("Lang_code_of present record is: ", *list(language_code_rec))
        print("Previous record Lang_code is: ", previous_lang)
        lang = next(language_code_rec,None)
        
        result = self._default_predictions(domain)

        if previous_lang is not None and lang != previous_lang:
            idx = domain.index_for_action("action_ask_language")
            if idx is None:
                    raise_warning(
                        "LangChangePolicy tried to predict unknown "
                        "action 'action_ask_language'. Make sure to map this actions"
                        "in the domain and run it the custom action server.",
                    )
            else:
                result[idx] = 1
        
        return result

    def persist(self, path: Text) -> None:
        """Only persists the priority."""

        config_file = os.path.join(path, "mapping_policy.json")
        meta = {"priority": self.priority}#, "last_lang": self.last_lang}
        rasa.utils.io.create_directory_for_file(config_file)
        rasa.utils.io.dump_obj_as_json_to_file(config_file, meta)

    @classmethod
    def load(cls, path: Text) -> "MappingPolicy":
        """Returns the class with the configured priority."""

        meta = {}
        if os.path.exists(path):
            meta_path = os.path.join(path, "mapping_policy.json")
            if os.path.isfile(meta_path):
                meta = json.loads(rasa.utils.io.read_file(meta_path))

        return cls(**meta)