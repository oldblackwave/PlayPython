import numpy as np
import pandas as pd
import pandas.io.data as web
import sys 
import csv

import pandas.io.data as web

from pandas import Series, DataFrame
from numpy import NaN as NA

###############################################################

f = open('data/ex7.csv')
reader = csv.reader(f)

for line in reader:
    print(line)
    
print('\n')
###############################################################

lines = list(csv.reader(open('data/ex7.csv')))
header, values = lines[0], lines[1:]
data_dict = {h: v for h,v in zip(header, zip(*values))}

print(data_dict)

print('\n')


###############################################################

class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    
reader = csv.reader(f, dialect=my_dialect)

reader = csv.reader(f, delimiter='|')

###############################################################

with open('data/mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('4','5','6'))
    writer.writerow(('7','8','9'))
    
    
    
    
