import os
import json
import pandas as pd

os.getcwd()
seriea_df = pd.DataFrame(columns = ['Rank','Name','Played','Wins','Draws','Losses','Points','GF','GA','GD','Form'])
with open('League_Standings/serie_a.txt','r') as f:
    data = json.load(f)

#data = json.dumps(data)
#print(data['api']['standings']['rank'])


for i in data['api']['standings']:
    for x in i:
        seriea_df = seriea_df.append({'Rank':str(x['rank']),'Name':str(x['teamName']),'Played':str(x['all']['matchsPlayed']),'Wins':str(x['all']['win']),'Draws':str(x['all']['draw']),'Losses':str(x['all']['lose']),'Points':str(x['points']),'GF':str(x['all']['goalsFor']),'GA':str(x['all']['goalsAgainst']),'GD':str(x['goalsDiff']),'Form':str(x['forme'])}, ignore_index = True)
