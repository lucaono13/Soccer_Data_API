from dict_create import d
import pandas as pd
import numpy as np
import json

## Change first paramenter for league name, second paramenter for year and third paramenter for nation

## Dictionary that stores the league name, year of league wanted, and nation
leagues = {'Serie A': ('2019','Italy'),\
'Premier League':('2019','England'), \
'Bundesliga 1':('2019','Germany'), \
'Ligue 1':('2019','France'),\
'Primera Division':('2019','Spain'),\
'Major League Soccer':('2019','USA')}

## Creates empty dictionary to hold league IDs
l_ids = {}

"""
for i in leagues:
    print (i)
    print (leagues[i][0])
    print (leagues[i][1])
"""

## Runs through all the ids in the dictionary with all league info and sees if it matches the one in above dictionary
for i in d:
    for x in leagues:
        if ((x in i) & (leagues[x][0] in i) & (leagues[x][1] in i) & ('Women' not in i)):
            l_ids.update({x : d[i]})

for key,value in l_ids.items():
    l_ids[key] = value.rstrip()

l_ids = {v.replace(" ",""):x
    for x,v in l_ids.items()}


"""
for i in d:
    if (("'Serie A' in i) & ('2019' in i) & ('Italy' in i)):
        serie_a = d[i]
    elif (('Premier League' in i) & ('2019' in i) & ('England' in i)):
        epl = d[i]
    elif (('Bundesliga 1' in i) & ('2019' in i) & ('Germany' in i)):
        bundes = d[i]
    elif (('Ligue 1' in i) & ('2019' in i) & ('France' in i)):
        ligue1 = d[i]
    elif (('Primera Division' in i) & ('2019' in i) & ('Spain' in i)):
        laliga = d[i]
    elif (('Major League Soccer' in i) & ('2019' in i) & ('USA' in i)):
        mls = d[i]


with open('big_league_id.txt','w') as f:
    print('Serie A: ' + str(serie_a), file = f)
    print('EPL: ' + str(epl), file = f)
    print('Bundesliga: ' + str(bundes), file = f)
    print('Ligue 1: ' + str(ligue1), file = f)
    print('La Liga: ' + str(laliga), file = f)
    print('MLS: ' + str(mls), file = f)
"""
