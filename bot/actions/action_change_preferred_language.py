from typing import Text, Any, Dict, List

import logging 
logger = logging.getLogger(__name__)

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted

from rasa_sdk.executor import CollectingDispatcher

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


