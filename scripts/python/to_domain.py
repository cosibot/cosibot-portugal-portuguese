import os
from os.path import join, exists
import json
import yaml

"""WARNING: responses indentation is not completely correct."""

answers_dir = './examples/'
output_dir = './bot_files/'
if not exists(output_dir):
    os.makedirs(output_dir)

intents = [file.replace('de_', '').replace('.json', '') for file in os.listdir(answers_dir) if file.endswith('.json')]
intents_dict = {'intents' : intents}

all_answers = {}

for file in os.listdir(answers_dir):
    if file.endswith('.json'):
        # print(file)
        with open(join(answers_dir, file), 'r', encoding='utf-8') as f:
            all_answers[file.replace('de_', '').replace('.json', '')] = json.load(f)

utter = {}

for intent, answer in all_answers.items():
    utter['utter_' + intent] = {'custom' : answer}

responses_dict = {'responses' : utter}

with open(join(output_dir, 'domain.yml'), 'w', encoding='utf-8') as out_f:
    yaml.dump(intents_dict, out_f, allow_unicode=True)
    yaml.dump(responses_dict, out_f, allow_unicode=True)
