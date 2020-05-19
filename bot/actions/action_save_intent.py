from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted, UserUttered


class ActionSaveIntent(Action):

    def name(self) -> Text:
        return "action_save_intent"

    def run(self, dispatcher, tracker, domain):
        
        user_intent = tracker.latest_message['intent'].get('name')
        print("user_intent {}".format(user_intent))

        return [SlotSet('user_intent', user_intent)]