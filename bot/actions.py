# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


import requests
from datetime import date

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class DecsisAPI:

    def search(self, country_code, date_filter=None):

        try:
            if date_filter is None: 
                date_filter = date.today().strftime("%Y-%m-%d")
            else:
                date_filter = str(date_filter)
            
            query_fields = "[{\"country\": \"field\"}, {\"total_cases\": \"field\"},{\"new_cases\": \"field\"},{\"total_recovered\": \"field\"},{\"active_cases\": \"field\"},{\"critical\": \"field\"},{\"total_tests\": \"field\"},{\"region\": \"field\"},{\"new_deaths\": \"field\"},{\"total_deaths\": \"field\"},{\"total_cases_1m_pop\": \"field\"},{\"deaths_1m_pop\": \"field\"},{\"tests_1m_pop\": \"field\"},{\"continent\": \"field\"}]"
            query_filters = "[{\"date_day\":\"" + date_filter +"\"},{\"country_code\":\""+ str(country_code) + "\"}]"
            request_url = "https://api.data.decsis.cloud/api/v1/dataset/world_worldometers_coronavirus_countries?query={\"fields\":"+ str(query_fields) +", \"filters\":"+ str(query_filters) +"}&format=json&limit=5"

            stats = requests.get(request_url).json()[0]

            if str(stats["new_cases"]) == 'nan' and str(stats["new_deaths"]) == 'nan' or \
            stats["new_cases"] == None and stats["new_deaths"] == None:
                stats["updated_today"] = False
            else:
                stats["updated_today"] = True
            
            for key in stats:
                if stats[key] == None:
                    stats[key] = 0
            
            return stats 	
        except:
            return {}

class ActionSearchStats(Action):

    def name(self):
        return "action_search_stats"

    def run(self, dispatcher, tracker, domain):
        country_code = next(tracker.get_latest_entity_values("pt_country_code"), None)
        print(country_code)
        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_code)
        # dispatcher.utter_message("Estatísticas COVID-19 em {} (até {}): \n - Novos casos: {}".format(stats['country'], date.today().strftime("%d-%m-%Y"), stats['new_cases']))

        return [SlotSet('country', stats['country']), SlotSet('active_cases', stats['active_cases']), 
                SlotSet('new_cases', stats['new_cases']), SlotSet('total_cases', stats['total_cases']),
                SlotSet('total_recovered', stats['total_recovered']), SlotSet('total_deaths', stats['total_deaths']),
                SlotSet('total_tests', stats['total_tests']), SlotSet('new_deaths', stats['new_deaths']), ]
