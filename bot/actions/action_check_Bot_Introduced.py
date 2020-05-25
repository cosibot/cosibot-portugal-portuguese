## action_check_Bot_Introduced

#from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionCheckBotIntroduced(Action):
    def name(self):
        return "action_check_Bot_Introduced"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("bot_introduced", True)]