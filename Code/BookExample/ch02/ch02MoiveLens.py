from pandas import DataFrame, Series
from numpy import arange
from gc import get_count
from matplotlib.pyplot import plot

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import pylab
from email._header_value_parser import Header

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('movielens\\users.dat',sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('movielens\\ratings.dat',sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movielens\\movies.dat',sep='::', header=None, names=mnames, engine='python')

