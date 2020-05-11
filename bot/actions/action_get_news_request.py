from typing import Text

import logging

logger = logging.getLogger(__name__)

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, UserUtteranceReverted
from datetime import date
import time
import requests


news_config = {
    "search_URL": "https://www.googleapis.com/customsearch/v1?",
    "params": {
        "cx": "004792777853439682942:rtuf9l9ktg6",
        "key": "AIzaSyA8OTYeMDXJcOSLghUwuPBSEo27EL30Ckw",
        "lr": "lang_pt"
    }
}


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_get_news_request"

    def build_links_answer(self, data):
        links = []
        for link in data:
            info_append = {"title": link[0], "url": link[1]}
            links.append(info_append)

        return {"type": "links", "links": links}

    def google_search(self, search_term):

        try:
            params = news_config["params"]
            params["q"] = search_term

            response = requests.get(url=news_config["search_URL"], params=params,)
            return response.json()
        except:
            return []

    def run(self, dispatcher, tracker, domain):
        #search_term = tracker.latest_message.get('text')
        search_term = "covid-19 Coronavirus"

        res = self.google_search(search_term)
        links_info = []
        if (int(res["searchInformation"]["totalResults"])) > 0:

            for item in res['items']:
                links_info.append((item["title"], item["link"]))
                if len(links_info) == 3:
                    break
            message = self.build_links_answer(links_info)
            return_response = domain["responses"]["utter_news_request_hasdata"][0]["custom"]
            return_response["answers"].insert(2, message)
            dispatcher.utter_message(json_message=return_response)
            return[]
        else:
            dispatcher.utter_message(template="utter_news_request_emptyanswer")
            return [UserUtteranceReverted()]

        dispatcher.utter_message(template="utter_news_request_emptyanswer")
        return [UserUtteranceReverted()]
