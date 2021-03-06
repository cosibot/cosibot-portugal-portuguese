from typing import Text, Any, Dict, List
import requests
from datetime import date

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher


class DecsisAPI:

    def search(self, country_code, date_filter=None):

        """calls DECSIS API. takes care of codes"""

        if date_filter is None:
            date_filter = date.today().strftime("%Y-%m-%d")
        else:
            date_filter = str(date_filter)

        query_fields = "[{\"country\": \"field\"}, {\"total_cases\": \"field\"},{\"new_cases\": \"field\"},{\"total_recovered\": \"field\"},{\"active_cases\": \"field\"},{\"critical\": \"field\"},{\"total_tests\": \"field\"},{\"region\": \"field\"},{\"new_deaths\": \"field\"},{\"total_deaths\": \"field\"},{\"total_cases_1m_pop\": \"field\"},{\"deaths_1m_pop\": \"field\"},{\"tests_1m_pop\": \"field\"},{\"continent\": \"field\"}]"
        query_filters = "[{\"country_code\":\"" + str(country_code) + "\"}]"
        request_url = "https://api.data.decsis.cloud/api/v1/dataset/world_worldometers_coronavirus_countries?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&limit=5&last-data=date_day"

        response = requests.get(request_url)

        if response:
            stats = response.json()
            if not stats:
                return {'code': response.status_code, 'has_data': False}
            elif stats:
                stats = stats[0]
                if str(stats["new_cases"]) == 'nan' and str(stats["new_deaths"]) == 'nan' or stats["new_cases"] is None and stats["new_deaths"] is None:
                    stats["updated_today"] = False
                else:
                    stats["updated_today"] = True
                for key in stats:
                    if stats[key] is None:
                        stats[key] = 0
                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
        else:
            return {'code': response.status_code, 'has_data': False}


class ActionSearchStats(Action):

    def name(self):
        return "action_search_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        country_code = next(tracker.get_latest_entity_values("pt_country_code"), None)
        if country_code is None and tracker.get_slot("pt_country_code") == "PT":
            country_code = "PT"
        # country_code = tracker.get_slot("pt_country_code")
        print("country code is {}".format(country_code))

        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_code)

        # tracker_current_state = tracker.current_state()
        # dispatcher.utter_message(text=str(tracker_current_state))

        if country_code is not None:

            if stats['code'] == 200 and not stats['has_data'] and len(country_code) == 2:
                print('inexistent-country')
                """In this case we're assuming the user did not miss the country's name but instead it really does not exist at the source."""
                return [SlotSet('search_successful', 'inexistent-country'),
                        FollowupAction("utter_pt_covid_no_country_current_statistics"), ]
            elif stats['code'] == 200 and not stats['has_data'] and len(country_code) != 2:
                print('wrong-country')
                """In this case we're assuming the user missed the country's name so we ask them if they want to rephrase it"""
                return [SlotSet('search_successful', 'wrong-country'),
                        FollowupAction("utter_pt_want_to_add_country"), ]
            elif stats['code'] != 200 and not stats['has_data']:
                print('not-ok')
                """ """
                return [SlotSet('search_successful', 'not-ok'),
                        FollowupAction("utter_pt_covid_current_statistics"), ]
            elif stats['code'] == 200 and stats['has_data']:
                print('ok')
                '''
                try:
                    entity = next((e for e in tracker.latest_message["entities"] if
                                   e['entity'] == 'pt_country_code'), None)
                    print(entity)
                    input_country = tracker.latest_message['text'][entity['start']:entity['end']].capitalize()
                except:
                    if country_code == "PT" and tracker.get_slot("pt_country_code") == "PT":
                        input_country = "Portugal"
                '''
                entity = next((e for e in tracker.latest_message["entities"] if
                                   e['entity'] == 'pt_country_code'), None)
                print(entity)
                if entity is None:
                    pass
                else:
                    input_country = tracker.latest_message['text'][entity['start']:entity['end']].capitalize()
                
                if country_code == "PT" and tracker.get_slot("pt_country_code") == "PT":
                    input_country = "Portugal"
                
                intent_identified = tracker.latest_message["intent"].get("name")
                utter_response = None
                if intent_identified == "pt_covid_situation_deaths":
                    utter_response = "utter_pt_covid_situation_deaths"
                elif intent_identified == "pt_covid_situation_infected":
                    utter_response = "utter_pt_covid_situation_infected"
                elif intent_identified == "pt_covid_situation_infected_critical":
                    utter_response = "utter_pt_covid_situation_infected_critical"
                elif intent_identified == "pt_covid_situation_last_update":
                    utter_response = "utter_pt_covid_situation_last_update"
                elif intent_identified == "pt_covid_situation_recovered":
                    utter_response = "utter_pt_covid_situation_recovered"
                elif intent_identified == "pt_covid_situation_tested":
                    utter_response = "utter_pt_covid_situation_tested"
                elif intent_identified == "pt_covid_situation":
                    utter_response = "utter_pt_covid_situation"


                if utter_response is None:
                    return [
                        SlotSet('search_successful', 'ok'), 
                        SlotSet('country', input_country), 
                        SlotSet('active_cases', int(stats.get('active_cases', None))), 
                        SlotSet('new_cases', int(stats.get('new_cases', None))), 
                        SlotSet('total_cases', int(stats.get('total_cases', None))),
                        SlotSet('total_recovered', int(stats.get('total_recovered', None))), 
                        SlotSet('total_deaths', int(stats.get('total_deaths', None))),
                        SlotSet('total_tests', int(stats.get('total_tests', None))), 
                        SlotSet('new_deaths', int(stats.get('new_deaths', None))),
                        SlotSet('total_infected_critical', int(stats.get('critical', None))),FollowupAction('utter_pt_covid_situation')]
                else:
                    return [
                        SlotSet('search_successful', 'ok'), 
                        SlotSet('country', input_country), 
                        SlotSet('active_cases', int(stats.get('active_cases', None))), 
                        SlotSet('new_cases', int(stats.get('new_cases', None))), 
                        SlotSet('total_cases', int(stats.get('total_cases', None))),
                        SlotSet('total_recovered', int(stats.get('total_recovered', None))), 
                        SlotSet('total_deaths', int(stats.get('total_deaths', None))),
                        SlotSet('total_tests', int(stats.get('total_tests', None))), 
                        SlotSet('new_deaths', int(stats.get('new_deaths', None))),
                        SlotSet('total_infected_critical', int(stats.get('critical', None))),FollowupAction(utter_response)]
        
        elif country_code is None: 
            """In this case, no entity was recognized. Example: when user asks for 'world information'"""
            print('wrong-country')
            return [SlotSet('search_successful', 'wrong-country'),
                    FollowupAction("utter_pt_want_to_add_country"), ]
