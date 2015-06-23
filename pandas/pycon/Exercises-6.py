
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd


# In[2]:

from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))


# In[3]:

sales1 = pd.read_csv('sales1.csv')
sales1


# In[4]:

sales2 = pd.read_csv('sales2.csv')
sales2.fillna('')


# ### Challenge: first combine these sales together into a single dataframe, then compute how much money consumers spent on each book in each currency.

# In[ ]:




# In[ ]:



