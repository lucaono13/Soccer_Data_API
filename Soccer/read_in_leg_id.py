import pandas as pd
import numpy as np
import json

with open('leagues_avail.json','r') as f:
    data = json.load(f)

for i in data:
    print(i)
