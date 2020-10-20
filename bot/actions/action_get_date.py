from typing import Text, Any, Dict, List
from datetime import date

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher


class GetDateValue(Action):

    def name(self):
        return "action_get_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = date.today()
        return [SlotSet("bot_date", today.strftime("%d/%m/%Y")),
                FollowupAction("utter_pt_features_date")]
