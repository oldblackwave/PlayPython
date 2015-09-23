from pandas import DataFrame, Series
from numpy import arange
from gc import get_count
from matplotlib.pyplot import plot, subplots, yticks, xticks

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

#print(names[:10])
print('\n')

###############################################################

total_births = names.pivot_table('births','year','sex',sum)# sum of births on Rows=year and Cols=sex
#print(total_births)
#print(total_births.tail())
print('\n')

###############################################################
def add_prop(group):
    births = group.births.astype(float)
    
    group['prop'] = births/births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)
#print(names)
###############################################################
print('\n')
#print(np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1))
print('\n')
###############################################################
def get_top1000(group):
    return group.sort_index(by='births', ascending = False)[:1000]

grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
#print(top1000)
print('\n')
###############################################################
pieces = []
for year, group in names.groupby(['year','sex']):
    pieces.append(group.sort_index(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)
#print(top1000)
print('\n')
###############################################################
boys = top1000[top1000.sex == 'M']
#print(boys)
girls = top1000[top1000.sex == 'F']
#print(girls)
print('\n')

###############################################################
total_births = top1000.pivot_table('births','year','name',sum)
#print(total_births)
print('\n')

subset = total_births[['John','Harry','Mary','Marilyn']]
#subset.plot(subplots=True, figsize=(12,10),grid=False,title="Number of births per year")
#pylab.show()

###############################################################
table = top1000.pivot_table('prop', 'year', 'sex', sum)
#table.plot(title="Sum of table1000.prop by year and sex", yticks=np.linspace(0, 1.2, 13), xticks=range(1880,2020,10))
#pylab.show()

###############################################################

df2010 = boys[boys.year == 2010]
print(df2010)
print('\n')

df1880 = boys[boys.year == 1880]
print(df1880)
print('\n')

###############################################################
prop_cumsum = df2010.sort_index(by='prop', ascending=False).prop.cumsum()
print(prop_cumsum[:10])
print('\n')

print(prop_cumsum.searchsorted(0.5))
print('\n')
###############################################################

df1900 = boys[boys.year == 1990]
in1900 = df1900.sort_index(by='prop', ascending=False).prop.cumsum()
print(in1900.searchsorted(0.5)+1)
print('\n')
###############################################################
def get_quantile_count(group, q=0.5):
    group = group.sort_index(by='prop',ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1

diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

print(diversity)
print('\n')
print(diversity.head())
diversity.plot()
print('\n')

pylab.show()
###############################################################







