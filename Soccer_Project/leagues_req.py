### Only need to do once
import requests
import json
import pandas as pd
from collections import namedtuple

# Gets all leagues across all countries
leagues = requests.get('https://api-football-v1.p.rapidapi.com/v2/leagues',headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})

# Reads the api get as a json
leagues1 = leagues.json()

# Converts leagues1 to JSON string
leagues2 = json.dumps(leagues1)


# Writes JSON string to leagues_avail.json
with open('leagues_avail.json','w') as text_file:
	print(leagues2, file = text_file)
