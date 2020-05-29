import os
from os.path import join, exists
import json
import yaml

answers_dir = './examples/'
output_dir = './bot_files/'
if not exists(output_dir):
    os.makedirs(output_dir)

with open(join(output_dir, 'stories.md'), 'w', encoding='utf-8') as out_f:
    for file in os.listdir(answers_dir):
        if file.endswith('.json'):
            out_f.write('\n')
            out_f.write('## {}\n'.format(file.replace('.json', '')))
            out_f.write('* {}\n'.format(file.replace('.json', '')))
            out_f.write('  - utter_{}\n'.format(file.replace('.json', '')))