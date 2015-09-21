from pandas import DataFrame, Series
from numpy import arange
from gc import get_count
from matplotlib.pyplot import plot

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import pylab

###############################################################
names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
###############################################################

#print(names1880)
print('\n')
###############################################################

#print(names1880.groupby('sex').births.sum())
print('\n')
#print(names1880.groupby('name').sex.sum())
print('\n')

###############################################################
years = range(1880,2011)

pieces = []
colums = ['name','sex','births']

for year in years:
    #print(year)
    path = 'names/yob' + str(year) + '.txt'
    frame = pd.read_csv(path, names=colums)
    
    frame['year']=year
    pieces.append(frame)

#print(pieces[1])
names = pd.concat(pieces, ignore_index=True)

print(names[:10])
print('\n')

###############################################################

total_births = names.pivot_table('births','year','sex',sum)# sum of births on Rows=year and Cols=sex
print(total_births)
print(total_births.tail())
print('\n')

###############################################################
def add_prop(group):
    births = group.births.astype(float)
    
    group['prop'] = births/births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)
print(names)
###############################################################
print('\n')
print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))
