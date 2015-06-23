
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd


# In[2]:

from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[3]:

cast = pd.DataFrame.from_csv('data/cast.csv', index_col=None)
cast.head()


# In[4]:

release_dates = pd.DataFrame.from_csv('data/release_dates.csv', index_col=None,
                                      parse_dates=['date'], infer_datetime_format=True)
release_dates.head()


# In[ ]:




# ### Make a bar plot of the months in which movies with "Christmas" in their title tend to be released in the USA.

# In[ ]:




# In[ ]:




# ### Make a bar plot of the months in which movies whose titles start with "The Hobbit" are released in the USA.

# In[ ]:




# In[ ]:




# ### Make a bar plot of the day of the week on which movies with "Romance" in their title tend to be released in the USA.

# In[ ]:




# In[ ]:




# ### Make a bar plot of the day of the week on which movies with "Action" in their title tend to be released in the USA.

# In[ ]:




# In[ ]:




# ### On which date was each Judi Dench movie from the 1990s released in the USA?

# In[ ]:




# In[ ]:




# ### In which months do films with Judi Dench tend to be released in the USA?

# In[ ]:




# In[ ]:




# ### In which months do films with Tom Cruise tend to be released in the USA?

# In[ ]:




# In[ ]:



