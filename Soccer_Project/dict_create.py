import pandas as pd
import numpy as np
import json

# Creates empty dictionary
d = {}

# Fills dictionary with league name, year, and nation as the key and the league ID as the value
with open('leagues_ids2.txt','r') as text_file:
    for line in text_file:
        (key,val) = line.split(":")
        d[(key)] = val
