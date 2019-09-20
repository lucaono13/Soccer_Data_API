import pandas as pd
import numpy as np
import json

#f = open('leagues_avail.json','r')

#loaded_json = json.loads(f)
#print(loaded_json)

with open('leagues_avail.json','r') as f:
    data = json.load(f)

"""
with open('leagues_ids.txt','w') as text_file:
    for i in data['api']['leagues']:
        print(str(i['name']) + '(' + str(i['country']) + '; ' + str(i['season']) + '): ' + str(i['league_id']), file = text_file)
"""
with open('leagues_ids2.txt','w') as text_file:
    for i in data['api']['leagues']:
        print(str(i['name']) + ' ' + str(i['season']) + ' (' + str(i['country']) + '): ' + str(i['league_id']),file = text_file)



"""
with open('leagues_ids.txt','r') as text_file:
    league_text = text_file.readlines()

for i in league_text:
    if (('2019' in i) & ('Italy' in i)):
        print(i)
"""
