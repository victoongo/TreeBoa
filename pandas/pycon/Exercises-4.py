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

# ### Define a year as a "Superman year" whose films feature more Superman characters than Batman. How many years in film history have been Superman years?

# In[ ]:
c = cast
c= c[(c.character == "Superman") | (c.character == "Batman")]
g = c.groupby(['year', 'character']).size()
g = g.unstack().fillna(0)
len(g[g.Superman > g.Batman])

# ### How many years have been "Batman years", with more Batman characters than Superman characters?

# In[ ]:
len(g[g.Superman < g.Batman])

# ### Plot the number of actor roles each year and the number of actress roles each year over the history of film.

# In[ ]:
c = cast
c.groupby(['year', 'type']).size().unstack('type').plot()

# ### Plot the number of actor roles each year and the number of actress roles each year, but this time as a kind='area' plot.

# In[ ]:
c.groupby(['year', 'type']).size().unstack('type').plot(kind = 'area')

# ### Plot the difference between the number of actor roles each year and the number of actress roles each year over the history of film.

# In[ ]:
typ = c.groupby(['year', 'type']).size().unstack('type')
(typ.actor - typ.actress).plot(kind = 'area')

# ### Plot the fraction of roles that have been 'actor' roles each year in the hitsory of film.

# In[ ]:
(typ.actor / (typ.actor + typ.actress)).plot(kind = 'area')

# ### Plot the fraction of supporting (n=2) roles that have been 'actor' roles each year in the history of film.

# In[ ]:
c = cast[cast.n == 2]
typ = c.groupby(['year', 'type']).size().unstack('type')
(typ.actor / (typ.actor + typ.actress)).plot(kind = 'area')

# ### Build a plot with a line for each rank n=1 through n=3, where the line shows what fraction of that rank's roles were 'actor' roles for each year in the history of film.

# In[ ]:
c = cast[cast.n <= 3]
typ = c.groupby(['year', 'n', 'type']).size().unstack('type')
(typ.actor / (typ.actor + typ.actress)).unstack('n').plot(ylim = [0, 1])