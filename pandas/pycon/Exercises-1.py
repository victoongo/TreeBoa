
# coding: utf-8

# In[1]:
import os
#get_ipython().magic(u'matplotlib inline')
import pandas as pd
os.chdir('/home/victor/Dropbox/Projects/TreeBoa/pandas/pycon')

# In[2]:
#from IPython.core.display import HTML
#css = open('style-table.css').read() + open('style-notebook.css').read()
#HTML('<style>{}</style>'.format(css))


# In[3]:
titles = pd.DataFrame.from_csv('data/titles.csv', index_col=None)
titles.head()

# In[4]:
cast = pd.DataFrame.from_csv('data/cast.csv', index_col=None)
cast.head()

# ### How many movies are listed in the titles dataframe?

# In[ ]:
len(titles.title)
len(titles)

# ### What are the earliest two films listed in the titles dataframe?

# In[ ]:
titles.sort(['year']).head(2)

# ### How many movies have the title "Hamlet"?

# In[ ]:
len(titles[titles.title == "Hamlet"])

# ### How many movies are titled "North by Northwest"?

# In[ ]:
len(titles[titles.title == "North by Northwest"])

# ### When was the first movie titled "Hamlet" made?

# In[ ]:
titles[titles.title == "Hamlet"].sort('year').head(1)


# ### List all of the "Treasure Island" movies from earliest to most recent.

# In[ ]:
titles[titles.title == "Treasure Island"].sort('year')

# ### How many movies were made in the year 1950?

# In[ ]:
len(titles[titles.year == 1950])

# ### How many movies were made in the year 1960?

# In[ ]:
len(titles[titles.year == 1960])

# ### How many movies were made from 1950 through 1959?

# In[ ]:
len(titles[titles.year // 10 == 195])
len(titles[(titles.year >= 1950) & (titles.year <= 1959)]) # and doesn't work
# titles.year in range(1950, 1960)


# ### In what years has a movie titled "Batman" been released?

# In[ ]:
titles.year[titles.title == "Batman"]#.distinct()

# ### How many roles were there in the movie "Inception"?

# In[ ]:
len(cast.character[cast.title == "Inception"])

# ### How many roles in the movie "Inception" are NOT ranked by an "n" value?

# In[ ]:
sum(cast.n[cast.title == "Inception"].isnull()) # notnull() returns boolen

# ### But how many roles in the movie "Inception" did receive an "n" value?

# In[ ]:
sum(cast.n[cast.title == "Inception"].notnull())

# ### Display the cast of "North by Northwest" in their correct "n"-value order, ignoring roles that did not earn a numeric "n" value.

# In[ ]:
nbn = cast[cast.title == "North by Northwest"]
nbn = nbn[nbn.n.notnull()]
nbn.sort('n').name

# ### Display the entire cast, in "n"-order, of the 1972 film "Sleuth".

# In[ ]:
cast[(cast.title == "Sleuth") & (cast.year == 1972)].sort('n').name

# ### Now display the entire cast, in "n"-order, of the 2007 version of "Sleuth".

# In[ ]:
cast[(cast.title == "Sleuth") & (cast.year == 2007)].sort('n').name

# ### How many roles were credited in the silent 1921 version of Hamlet?

# In[ ]:
len(cast[(cast.title == "Hamlet") & (cast.year == 1921)])

# ### How many roles were credited in Branagh’s 1996 Hamlet?

# In[ ]:
len(cast[(cast.title == "Hamlet") & (cast.year == 1996)])

# ### How many "Hamlet" roles have been listed in all film credits through history?

# In[ ]:
len(cast[cast.title == "Hamlet"])

# ### How many people have played an "Ophelia"?

# In[ ]:
len(cast[cast.character == "Ophelia"])

# ### How many people have played a role called "The Dude"?

# In[ ]:
len(cast[cast.character == "The Dude"])

# ### How many people have played a role called "The Stranger"?

# In[ ]:
len(cast[cast.character == "The Stranger"])

# ### How many roles has Sidney Poitier played throughout his career?

# In[ ]:
len(cast[cast.name == "Sidney Poitier"])

# ### How many roles has Judi Dench played?

# In[ ]:
len(cast[cast.name == "Judi Dench"])

# ### List the supporting roles (having n=2) played by Cary Grant in the 1940s, in order by year.

# In[ ]:
cast[(cast.name == "Cary Grant") & (cast.year // 10 == 194) & (cast.n == 2)].sort('year')

# ### List the leading roles that Cary Grant played in the 1940s in order by year.

# In[ ]:
cast[(cast.name == "Cary Grant") & (cast.year // 10 == 194) & (cast.n == 1)].sort('year')

# ### How many roles were available for actors in the 1950s?

# In[ ]:
len(cast[(cast.type == "actor") & (cast.year // 10 == 195)])

# ### How many roles were avilable for actresses in the 1950s?

# In[ ]:
len(cast[(cast.type != "actor") & (cast.year // 10 == 195)])

# ### How many leading roles (n=1) were available from the beginning of film history through 1980?

# In[ ]:
len(cast[(cast.n == 1) & (cast.year < 1981)])

# ### How many non-leading roles were available through from the beginning of film history through 1980?

# In[ ]:
len(cast[(cast.n != 1) & (cast.year <= 1980)])

# ### How many roles through 1980 were minor enough that they did not warrant a numeric "n" rank?

# In[ ]:
len(cast[(cast.n.isnull()) & (cast.year <= 1980)])