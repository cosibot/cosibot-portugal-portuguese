from typing import Text, Any, Dict, List
import requests
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction, SlotSet
from rasa_sdk.executor import CollectingDispatcher


class DecsisAPI:

    def search(self, country_region, date_filter=None):
        try:
            query_fields = "[{\"region\": \"field\"}, {\"confirmed_accum\": \"field\"},{\"confirmed_new\": \"field\"},{\"waiting_lab_results\": \"field\"},{\"hospitalized\": \"field\"},{\"hospitalized_critical\": \"field\"},{\"recovered\": \"field\"},{\"deaths\": \"field\"}]"

            # today = date.today()
            query_filters = "[{\"region\":\"" + str(country_region) + "\"}]"

            request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_regions?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&last-data=date_day"
            response = requests.get(url=request_url)

            json_response = (response.json())

            if (len(json_response) > 0):
                # return json_response[0]
                stats = json_response[0]
                stats['code'] = response.status_code
                stats['has_data'] = True
                return stats
            else:
                date_search = datetime.today() - timedelta(days=1)
                query_filters = "[{\"date_day\":\"" + date_search.strftime("%Y-%m-%d")+"\"},{\"region\":\"" + str(country_region) + "\"}]"

                request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_regions?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json"
                response = requests.get(url=request_url)
                json_response = (response.json())[0]
                # return json_response
                stats = json_response
                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
        except Exception:
            return {'code': response.status_code, 'has_data': False}
            # return stats


class ActionSearchStatsRegion(Action):

    def name(self):
        return "action_search_stats_region"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country_region = next(tracker.get_latest_entity_values("pt_country_region"), None)
        print("country region is {}".format(country_region))
        
        if country_region is None:
            if tracker.get_latest_entity_values("pt_country_code"):
                return [FollowupAction("action_search_stats")]
            else:
                pass
        
        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_region)

        if stats['code'] == 200 and not stats['has_data']:
            return [
                SlotSet('country_region_search_successful', 'empty'),
                SlotSet('country_region', country_region),
                SlotSet('pt_country_code', 'PT'),
                FollowupAction("utter_country_region_nodata")]
        elif stats['code'] == 200 and stats['has_data']:
            return [SlotSet('country_region_search_successful', 'ok'),
                SlotSet('country_region', country_region),
                SlotSet('country_region_confirmed_accum',int(stats.get('confirmed_accum', "N/A"))),
                SlotSet('country_region_confirmed_new',int(stats.get('confirmed_new', "N/A"))),
                SlotSet('country_region_hospitalized_critical',int(stats.get('hospitalized_critical', "N/A"))),
                FollowupAction("utter_country_region_hasdata")]
        else:
            return [
                SlotSet('country_regionsearch_successful', 'not-ok'),
                SlotSet('pt_country_code', 'PT'),
                FollowupAction("utter_country_region_nodata")]
