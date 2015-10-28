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


frame = pd.read_csv('data/ex1.csv')
print(frame)
print('\n')

#frame.save('data/frame_pickle')
print(pd.load('data/frame_pickle'))
print('\n')
print(pd.read_pickle('data/frame_pickle'))
print('\n')

###############################################################


xls_file = pd.ExcelFile('data/data.xls')
table = xls_file.parse('Sheet1')

print(table)

print('\n')





