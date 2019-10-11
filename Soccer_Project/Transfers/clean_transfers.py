"""
Response:
player_id : integer
player_name : string
transfer_date : date YYYY-MM-DD
type : string
team_in->team_id : integer
team_in->team_name : string
team_out->team_id : integer
team_out->team_name : string
lastUpdate : integer
"""
import pandas as pd
from teams import teams
import json
def transfers(team_name):
    path_f = str(team_name) + "_transfers.json"
    clean_trfs = pd.DataFrame(columns = ['Name','Old_Team','Fee','New_Team','Date'])
    with open(path_f,'r') as f:
        data = json.load(f)
    for i in data['api']['transfers']:
        clean_trfs = clean_trfs.append({'Name':i['player_name'],'Old_Team':i['team_out']['team_name'],'Fee':i['type'],'New_Team':i['team_in']['team_name'],'Date':i['transfer_date']}, ignore_index = True)
    new_name = "/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project/Transfers/CTransfers/" + team_name + "_transfers.csv"
    clean_trfs.to_csv(new_name)

for i in teams:
    transfers(i)
