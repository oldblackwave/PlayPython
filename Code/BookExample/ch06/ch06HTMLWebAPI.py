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


import pandas.io.data as web

from pandas import Series, DataFrame
from pandas.io.parsers import TextParser
from numpy import NaN as NA
from lxml.html import parse
from urllib.request import urlopen
from lxml import objectify
from io import StringIO

###############################################################

url = 'http://search.twitter.com/search.json?q=python%20pandas'
resp = requests.get(url)

print(resp)

data = json.loads(resp.text)
print(data.keys())
print('\n')

tweet_fields = ['created_at','from_user','id','text']
tweets = DataFrame(data['results'], columns=tweet_fields)

print(tweets)
print('\n')

tweets.ix[7]
###############################################################




