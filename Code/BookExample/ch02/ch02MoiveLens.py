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

###############################################################

print(users[:5])
print('\n')
print(ratings[:5])
print('\n')
print(movies[:10])
print('\n')

###############################################################

data = pd.merge(pd.merge(ratings, users),movies)
print(data[:5])
print('\n')
print(data.ix[0])
print('\n')
###############################################################

#mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
mean_ratings = data.pivot_table('rating', 'title', 'gender', 'mean')
print(mean_ratings[:5])
print('\n')
###############################################################

ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])
print('\n')
###############################################################

active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles)
print('\n')

###############################################################
mean_ratings = mean_ratings.ix[active_titles]
print(mean_ratings)
print('\n')

###############################################################
top_female_ratings = mean_ratings.sort_index(by='F', ascending =False)
print(top_female_ratings[:10])
print('\n')
###############################################################
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
print(sorted_by_diff[:15])
print('\n')
print(sorted_by_diff[::-1][:15])
print('\n')
###############################################################
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]
print(rating_std_by_title.order(ascending=False))

