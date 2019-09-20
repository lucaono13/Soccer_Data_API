import pandas as pd
import numpy as np
import json

d = {}

with open('leagues_ids2.txt','r') as text_file:
    for line in text_file:
        (key,val) = line.split(":")
        d[(key)] = val
"""
for i in d:
    if (('Italy' in i) & ('2019' in i) & ('Serie A' in i)):
        print (d[i])
"""
