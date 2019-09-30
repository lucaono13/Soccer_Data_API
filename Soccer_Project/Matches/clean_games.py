"""
fixture_id : integer
league_id : integer
event_date : string
event_timestamp : integer
firstHalfStart : integer
secondHalfStart : integer
round : string
status : string
statusShort : string
elapsed : integer
venue : string
referee : string
homeTeam->team_id : integer
homeTeam->team_name : string
homeTeam->logo : string image in png format, 150/150px
awayTeam->team_id : integer
awayTeam->team_name : string
awayTeam->logo : string image in png format, 150/150px
goalsHomeTeam : integer
goalsAwayTeam : integer
score->halftime : string
score->fulltime : string
score->extratime : string
score->penalty : string
"""
import pandas as pd
import json
from get_matches import teams

def matches(team_name):
    path_f = "/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project/Matches/JSON Files/" + str(team_name) + "_matches.json"
    clean_match = pd.DataFrame(columns = ['Round','Home_Team','Home_Goals','Away_Team','Away_Goals','Date','Venue','Referee','Elapsed'])
    with open(path_f,'r') as f:
        data = json.load(f)
    for i in data['api']['fixtures']:
        clean_match = clean_match.append({'Round':i['round'],'Home_Team':i['homeTeam']['team_name'],'Home_Goals':i['goalsHomeTeam'],'Away_Team':i['awayTeam']['team_name'],'Away_Goals':i['goalsAwayTeam'],'Date':i['event_date'],'Venue':i['venue'],'Referee':i['referee'],'Elapsed':i['elapsed']}, ignore_index = True)
    new_name = "/home/lucaono13/Documents/GitHub_Projects/APIs/Soccer/Soccer_Project/Matches/CMatches/" + team_name + "_matches.csv"
    clean_match.to_csv(new_name)

for i in teams:
    matches(i)
