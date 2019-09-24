from dict_create import d
import pandas as pd
import numpy as np
import json

### For different leagues:
#### Key of dictionary is the league name; the first value is the year of the season wanted and the second value is the nation the league is from

## Dictionary that stores the league name, year of league wanted, and nation
leagues = {'Serie A': ('2019','Italy'),\
'Premier League':('2019','England'), \
'Bundesliga 1':('2019','Germany'), \
'Ligue 1':('2019','France'),\
'Primera Division':('2019','Spain'),\
'Major League Soccer':('2019','USA')}

## Creates empty dictionary to hold league IDs
l_ids = {}

## Runs through all the ids in the dictionary with all league info and sees if it matches the one in above dictionary
for i in d:
    for x in leagues:
        if ((x in i) & (leagues[x][0] in i) & (leagues[x][1] in i) & ('Women' not in i)):
            l_ids.update({x : d[i]})

# Strips the "\n" at the end of each value
for key,value in l_ids.items():
    l_ids[key] = value.rstrip()

# Strips the " " (space) in the value of the dictionary
l_ids = {v.replace(" ",""):x
    for x,v in l_ids.items()}
