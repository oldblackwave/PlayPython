import numpy as np
import pandas as pd
import pandas.io.data as web
import sys 

import pandas.io.data as web

from pandas import Series, DataFrame
from numpy import NaN as NA

###############################################################


print(pd.read_csv('data/ex1.csv', sep=','))

print('\n')

print(pd.read_csv('data/ex2.csv', header=None))

print('\n')

print(pd.read_csv('data/ex2.csv', names=['a','b','c','d', 'message']))

print('\n')

names = ['a','b','c','d','message']
print(pd.read_csv('data/ex2.csv', names=names, index_col='message'))

print('\n')

parsed = pd.read_csv('data/csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)

print('\n')

print(list(open('data/ex3.txt')))

print('\n')

result = pd.read_table('data/ex3.txt', sep='\s+')
print(result)

print('\n')

print(pd.read_csv('data/ex4.csv', skiprows=[0,2,3]))
print('\n')

result = pd.read_csv('data/ex5.csv')
print(result)

print('\n')

print(pd.isnull(result))

print('\n')

result = pd.read_csv('data/ex5.csv', na_values=['NULL'])
print(result)

print('\n')

sentinels = {'message':['foo', 'NA'], 'something':['two']}
print(pd.read_csv('data/ex5.csv', na_values=sentinels))

print('\n')

result = pd.read_csv('data/ex6.csv')
#print(result)

print('\n')

print(pd.read_csv('data/ex6.csv', nrows=5))

print('\n')

chunker = pd.read_csv('data/ex6.csv', chunksize = 1000)
print(chunker)

print('\n')

tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.order(ascending=False)
print(tot)

print('\n')

data = pd.read_csv('data/ex5.csv')
print(data)
#data.to_csv('data/out01.csv')

print('\n')

print(data.to_csv(sys.stdout, sep='|'))

print('\n')

print(data.to_csv(sys.stdout, na_rep='NULL'))














