import sys
import os.path
import pandas as pd
import requests
import json

sys.path.append('/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project')
from clean_standings import team_ids
save_path = '/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project/Matches/'

# Manually enter team name and league ID (found in leagues_ids2.txt)
teams = {'Juventus': '891','Bayer Leverkusen':'754'}
for i in teams:
    team_id = team_ids[i]
    api_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/" + str(team_id) + "/" + str(teams[i])
    transfers = requests.get(api_url, headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})
    json_file = "JSON Files/" + str(i) + "_matches.json"
    saveName = os.path.join(save_path,json_file)
    to_json = transfers.json()
    json_dump = json.dumps(to_json)
    with open(saveName, 'w') as f:
        print(json_dump, file = f)
    """
    print(team_ids[i])
    print(i)
    print(teams[i])
    """
