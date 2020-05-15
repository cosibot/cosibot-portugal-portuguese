from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted, UserUttered
import requests
from datetime import date

class DecsisAPI:

    def search(self, country_code, date_filter=None):

        """calls DECSIS API. takes care of codes"""

        
        if date_filter is None: 
            date_filter = '2020-05-14' #date.today().strftime("%Y-%m-%d")
        else:
            date_filter = str(date_filter)
        
        query_fields = "[{\"country\": \"field\"}, {\"total_cases\": \"field\"},{\"new_cases\": \"field\"},{\"total_recovered\": \"field\"},{\"active_cases\": \"field\"},{\"critical\": \"field\"},{\"total_tests\": \"field\"},{\"region\": \"field\"},{\"new_deaths\": \"field\"},{\"total_deaths\": \"field\"},{\"total_cases_1m_pop\": \"field\"},{\"deaths_1m_pop\": \"field\"},{\"tests_1m_pop\": \"field\"},{\"continent\": \"field\"}]"
        query_filters = "[{\"date_day\":\"" + date_filter +"\"},{\"country_code\":\""+ str(country_code) + "\"}]"
        request_url = "https://api.data.decsis.cloud/api/v1/dataset/world_worldometers_coronavirus_countries?query={\"fields\":"+ str(query_fields) +", \"filters\":"+ str(query_filters) +"}&format=json&limit=5"

        response = requests.get(request_url)

        if response: 
            stats = response.json()
            if not stats: 
                return {'code' : response.status_code, 'has_data': False}
            elif stats:        
                stats = stats[0]
                print(stats)
                
                if str(stats["new_cases"]) == 'nan' and str(stats["new_deaths"]) == 'nan' or \
                stats["new_cases"] == None and stats["new_deaths"] == None:
                    stats["updated_today"] = False
                else:
                    stats["updated_today"] = True
                
                for key in stats:
                    if stats[key] == None:
                        stats[key] = 0

                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
        
        else: 
            return {'code': response.status_code, 'has_data': False}

class ActionSaveIntent(Action):

    def name(self) -> Text:
        return "action_save_intent"

    def run(self, dispatcher, tracker, domain):
        
        user_intent = tracker.latest_message['intent'].get('name')
        print("user_intent {}".format(user_intent))

        return [SlotSet('user_intent', user_intent)]


class StatsForm(FormAction):

    def name(self) -> Text:

        return "stats_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["pt_country_code"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
        
            or a list of them, where a first match will be picked"""
        print("slot_mappings -> from entity {}".format(self.from_entity(entity="pt_country_code")))
        # print("from text {}".format(self.from_text(intent="covid_info_cases")))
        # print("from trigger intent {}".format(self.from_trigger_intent(intent=["covid_info_cases", "covid_info_deaths", "country"])))
        return {
            "pt_country_code": [
                self.from_entity(entity="pt_country_code", intent=None)
                
                # ["pt_country", "pt_covid_situation", "pt_covid_situation_deaths", "pt_covid_situation_infected", 
                #                                                     "pt_covid_situation_last_update", "pt_covid_situation_infected_critical", "pt_covid_situation_recovered", 
                #                                                     "pt_covid_situation_tested",]),
                # self.from_trigger_intent(intent=["covid_info_cases", "covid_info_deaths", "country"])
                # self.from_intent(intent="covid_info_cases"),
                # self.from_intent(intent="covid_info_deaths"),
                # self.from_intent(intent="country"),
            ],
        }

    def validate_pt_country_code(self, value, dispatcher, tracker, domain) -> Dict[Text, Any]:
        """Check to see if a country entity was actually picked up."""

        if any(tracker.get_latest_entity_values("pt_country_code")):
            print("validate_ok: {}".format(value))
            # entity was picked up, validate slot
            return {"pt_country_code": value}
        else:
            print("validate_not_ok")
            # no entity was picked up, we want to ask again
            dispatcher.utter_message(template="utter_ask_pt_country_code")
            return {"pt_country_code": None}
    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        country_code = tracker.get_slot('pt_country_code')
        print("country code is {}".format(country_code))

        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_code)

        user_intent = tracker.get_slot('user_intent')
        # tracker_current_state = tracker.current_state()
        # dispatcher.utter_message(text=str(tracker_current_state))

        if country_code is not None: 

            if stats['code'] == 200 and not stats['has_data'] and len(country_code) == 2:
                print('inexistent-country')
                """In this case we're assuming the user did not miss the country's name but instead it really does not exist at the source."""
                return [SlotSet('search_successful', 'inexistent-country'), SlotSet('pt_country_code', None), FollowupAction("utter_pt_covid_no_country_current_statistics")]
            elif stats['code'] == 200 and not stats['has_data'] and len(country_code) != 2:
                print('wrong-country')
                """In this case we're assuming the user missed the country's name so we ask them if they want to rephrase it"""
                return [SlotSet('search_successful', 'wrong-country'), SlotSet('pt_country_code', None), FollowupAction("utter_ask_pt_country_code")]
            elif stats['code'] != 200 and not stats['has_data']:
                print('not-ok')
                """ """
                return [SlotSet('search_successful', 'not-ok'), SlotSet('pt_country_code', None), FollowupAction("utter_pt_covid_current_statistics")]
            elif stats['code'] == 200 and stats['has_data']:
                print('ok')
                entity = next((e for e in tracker.latest_message["entities"] if
                                    e['entity'] == 'pt_country_code'), None)
                print(entity)

                input_country = tracker.latest_message['text'][entity['start']:entity['end']]
                
                return [SlotSet('search_successful', 'ok'), SlotSet('input_country', input_country), SlotSet('active_cases', int(stats.get('active_cases', None))), 
                    SlotSet('new_cases', int(stats.get('new_cases', None))), SlotSet('total_cases', int(stats.get('total_cases', None))),
                    SlotSet('total_recovered', int(stats.get('total_recovered', None))), SlotSet('total_deaths', int(stats.get('total_deaths', None))),
                    SlotSet('total_tests', int(stats.get('total_tests', None))), SlotSet('new_deaths', int(stats.get('new_deaths', None))),
                    SlotSet('total_infected_critical', int(stats.get('critical', None))), SlotSet('pt_country_code', None), FollowupAction(f"utter_{user_intent}")] 
        
        elif country_code is None: 
            """In this case, no entity was recognized. Example: when user asks for 'world information'"""
            print('wrong-country')
            return [SlotSet('search_successful', 'wrong-country'), SlotSet('pt_country_code', None), FollowupAction("utter_ask_pt_country_code")]