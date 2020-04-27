# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Text, Any, Dict, List

import logging 
logger = logging.getLogger(__name__)

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import UserUtteranceReverted
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

class AskLanguage(Action):

    def name(self):
        return "action_ask_language"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(text="Hello, which language would you like to use? English/Englisch or/oder German/Deutsch")
# FollowupAction(action_listen)

        return [UserUtteranceReverted()]
