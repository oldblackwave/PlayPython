import numpy as np
import pandas as pd
import pandas.io.data as web
import sys
import csv
import json
import urllib

import pandas.io.data as web

from pandas import Series, DataFrame
from pandas.io.parsers import TextParser
from numpy import NaN as NA
from lxml.html import parse
from urllib.request import urlopen
from lxml import objectify
from io import StringIO

###############################################################

df = DataFrame(np.arange(5*4).reshape(5,4))
sampler = np.random.permutation(5)
print(sampler)
print('\n')

print(df)
print(df.take(sampler))
print('\n')
print(df.take(np.random.permutation(len(df))[:3]))

bag = np.array([5,7,-1,6,4])

sampler = np.random.randint(0,len(bag), size=10)

print(sampler)
print('\n')

draws = bag.take(sampler)

print(draws)
print('\n')

###############################################################

df = DataFrame({'key':['b','b','a','c','a','b'],
                'data1':range(6)})
print(df)
print(pd.get_dummies(df['key']))
print('\n')

dummies = pd.get_dummies(df['key'],prefix='key')

df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)
print('\n')


###############################################################

mnames = ['moive_id', 'title', 'genres']
moives = pd.read_table('data/movies.dat', sep='::', header=None, names=mnames)

print(moives[:10])
print('\n')

genre_iter = (set(x.split('|')) for x in moives.genres)
genres = sorted(set.union(*genre_iter))

dummies = DataFrame(np.zeros((len(moives), len(genres))), columns=genres)

for i, gen in enumerate(moives.genres):
    dummies.ix[i, gen.split('|')] = 1

moives_windic = moives.join(dummies.add_prefix('Genre_'))

print(moives_windic.ix[0])

print('\n')


values = np.random.rand(10)

print(values)

bins = [0,0.2,0.4,0.6,0.8,1]
print(pd.get_dummies(pd.cut(values,bins)))

print('\n')






