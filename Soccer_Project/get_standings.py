import pandas as pd
import numpy as np
import json
import requests
import os.path
from get_league_standing import l_ids

## Get where you want to save the files and change/add to these
# Linux Save Path
#save_path = '/home/lucaono13/Documents/Soccer_Project/League_Standings/'
# Surface Laptop Save Path
save_path = 'C:/Users/Owner/Box Sync/API_Projects/Soccer_Data_API/Soccer_Project/League_Standings/'

# Function that takes in league name and league ID and reqests the standings from the API and then writes the JSON string to a JSON file with the name of the league
def get_standing(league_name,league_id):
    api_url = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/" + str(league_id)
    table = requests.get(api_url,headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})
    json_file = str(league_name) + ".json"
    completeName = os.path.join(save_path, json_file)
    to_json = table.json()
    json_dump = json.dumps(to_json)
    with open(completeName, 'w') as f:
        print(json_dump, file = f)

# For each key in the dictionary created in get_league_standing.py, it runs the function
for i in l_ids:
    #print(l_ids[i] + ' ' +i)
    get_standing(l_ids[i], i)
