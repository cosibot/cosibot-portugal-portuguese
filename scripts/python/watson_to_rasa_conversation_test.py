import json
import shutil
import os
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    
## Install the sdk
## pip install --upgrade "ibm-watson>=4.3.0"

## This script will create a conversation_test.md file to test the RASA bot
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

intent_list = response["intents"]

output_path = '../../bot/tests/conversation_tests.md'
# output_path = './convesation_test.md'

with open(output_path, 'w', encoding='utf-8') as out_f:
    
    # get one example for each intent
    # generates the respective story

    for intent in intent_list:
        # print('--', intent["intent"],)
        response=assistant.get_intent(
            workspace_id=config["workspace_id"],
            intent=intent["intent"],
            export=True
        ).get_result()

        request_example = response["examples"][0]

        out_f.write('\n')
        out_f.write('## {}\n'.format(intent['intent']))
        out_f.write('* {}: {}\n'.format(intent['intent'], request_example['text']))
        out_f.write('  - utter_{}\n'.format(intent['intent']))




