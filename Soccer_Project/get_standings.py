import pandas as pd
import numpy as np
import json
import requests
import os.path
save_path = '/home/lucaono13/Documents/League Standings/'

serie_a_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/891',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "serie_a.txt")
serie_a = serie_a_table.json()
serie_a = json.dumps(serie_a)
with open(completeName,'w') as f:
  print(serie_a, file = f)

epl_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/524',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "epl.txt")
epl = epl_table.json()
epl = json.dumps(epl)
with open(completeName,'w') as f:
  print(epl, file = f)

bundes_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/754',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "bundes.txt")
bundes = bundes_table.json()
bundes = json.dumps(bundes)
with open(completeName,'w') as f:
  print(bundes, file = f)

ligue1_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/525',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "ligue1.txt")
ligue1 = ligue1_table.json()
ligue1 = json.dumps(ligue1)
with open(completeName,'w') as f:
  print(ligue1, file = f)

laliga_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/920',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "laliga.txt")
laliga = laliga_table.json()
laliga = json.dumps(laliga)
with open(completeName,'w') as f:
  print(laliga, file = f)

mls_table = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagueTable/294',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

completeName = os.path.join(save_path, "mls.txt")
mls = mls_table.json()
mls = json.dumps(mls)
with open(completeName,'w') as f:
  print(mls, file = f)
