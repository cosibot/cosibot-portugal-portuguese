from typing import Text, Any, Dict, List

import logging 
logger = logging.getLogger(__name__)

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted

from rasa_sdk.executor import CollectingDispatcher
from datetime import date
import time


class GetDateValue(Action):

    def name(self):
        return "action_get_date"

    def run(self, dispatcher, tracker, domain):
        today = date.today()
        return [SlotSet("bot_date", today.strftime("%d/%m/%Y")),
                    FollowupAction("utter_pt_features_date")]