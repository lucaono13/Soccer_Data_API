import requests
import json
import pandas as pd
from collections import namedtuple

def _json_object_hook(d):
	return namedtuple('X',d.keys())(*d.values())

def json2obj(data):
	return json.loads(data,object_hook = _json_object_hook)


# Below code gets lineup data from api
#f = requests.get('https://www.api-football.com/demo/api/v2/lineups/341')

# Event Data
f = requests.get('https://www.api-football.com/demo/api/v2/teams/league/2')

# Creates Python Object from API Data (if it was a JSON)
f1 = f.json()

print(str(f1))

# How to get the unique ID for each team in a league (alphabetical based on the season's teams (aka. Bournemouth is first because name is AFC Bournemouth))
teams = f1['api']['teams']

# Print out each teams ID
#for i in range(len(team_id)):
#	print(str(team_id[i]['name']) + ': ' + str(team_id[i]['team_id']))
#	{}.format(str(team_id[i]['name'])) = team_id[i]['team_id']

# Print out team name and ID to Text file
with open('epl_team_id.txt','w') as text_file:
	for i in range(len(teams)):
		print(str(teams[i]['name']) + ': ' + str(teams[i]['team_id']), file = text_file)


with open('out1.txt','w') as text_file:
	print(f1, file = text_file)


# Do not use numbers, creates error due to this not being a list, but a dictionary. Still need to figure out how to create list from dictionary and if it is efficient to.
# Creates a dictionary with the part of the lineups for each team
#man_city = f1['api']['lineUps']
#print(man_city)

# Prints the name of each player in the starting XI for the first team and then print their number (use for loop to do both at same time)
#for i in range(11):
#	print(str(man_city['Manchester City']['startXI'][i]['player']) + ' (' + str(man_city['Manchester City']['startXI'][i]['number']) + ')')