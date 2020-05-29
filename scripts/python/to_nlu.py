import json 
from os.path import exists, join
import os

input_path = './intents_examples/intents.json'
output_dir = './bot_files/'
if not exists(output_dir):
    os.makedirs(output_dir)

with open(input_path, 'r', encoding='utf-8') as f:
    intents_dict = json.load(f)

with open(join(output_dir, 'nlu.md'), 'w', encoding='utf-8') as out_f:
    for intent, examples in intents_dict.items(): 
        # print('## intent: {} \n'.format(intent))
        out_f.write('## intent: {} \n'.format(intent))
        for ex in examples: 
            out_f.write('- {} \n'.format(ex))
            # print('- {} \n'.format(ex))