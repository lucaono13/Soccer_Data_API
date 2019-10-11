import os
import json
import pandas as pd
from get_league_standing import l_ids

# Dictionary for all team IDs
team_ids = {}

# Function that takes in the league name and cleans up the standings to look presentable. Also prints the standings out at the end (uncomment for this)
def standings(league_name):
    path_f = "League_Standings/" + str(league_name) + ".json"
    clean_stds = pd.DataFrame(columns = ['Rank','Name','ID','Played','Wins','Draws','Losses','Points','GF','GA','GD','Form'])
    with open(path_f, 'r') as f:
        data = json.load(f)
    for i in data['api']['standings']:
        for x in i:
            clean_stds = clean_stds.append({'Rank':str(x['rank']),'Name':str(x['teamName']),'ID':str(x['team_id']),'Played':str(x['all']['matchsPlayed']),'Wins':str(x['all']['win']),'Draws':str(x['all']['draw']),'Losses':str(x['all']['lose']),'Points':str(x['points']),'GF':str(x['all']['goalsFor']),'GA':str(x['all']['goalsAgainst']),'GD':str(x['goalsDiff']),'Form':str(x['forme'])}, ignore_index = True)
            team_ids[x['teamName']] = x['team_id']
    new_name = "Cleaned_Up_Standings/" + league_name + "_standings.csv"
    clean_stds.set_index('Rank', inplace = True)
    clean_stds.to_csv(new_name)


    # print(clean_stds)

# Iterates through the get_league_standing.py dictionary to get clean standings
for i in l_ids:
    standings(l_ids[i])
