import pandas as pd
import sys
import requests
import json
import os.path
# Don't remove
sys.path.append('/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project')
from clean_standings import team_ids

save_path = '/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project/Transfers/'
#team_ids = pd.read_csv('/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project/Cleaned_Up_Standings/Serie A_standings.csv')
#print(team_ids['Juventus'])
teams = ['Juventus','Manchester City']
for i in teams:
    team_id = team_ids[i]
    api_url = "https://api-football-v1.p.rapidapi.com/v2/transfers/team/" + str(team_id)
    transfers = requests.get(api_url, headers = {'X-RapidAPI-Key' : '9cd6c83d63msh4525a1ecc10ff3ep1a4e35jsnbcb3e792b9e4', 'Accept' : 'application/json'})
    json_file = "JSON Files/" + str(i) + "_transfers.json"
    completeName = os.path.join(save_path,json_file)
    to_json = transfers.json()
    json_dump = json.dumps(to_json)
    with open(completeName, 'w') as f:
        print(json_dump,file = f)
