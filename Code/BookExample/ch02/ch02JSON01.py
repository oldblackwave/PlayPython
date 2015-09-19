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

records = [json.loads(line) for line in open(path)] #return List
'''
for line in open(path):
    records = []
    #print(type(line),line)
    records.append(json.loads(line))
'''
#print(type(records).records)

print(type(records),records[0])
print('\n')
print(records[0]['a'])
print(records[0]['tz'])
print(records[0]['nk'])
print(records[0]['c'])
print(records[0]['g'])
print(records[0]['h'])
print(records[0]['l'])
print(records[0]['hh'])
print(records[0]['r'])
print('\n')