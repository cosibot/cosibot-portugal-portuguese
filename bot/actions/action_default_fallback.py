from typing import Any, Text, Dict, List
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, UserUtteranceReverted


fallback_config = {
    "search_URL": "https://www.googleapis.com/customsearch/v1?",
    "params": {
        "cx": "004792777853439682942:bqj2kbtzewg",
        "key": "AIzaSyA8OTYeMDXJcOSLghUwuPBSEo27EL30Ckw",
        "lr": "lang_pt"
    }
}


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def build_links_answer(self, data):
        links = []
        for link in data:
            info_append = {"title": link[0], "url": link[1]}
            links.append(info_append)

        return {"type": "links", "links": links}

    def google_search(self, search_term):

        try:
            params = fallback_config["params"]
            params["q"] = search_term

            response = requests.get(url=fallback_config["search_URL"], params=params,)
            return response.json()
        except Exception:
            return []

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nr_tries = tracker.get_slot("total_nr_tries")
        nr_tries = nr_tries + 1.0

        if nr_tries == 1.0:
            dispatcher.utter_message(template="utter_fallback_first")
            return [SlotSet("total_nr_tries", nr_tries)]
        else:
            search_term = tracker.latest_message.get('text')

            res = self.google_search(search_term)
            links_info = []
            if (int(res["searchInformation"]["totalResults"])) > 0:

                for item in res['items']:
                    links_info.append((item["title"], item["link"]))
                    if len(links_info) == 3:
                        break
                message = self.build_links_answer(links_info)
                return_response = domain["responses"]["utter_fallback_request_hasdata"][0]["custom"]
                return_response["answers"].append(message)
                dispatcher.utter_message(json_message=return_response)
            else:
                dispatcher.utter_message(template="utter_fallback_request_emptyanswer")
                return [UserUtteranceReverted()]

            return [SlotSet("total_nr_tries", 0.0)]
