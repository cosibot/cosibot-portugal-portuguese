import requests
from datetime import date, datetime, timedelta

class DecsisAPI:

    def search_country(self, country_code, date_filter=None):

        """calls DECSIS API. takes care of codes"""

        
        if date_filter is None: 
            date_filter = date.today().strftime("%Y-%m-%d")
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

    def search_municipality(self, country_municipal, date_filter=None):
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

    def search_region(self, country_region, date_filter=None):
        try:
            query_fields = "[{\"region\": \"field\"}, {\"confirmed_accum\": \"field\"},{\"confirmed_accum_male\": \"field\"},{\"confirmed_accum_female\": \"field\"},{\"confirmed_new\": \"field\"},{\"waiting_lab_results\": \"field\"},{\"hospitalized\": \"field\"},{\"hospitalized_critical\": \"field\"},{\"recovered\": \"field\"},{\"deaths\": \"field\"},{\"suspected\": \"field\"}]"

            today = date.today()
            query_filters = "[{\"date_day\":\"" + today.strftime("%Y-%m-%d")+"\"},{\"region\":\""+ str(country_region) + "\"}]"

            request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_regions?query={\"fields\":"+ str(query_fields) +", \"filters\":"+ str(query_filters) +"}&format=json"
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
                query_filters = "[{\"date_day\":\"" + date_search.strftime("%Y-%m-%d")+"\"},{\"region\":\""+ str(country_region) + "\"}]"

                request_url = "https://api.data.decsis.cloud/api/v1/dataset/pt_dgs_covid19_regions?query={\"fields\":"+ str(query_fields) +", \"filters\":"+ str(query_filters) +"}&format=json"
                response = requests.get(url = request_url)
                json_response = (response.json())[0]
    
                #return json_response
                stats = json_response
                stats['code'] = response.status_code
                stats['has_data'] = True

                return stats
        except:
            return {'code': response.status_code, 'has_data': False}
            #return stats