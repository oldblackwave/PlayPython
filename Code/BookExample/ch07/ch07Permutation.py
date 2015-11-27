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
moives = pd.read_table('data/moives.dat', sep='::', header=None, names=mnames)


