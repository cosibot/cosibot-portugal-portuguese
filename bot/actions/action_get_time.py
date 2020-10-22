
from typing import Text, Any, Dict, List
import time

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher


class GetTimeValue(Action):

    def name(self):
        return "action_get_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        t = time.localtime()
        return [SlotSet("bot_time", time.strftime("%H:%M:%S", t)),
                FollowupAction("utter_pt_features_time")]
