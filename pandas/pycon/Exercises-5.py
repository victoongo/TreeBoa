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
cast = pd.DataFrame.from_csv('data/cast.csv', index_col=None)
cast.head()

# In[4]:
release_dates = pd.DataFrame.from_csv('data/release_dates.csv', index_col=None,
                                      parse_dates=['date'], infer_datetime_format=True)
release_dates.head()

# ### Make a bar plot of the months in which movies with "Christmas" in their title tend to be released in the USA.

# In[ ]:
rd = release_dates
rd = rd[rd.title.str.contains('Christmas')]
rd = rd[rd.country == 'USA']
rd.date.dt.month.value_counts().sort_index().plot(kind = 'bar')

# ### Make a bar plot of the months in which movies whose titles start with "The Hobbit" are released in the USA.

# In[ ]:
rd = release_dates
rd = rd[rd.title.str.startswith('The Hobbit')]
rd = rd[rd.country == 'USA']
rd.date.dt.month.value_counts().sort_index().plot(kind = 'bar')

# ### Make a bar plot of the day of the week on which movies with "Romance" in their title tend to be released in the USA.

# In[ ]:
rd = release_dates
rd = rd[rd.title.str.contains('Romance')]
rd = rd[rd.country == 'USA']
rd.date.dt.dayofweek.value_counts().sort_index().plot(kind = 'bar')

# ### Make a bar plot of the day of the week on which movies with "Action" in their title tend to be released in the USA.

# In[ ]:
rd = release_dates
rd = rd[rd.title.str.contains('Action')]
rd = rd[rd.country == 'USA']
rd.date.dt.dayofweek.value_counts().sort_index().plot(kind = 'bar')

# ### On which date was each Judi Dench movie from the 1990s released in the USA?

# In[ ]:
rd = release_dates
rd = rd[(rd.country == 'USA') & (rd.year // 10 == 199)]

c = cast
c = c[c.name == "Judi Dench"]
c.merge(rd).sort('date')

# ### In which months do films with Judi Dench tend to be released in the USA?

# In[ ]:
rd = release_dates
rd = rd[rd.country == 'USA']

c = cast
c = c[c.name == "Judi Dench"]
c.merge(rd).date.dt.month.value_counts().sort_index().plot(kind = "bar")


# ### In which months do films with Tom Cruise tend to be released in the USA?

# In[ ]:

c = cast
c = c[c.name == "Tom Cruise"]
c.merge(rd).date.dt.month.value_counts().sort_index().plot(kind = "bar")