import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import json

from matplotlib.pyplot import plot
from numpy import arange
from gc import get_count
from collections import defaultdict

path = 'usagov_bitly_data2012-03-16-1331923249.txt'

#records = [json.loads(line) for line in open(path)] #return List

records = []
for line in open(path):
    #print(type(line),line)
    records.append(json.loads(line))

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones)
print(time_zones[:10])
print('\n')