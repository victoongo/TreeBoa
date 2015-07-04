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

# ### Using groupby(), plot the number of films that have been released each decade in the history of cinema.

# In[ ]:
titles.groupby(titles.year // 10 * 10).size().plot(kind = "bar")

# ### Use groupby() to plot the number of "Hamlet" films made each decade.

# In[ ]:
t = titles[titles.title == "Hamlet"]
t.groupby(t.year // 10 * 10).size().plot(kind = "bar")

# ### How many leading (n=1) roles were available to actors, and how many to actresses, in each year of the 1950s?

# In[ ]:
c = cast[(cast.n == 1) & (cast.year // 10 == 195)]
c.groupby(['year', 'type']).size().plot(kind = "bar")

# ### In the 1950s decade taken as a whole, how many total roles were available to actors, and how many to actresses, for each "n" number 1 through 5?

# In[ ]:
c = cast
c = c[(c.year // 10 == 195) & (c.n <= 5)]
c.groupby(['n', 'type']).size().plot(kind = 'bar')

# ### Use groupby() to determine how many roles are listed for each of the Pink Panther movies.

# In[ ]:
c = cast
c = c[c.title == "The Pink Panther"]
c.groupby('year').size()
c.groupby('year').n.max()

# ### List, in order by year, each of the films in which Frank Oz has played more than 1 role.

# In[ ]:
c = cast
c = c[c.name == 'Frank Oz']
fo = c.groupby(['year', 'title']).size() # put year before title in the groupby ensures sorting by year
fo[fo > 1]

# ### List each of the characters that Frank Oz has portrayed at least twice.

# In[ ]:
c = cast
c = c[c.name == 'Frank Oz']
fo = c.groupby(['character']).size() # put year before title in the groupby ensures sorting by year
fo[fo > 1].order() # order works on vectors of values, sort on data frames (var)