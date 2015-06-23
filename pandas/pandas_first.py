import pandas as pd
import numpy as np
s = pd.Series([1,3,5,np.nan,6,8])
s
dates = pd.date_range('20130101',periods=6)
dates
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df


# MovieLens
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('/home/victor/Dropbox/Projects/data/MovieLens/ml-1m/users.dat',
                      sep='::', header=None, names=unames)
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('/home/victor/Dropbox/Projects/data/MovieLens/ml-1m/ratings.dat',
                        sep='::', header=None, names=rnames)
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('/home/victor/Dropbox/Projects/data/MovieLens/ml-1m/movies.dat',
                       sep='::', header=None, names=mnames)

data = pd.merge(pd.merge(ratings, users), movies)
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
mean_ratings[:5]
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]
active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles
mean_ratings = mean_ratings.ix[active_titles]
mean_ratings
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]