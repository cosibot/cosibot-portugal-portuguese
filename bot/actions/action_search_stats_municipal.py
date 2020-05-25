from typing import Text

import requests
from datetime import date, datetime, timedelta

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted

class DecsisAPI:

    def search(self, country_municipal, date_filter=None):
        try:
            query_fields = "[{\"municipality\": \"field\"}, {\"confirmed_accum\": \"field\"},{\"confirmed_accum_male\": \"field\"},{\"confirmed_accum_female\": \"field\"},{\"confirmed_new\": \"field\"},{\"waiting_lab_results\": \"field\"},{\"hospitalized\": \"field\"},{\"hospitalized_critical\": \"field\"},{\"recovered\": \"field\"},{\"deaths\": \"field\"},{\"suspected\": \"field\"}]"

            today = date.today()
            query_filters = "[{\"date_day\":\"" + today.strftime("%Y-%m-%d")+"\"},{\"municipality\":\""+ str(country_municipal) + "\"}]"

            request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_municipalities?query={\"fields\":"+ str(query_fields) +", \"filters\":"+ str(query_filters) +"}&format=json"
            response = requests.get(url = request_url)

            json_response = (response.json())

            if (len(json_response) > 0):
                #return json_response[0]
                stats = json_response[0]
                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
            else:
                date_search = datetime.today() - timedelta(days=1)
                query_filters = "[{\"date_day\":\"" + date_search.strftime("%Y-%m-%d")+"\"},{\"municipality\":\""+ str(country_municipal) + "\"}]"

                request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_municipalities?query={\"fields\":"+ str(query_fields) +", \"filters\":"+ str(query_filters) +"}&format=json"
                response = requests.get(url = request_url)
                json_response = (response.json())[0]
    
                #return json_response
                stats = json_response
                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
        except:
            return {'code': response.status_code, 'has_data': False}


class ActionSearchStatsMunicipal(Action):

    def name(self):
        return "action_search_stats_municipal"

    def run(self, dispatcher, tracker, domain):
        
        country_municipal = next(tracker.get_latest_entity_values("pt_country_municipal"), None)
        print("country municipal is {}".format(country_municipal))

        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_municipal)

        if stats['code'] == 200 and not stats['has_data']:
            return [SlotSet('country_municipal_search_successful', 'empty'),SlotSet('country_municipal', country_municipal),SlotSet('pt_country_code', 'PT'),]
            #self.get_country_data(country_municipal,"empty",dispatcher, tracker, domain)
        elif stats['code'] == 200 and stats['has_data']:
            return [SlotSet('country_municipal_search_successful', 'ok'),SlotSet('country_municipal', country_municipal), SlotSet('country_municipal_confirmed_accum', int(stats.get('confirmed_accum', None))),]
        else:
            return [SlotSet('country_municipal_search_successful', 'not-ok'),SlotSet('pt_country_code', 'PT'),]
            #self.get_country_data(country_municipal, "not-ok",dispatcher, tracker, domain)