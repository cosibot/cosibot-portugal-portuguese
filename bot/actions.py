# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Text
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted
from datetime import date
import time
from googleapiclient.discovery import build
from bot.secret import *

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

class ActionGoogleCustomSearch(Action):
    def name(self) -> Text:
        return "action_google_custom_search"

    def google_search(self, search_term):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id).execute()
        return res['items']

    def run(self, dispatcher, tracker, domain):
        search_term = next(tracker.get_latest_entity_values("pt_search_term"), None)
        self.google_search(search_term)
        return []
