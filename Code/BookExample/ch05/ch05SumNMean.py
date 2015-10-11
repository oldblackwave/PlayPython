import numpy as np
import pandas as pd

import pandas.io.data as web

from pandas import Series, DataFrame

###############################################################

df = DataFrame([[1.4, np.nan], [7.1,-4.5], [np.nan, np.nan], [0.75, -1.3]],
               index = ['a','b','c','d'],
               columns=['one','two']
               )

print(df)
print('\n')
print(df.sum())
print('\n')
print(df.sum(axis=1))
print('\n')
print(df.mean())
print('\n')
print(df.mean(axis=1,skipna=False))
print('\n')
print(df.idxmax())
print('\n')
print(df.cumsum())
print('\n')
print(df.cumsum(axis=1))
print('\n')
print(df.describe())
print('\n')

###############################################################

obj = Series(['a','a','b','c']*4)
print(obj)
print(obj.describe())
print('\n')

###############################################################

all_data = {}

for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOGL']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2010', '2/1/2010')

price = DataFrame({tic:data['Adj Close']
                            for tic, data in all_data.items()})
volume = DataFrame({tic:data['Volume']
                            for tic, data in all_data.items()})

print(price)

    
    
    
    
    
    
    

