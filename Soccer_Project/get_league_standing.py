from dict_create import d
import pandas as pd
import numpy as np
import json

for i in d:
    if (('Serie A' in i) & ('2019' in i) & ('Italy' in i)):
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
