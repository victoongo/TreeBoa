
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd


# In[2]:

from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[3]:

titles = pd.DataFrame.from_csv('data/titles.csv', index_col=None)
titles.head()


# In[4]:

cast = pd.DataFrame.from_csv('data/cast.csv', index_col=None)
cast.head()


# In[ ]:




# ### Using groupby(), plot the number of films that have been released each decade in the history of cinema.

# In[ ]:




# In[ ]:




# ### Use groupby() to plot the number of "Hamlet" films made each decade.

# In[ ]:




# In[ ]:




# ### How many leading (n=1) roles were available to actors, and how many to actresses, in each year of the 1950s?

# In[ ]:




# In[ ]:




# ### In the 1950s decade taken as a whole, how many total roles were available to actors, and how many to actresses, for each "n" number 1 through 5?

# In[ ]:




# In[ ]:




# ### Use groupby() to determine how many roles are listed for each of the Pink Panther movies.

# In[ ]:




# In[ ]:




# ### List, in order by year, each of the films in which Frank Oz has played more than 1 role.

# In[ ]:




# In[ ]:




# ### List each of the characters that Frank Oz has portrayed at least twice.

# In[ ]:




# In[ ]:



