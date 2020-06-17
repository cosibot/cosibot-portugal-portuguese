## action_check_Bot_Introduced

#from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction

class ActionCheckBotIntroduced(Action):
    def name(self):
        return "action_check_Bot_Introduced"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("bot_introduced") == False:
            return [SlotSet("bot_introduced", True), FollowupAction("utter_pt_welcome")]
        else:
            return [FollowupAction("utter_pt_greeting_hello")]