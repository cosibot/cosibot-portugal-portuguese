from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


class ActionCheckBotIntroduced(Action):
    def name(self) -> Text:
        return "action_check_Bot_Introduced"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if not tracker.get_slot("bot_introduced"):
            return [SlotSet("bot_introduced", True), FollowupAction("utter_pt_welcome")]
        else:
            return [FollowupAction("utter_pt_greeting_hello")]
