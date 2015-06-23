
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


# ### What are the ten most common movie names of all time?

# In[ ]:




# In[ ]:




# ### Which three years of the 1930s saw the most films released?

# In[ ]:




# In[ ]:




# ### Plot the number of films that have been released each decade over the history of cinema.

# In[ ]:




# In[ ]:




# ### Plot the number of "Hamlet" films made each decade.

# In[ ]:




# In[ ]:




# ### Plot the number of "Rustler" characters in each decade of the history of film.

# In[ ]:




# In[ ]:




# ### Plot the number of "Batman" characters each decade.

# In[ ]:




# In[ ]:




# ### What are the 11 most common character names in movie history?

# In[ ]:




# In[ ]:




# ### Who are the 10 people most often credited as "Herself" in film history?

# In[ ]:




# In[ ]:




# ### Who are the 10 people most often credited as "Himself" in film history?

# In[ ]:




# In[ ]:




# ### Which actors or actresses appeared in the most movies in the year 1945?

# In[ ]:




# In[ ]:




# ### Which actors or actresses appeared in the most movies in the year 1985?

# In[ ]:




# In[ ]:




# ### Plot how many roles Mammootty has played in each year of his career.

# In[ ]:




# In[ ]:




# ### What are the 10 most frequent roles that start with the phrase "Patron in"?

# In[ ]:




# In[ ]:




# ### What are the 10 most frequent roles that start with the word "Science"?

# In[ ]:




# In[ ]:




# ### Plot the n-values of the roles that Judi Dench has played over her career.

# In[ ]:




# In[ ]:




# ### Plot the n-values of Cary Grant's roles through his career.

# In[ ]:




# In[ ]:




# ### Plot the n-value of the roles that Sidney Poitier has acted over the years.

# In[ ]:




# In[ ]:




# ### How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s?

# In[ ]:




# In[ ]:




# ### How many supporting (n=2) roles were available to actors, and how many to actresses, in the 1950s?

# In[ ]:




# In[ ]:



