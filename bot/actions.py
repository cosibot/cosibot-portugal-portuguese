# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Text, Any, Dict, List

import logging 
logger = logging.getLogger(__name__)

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted

from rasa_sdk.executor import CollectingDispatcher
from datetime import date
import time

import requests

class GetTimeValue(Action):

    def name(self):
        return "action_get_time"

    def run(self, dispatcher, tracker, domain):

        t = time.localtime()
        return [SlotSet("bot_time", time.strftime("%H:%M:%S", t)),
                    FollowupAction("utter_pt_features_time")]

class GetDateValue(Action):

    def name(self):
        return "action_get_date"

    def run(self, dispatcher, tracker, domain):
        today = date.today()
        return [SlotSet("bot_date", today.strftime("%d/%m/%Y")),
                    FollowupAction("utter_pt_features_date")]

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        return [UserUtteranceReverted(), FollowupAction("utter_")]

class ChangePreferredLanguage(Action):

    def name(self):
        return "action_change_preferred_language"

    def run(self, dispatcher, tracker, domain):

        preferred_lang = next(tracker.get_latest_entity_values("preferred_lang"), None)

        lang_code = preferred_lang.split('_')[0]
        print("lang_code: {}".format(lang_code))
        """ 
            if predicted lang = eng 
                return [FollowupAction("utter_pt_ask_change_bot_language")]
            else 
                return [FollowupAction("utter_pt_lang_not_available")]


        utter_pt_ask_change_bot_language
        "Não falo inglês, mas posso "

        

        """

        return [SlotSet('preferred_lang', lang_code), FollowupAction("utter_pt_command_change_bot")]


