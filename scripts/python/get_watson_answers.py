import json
import shutil
import os
from os.path import join, exists
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    
## Install the sdk
## pip install --upgrade "ibm-watson>=4.3.0"

## This script will create a file for each intent present in the bot and write the answers (only one variation)
## https://cloud.ibm.com/apidocs/assistant/assistant-v2
## https://cloud.ibm.com/apidocs/assistant/assistant-v1
##
## Note: this request have a limitation on watson, due to having "export=True" on get_intent method watson only permits 400 calls every 30 minuts
## "With export=false, this operation is limited to 6000 requests per 5 minutes. With export=true, the limit is 400 requests per 30 minutes. For more information, see Rate limiting."

## Necessary: have a folder called examples (it is not created automatically in this version) at the same level of the script for storing the result
## main folder
##      - examples
##      - get_watson_answers.py


## config
#### workspace_id from the skill where the answers are
#### version of the api
config = {
    "workspace_id": 'd385cab3-de06-4774-8fa3-c9ce2218a43f',
    "version":'2020-04-01'
}

## api key from the skill
#### IAMAuthenticator({api_key})
authenticator = IAMAuthenticator('5p8sXN8Bsy4ELDisT5QySwE4EGeLy2p42HrsU2te7sYH')
assistant = AssistantV1(
    version=config["version"],
    authenticator=authenticator
)

## Server url
## https://cloud.ibm.com/apidocs/assistant/assistant-v2#service-endpoint
assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')

## get list of intents
## https://cloud.ibm.com/apidocs/assistant/assistant-v1?code=python#list-intents
response=assistant.list_intents(
    workspace_id=config["workspace_id"],
    page_limit=1000
).get_result()

intents_to_add = ['pt_quarantine_general', 'pt_spread_phases', 'pt_spread_washing_clothes', 'pt_state_calamity', 
                'pt_state_emergency_end', 'pt_user_laugh',  'pt_covid_ibuprofen',
                'pt_prevention_informed', 'utter_pt_bot_hobbies', 'pt_portugal_elders',
                'pt_stayhomeinfo_supermarket', 'pt_user_no_data', 'pt_bot_personal_questions',
                'pt_bot_sing', 'pt_bot_sports', 'pt_bot_worst_experience', 'pt_cc_deepest_point', 
                'pt_cc_fun_fact', 'pt_cc_geography', 'pt_cc_highest_building', 'pt_covid_sex', 
                'pt_deconfinement_establishments', 'pt_bot_games', 'pt_economy_consequences',
                'pt_portugal_elders', 'pt_prevention_medical_attention'     ]
dir_name = './examples'
if not exists(dir_name):
    os.makedirs(dir_name)                

intent_list = response["intents"]

# get one example for each intent
# send a message
# grab the answer and stores in file
for intent in intent_list:
    if intent['intent'] in intents_to_add:
        print('--', intent["intent"],)
        response=assistant.get_intent(
            workspace_id=config["workspace_id"],
            intent=intent["intent"],
            export=True
        ).get_result()

        request_example = response["examples"][0]

        response = assistant.message(
            workspace_id=config["workspace_id"],
            input={
                'text': request_example["text"]
            }
        ).get_result()

        answers_output = {
            "answers":[]
        }

        for answer in response["output"]["generic"]:
            answers_output["answers"].append(json.loads(answer["text"], strict=False))


        with open(join(dir_name, '{}.json'.format(intent["intent"])), 'w', encoding='utf-8') as f:
            f.write(json.dumps(answers_output, ensure_ascii=False, indent=2))

        

print("...... END")  