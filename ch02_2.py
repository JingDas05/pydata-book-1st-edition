# -*- encoding: utf-8 -*-
import pandas as pd
import os
import sys

# 为了防止报错，设置编码为latin1
reload(sys)
sys.setdefaultencoding('latin1')
encoding = 'latin1'

upath = os.path.expanduser('ch02/movielens/users.dat')
rpath = os.path.expanduser('ch02/movielens/ratings.dat')
mpath = os.path.expanduser('ch02/movielens/movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding, engine='python')
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding, engine='python')
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding, engine='python')

# print movies[:5]
# print ratings[:5]
# print users[:5]

# 类似于数据库里面的join查询
data = pd.merge(pd.merge(ratings, users), movies)
# print data[:1]


mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# print mean_ratings[:5]

ratings_by_title = data.groupby('title').size()
print ratings_by_title[:5]

active_titles = ratings_by_title.index[ratings_by_title >= 250]
# print active_titles[:10]

mean_ratings = mean_ratings.ix[active_titles]
# print mean_ratings