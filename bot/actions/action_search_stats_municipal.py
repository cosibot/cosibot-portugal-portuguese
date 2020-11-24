from typing import Text, Any, Dict, List
import requests
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction, SlotSet
from rasa_sdk.executor import CollectingDispatcher


class DecsisAPI:

    def search(self, country_municipal: str, date_filter=None) -> dict:
        try:
            query_fields = "[{\"municipality\": \"field\"}, {\"confirmed_accum\": \"field\"}]"

            # today = date.today()
            query_filters = "[{\"municipality\":\"" + str(country_municipal) + "\"}]"

            request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_municipalities?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json&last-data=date_day"
            print(request_url)
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
                query_filters = "[{\"date_day\":\"" + date_search.strftime("%Y-%m-%d") + "\"},{\"municipality\":\"" + str(country_municipal) + "\"}]"

                request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_municipalities?query={\"fields\":" + str(query_fields) + ", \"filters\":" + str(query_filters) + "}&format=json"
                response = requests.get(url=request_url)
                json_response = (response.json())[0]

                # return json_response
                stats = json_response
                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
        except Exception:
            return {'code': response.status_code, 'has_data': False}


class ActionSearchStatsMunicipal(Action):

    def name(self):
        return "action_search_stats_municipal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet('pt_country_code', 'PT'),
                FollowupAction("action_search_stats")]
        '''
        country_municipal = next(tracker.get_latest_entity_values("pt_country_municipal"), None)
        print("country municipal is {}".format(country_municipal))

        # date = tracker.get_slot("date")
        decsis_api = DecsisAPI()
        stats = decsis_api.search(country_municipal)

        if stats['code'] == 200 and not stats['has_data']:
            print("1", stats['has_data'])
            return [
                SlotSet('country_region_search_successful', 'empty'),
                SlotSet('country_region', country_municipal),
                SlotSet('pt_country_code', 'PT'),
                FollowupAction("utter_country_region_nodata")]
        elif stats['code'] == 200 and stats['has_data']:
            print("2", stats['has_data'])
            return [
                SlotSet('country_region_search_successful', 'ok'),
                SlotSet('country_region', country_municipal), 
                SlotSet('country_region_confirmed_accum', int(stats.get('confirmed_accum', None))),
                FollowupAction("utter_country_municipal_hasdata")]
        else:
            return [
                SlotSet('country_region_search_successful', 'not-ok'),
                SlotSet('pt_country_code', 'PT'),
                FollowupAction("utter_country_region_nodata")]
        '''
