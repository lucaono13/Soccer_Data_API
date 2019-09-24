import pandas as pd
import numpy as np
import json

# Open json file with league info
with open('leagues_avail.json','r') as f:
    data = json.load(f)

# Create clean "leagues_ids2.txt" file as a clean way to see all leagues and their respective IDs
with open('leagues_ids2.txt','w') as text_file:
    for i in data['api']['leagues']:
        print(str(i['name']) + ' ' + str(i['season']) + ' (' + str(i['country']) + '): ' + str(i['league_id']),file = text_file)
