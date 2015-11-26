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

ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]

print(ages)
print(bins)
print('\n')

cats = pd.cut(ages,bins)

print(cats)
print('\n')

print(cats.labels)
print('\n')

print(cats.levels)
print('\n')

print(pd.value_counts(cats))
print('\n')

print(pd.cut(ages, [18,26,36,61,100], right=False))
print('\n')

###############################################################

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))
print('\n')

data = np.random.rand(20)
print(pd.cut(data, 4, precision=2))
print('\n')

data = np.random.randn(1000)
cats = pd.qcut(data, 4)
print(cats)

print('\n')

print(pd.value_counts(cats))
print(pd.qcut(data,[0,0.1,0.5,0.9,1.]))
print('\n')
###############################################################

np.random.seed(12345)
data = DataFrame(np.random.randn(1000,4))
print(data.describe())

print('\n')

col = data[3]
print(col[np.abs(col)>3])
print('\n')
print(data[(np.abs(data)>3).any(1)])
print('\n')
data[np.abs(data)>3] = np.sign(data)*3
print(data.describe())
print('\n')


