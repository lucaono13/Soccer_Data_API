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


def get_standing(league_name,league_id):
    api_url = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/" + str(league_id)
    table = requests.get(api_url,headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})
    json_file = str(league_name) + ".json"
    completeName = os.path.join(save_path, json_file)
    to_json = table.json()
    json_dump = json.dumps(to_json)
    with open(completeName, 'w') as f:
        print(json_dump, file = f)

for i in l_ids:
    #print(l_ids[i] + ' ' +i)
    get_standing(l_ids[i], i)


## Use leagues_ids2.txt to get league ID

"""

serie_a_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/891',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "serie_a.json")
serie_a = serie_a_table.json()
serie_a = json.dumps(serie_a)
with open(completeName,'w') as f:
  print(serie_a, file = f)

epl_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/524',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "epl.json")
epl = epl_table.json()
epl = json.dumps(epl)
with open(completeName,'w') as f:
  print(epl, file = f)

bundes_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/754',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "bundes.json")
bundes = bundes_table.json()
bundes = json.dumps(bundes)
with open(completeName,'w') as f:
  print(bundes, file = f)

ligue1_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/525',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "ligue1.json")
ligue1 = ligue1_table.json()
ligue1 = json.dumps(ligue1)
with open(completeName,'w') as f:
  print(ligue1, file = f)

laliga_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/920',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "laliga.json")
laliga = laliga_table.json()
laliga = json.dumps(laliga)
with open(completeName,'w') as f:
  print(laliga, file = f)

mls_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/294',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "mls.json")
mls = mls_table.json()
mls = json.dumps(mls)
with open(completeName,'w') as f:
  print(mls, file = f)

"""
