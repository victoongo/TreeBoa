
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


# ### What are the ten most common movie names of all time?

# In[ ]:
titles.title.value_counts().head(10)

# ### Which three years of the 1930s saw the most films released?

# In[ ]:
titles.year[titles.year // 10 == 193].value_counts().head(3)

# ### Plot the number of films that have been released each decade over the history of cinema.

# In[ ]:
films_by_decade = (titles.year // 10 * 10).value_counts().sort_index()
films_by_decade.plot(kind = "bar")

# ### Plot the number of "Hamlet" films made each decade.

# In[ ]:
(titles.year[titles.title == "Hamlet"] // 10 * 10).value_counts().sort_index().plot(kind = "bar")

# ### Plot the number of "Rustler" characters in each decade of the history of film.

# In[ ]:
(cast.year[cast.character == "Rustler"] // 10 * 10).value_counts().sort_index().plot(kind = "bar")

# ### Plot the number of "Batman" characters each decade.

# In[ ]:
(cast.year[cast.title == "Batman"] // 10 * 10).value_counts().sort_index().plot(kind = "bar")

# ### What are the 11 most common character names in movie history?

# In[ ]:
cast.character.value_counts().head(11)

# ### Who are the 10 people most often credited as "Herself" in film history?

# In[ ]:
cast.name[cast.character == "Herself"].value_counts().head(10)

# ### Who are the 10 people most often credited as "Himself" in film history?

# In[ ]:
cast.name[cast.character == "Himself"].value_counts().head(10)

# ### Which actors or actresses appeared in the most movies in the year 1945?

# In[ ]:
cast.name[cast.year == 1945].value_counts().head(1)

# ### Which actors or actresses appeared in the most movies in the year 1985?

# In[ ]:
cast.name[cast.year == 1985].value_counts().head(1)

# ### Plot how many roles Mammootty has played in each year of his career.

# In[ ]:
cast.year[cast.name == "Mammootty"].value_counts().sort_index().plot(kind = "bar")

# ### What are the 10 most frequent roles that start with the phrase "Patron in"?

# In[ ]:
cast.character[cast.character.str.startswith('Patron in')].value_counts().head(10)

# ### What are the 10 most frequent roles that start with the word "Science"?

# In[ ]:
cast.character[cast.character.str.startswith('Science')].value_counts().head(10)

# ### Plot the n-values of the roles that Judi Dench has played over her career.

# In[ ]:
cast.n[cast.name == "Judi Dench"].value_counts().sort_index().plot(kind = "bar")
cast[(cast.name == "Judi Dench") & (cast.n.notnull())].sort('year').plot(x = 'year', y = 'n', kind = "scatter")

# ### Plot the n-values of Cary Grant's roles through his career.

# In[ ]:
cast[(cast.name == "Cary Grant") & (cast.n.notnull())].sort('year').plot(x = 'year', y = 'n', kind = "scatter")

# ### Plot the n-value of the roles that Sidney Poitier has acted over the years.

# In[ ]:
cast[(cast.name == "Sidney Poitier") & (cast.n.notnull())].sort('year').plot(x = 'year', y = 'n', kind = "scatter")

# ### How many leading (n=1) roles were available to actors, and how many to actresses, in the 1950s?

# In[ ]:
cast.type[(cast.year // 10 == 195) & (cast.n == 1)].value_counts()

# ### How many supporting (n=2) roles were available to actors, and how many to actresses, in the 1950s?

# In[ ]:
cast.type[(cast.year // 10 == 195) & (cast.n == 2)].value_counts()