import pandas as pd
import numpy as np
import json

with open('leagues_avail.json','r') as f:
    data = json.load(f)
    
with open('leagues_ids2.txt','w') as text_file:
    for i in data['api']['leagues']:
        print(str(i['name']) + ' ' + str(i['season']) + ' (' + str(i['country']) + '): ' + str(i['league_id']),file = text_file)
