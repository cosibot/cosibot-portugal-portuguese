# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/



from typing import Text
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted
from datetime import date
import time
from googleapiclient.discovery import build
from bot.secret import *

class GetTimeValue(Action):

    def name(self):
        return "action_get_time"

    def run(self, dispatcher, tracker, domain):

        t = time.localtime()
        return [SlotSet("bot_time", time.strftime("%H:%M:%S", t)),
                    FollowupAction("utter_pt_features_time")]

class GetDateValue(Action):

    def name(self):
        return "action_get_date"

    def run(self, dispatcher, tracker, domain):
        today = date.today()
        return [SlotSet("bot_date", today.strftime("%d/%m/%Y")),
                    FollowupAction("utter_pt_features_date")]

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        return [UserUtteranceReverted(), FollowupAction("utter_")]

class ActionGoogleCustomSearch(Action):
    def name(self) -> Text:
        return "action_google_custom_search"

    def google_search(self, search_term):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id).execute()
        return res['items']

    def run(self, dispatcher, tracker, domain):
        search_term = next(tracker.get_latest_entity_values("pt_search_term"), None)
        self.google_search(search_term)
        return []


class DecsisAPI:

    def search(self, country_code, date_filter=None):

        try:
            if date_filter is None:
                date_filter = date.today().strftime("%Y-%m-%d")
            else:
                date_filter = str(date_filter)

            query_fields = "[{\"country\": \"field\"}, {\"total_cases\": \"field\"},{\"new_cases\": \"field\"},{\"total_recovered\": \"field\"},{\"active_cases\": \"field\"},{\"critical\": \"field\"},{\"total_tests\": \"field\"},{\"region\": \"field\"},{\"new_deaths\": \"field\"},{\"total_deaths\": \"field\"},{\"total_cases_1m_pop\": \"field\"},{\"deaths_1m_pop\": \"field\"},{\"tests_1m_pop\": \"field\"},{\"continent\": \"field\"}]"
            query_filters = "[{\"date_day\":\"" + date_filter + "\"},{\"country_code\":\"" + str(country_code) + "\"}]"
            request_url = "https://api.data.decsis.cloud/api/v1/dataset/world_worldometers_coronavirus_countries?query={\"fields\":" + str(
                query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&limit=5"

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
        print("country code é {}".format(country_code))
        print(tracker.latest_message['text'])

        dispatcher.utter_message("A procurar estatísticas sobre {}".format(country_code))
        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_code)
        # dispatcher.utter_message("Estatísticas COVID-19 em {} (até {}): \n - Novos casos: {}".format(stats['country'], date.today().strftime("%d-%m-%Y"), stats['new_cases']))

        return [SlotSet('country', stats.get('country', None)),
                SlotSet('active_cases', stats.get('active_cases', None)),
                SlotSet('new_cases', stats.get('new_cases', None)),
                SlotSet('total_cases', stats.get('total_cases', None)),
                SlotSet('total_recovered', stats.get('total_recovered', None)),
                SlotSet('total_deaths', stats.get('total_deaths', None)),
                SlotSet('total_tests', stats.get('total_tests', None)),
                SlotSet('new_deaths', stats.get('new_deaths', None)),
                SlotSet('total_infected_critical', stats.get('critical', None)), ]
