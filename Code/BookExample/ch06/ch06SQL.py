import numpy as np
import pandas as pd
import pandas.io.data as web
import sys 
import csv
import json
import urllib
import requests
import sqlite3
import pymongo
import sqlite3
import pandas.io.sql as sql
import pymongo

import pandas.io.data as web

from pandas import Series, DataFrame
from pandas.io.parsers import TextParser
from numpy import NaN as NA
from lxml.html import parse
from urllib.request import urlopen
from lxml import objectify
from io import StringIO

###############################################################

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);
"""

con = sqlite3.connect(':memory:')
con.execute(query)

con.commit()

###############################################################

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)
        ]

stmt = "INSERT INTO test VALUES(?,?,?,?)"

con.executemany(stmt,data)
con.commit()


###############################################################

cursor = con.execute('select * from test')
rows = cursor.fetchall()

print(rows)
print('\n')
print(cursor.description)

print('\n')

testDataFrame = DataFrame(rows)
print(testDataFrame)
print('\n')
###############################################################

print(sql.read_frame('Select * from test', con))
print('\n')
###############################################################

con = pymongo.Connection('localhost', port = 27017)
tweets = con.db.tweets

url = 'http://search.twitter.com/search.json?q=python%20pandas'
data = json.loads(requests.get(url).text)

for tweet in data['result']:
    tweet.save(tweet)
    
cursor = tweets.find({'from_user':'wesmckinn'})

tweet_fields = ['created_at', 'from_user', 'id', 'text']
result = DataFrame(list(cursor), columns=tweet_fields)















