import requests

fallback_config = {
    "search_URL": "https://www.googleapis.com/customsearch/v1?",
    "params": {
        "cx": "004792777853439682942:bqj2kbtzewg",
        "key": "AIzaSyA8OTYeMDXJcOSLghUwuPBSEo27EL30Ckw",
        "lr": "lang_pt"
    }
}

params = fallback_config["params"]
params["q"] = "lalala"

response = requests.get(url=fallback_config["search_URL"], params=params,)
response_json = response.json()
print(response.json())
