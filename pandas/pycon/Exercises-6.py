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
sales1 = pd.read_csv('data/sales1.csv')
sales1

# In[4]:
sales2 = pd.read_csv('data/sales2.csv')
sales2.fillna('')

# ### Challenge: first combine these sales together into a single dataframe, then compute how much money consumers spent on each book in each currency.

# In[ ]:
df1 = sales1.rename(columns = {
    "Book title": "title",
    "Number sold": 'number',
    "Sales price": 'price',
    "Royalty paid": 'paid'
})
df1['currency'] = 'USD'

s = sales2.copy()
t = s.Title
t = t.where(t.str.endswith(')')).str.split().str[-1].str.strip('()')
s['currency'] = t.fillna(method = 'bfill')
s = s[s['Units sold'].notnull()]
df2 = s.rename(columns = {
    "Title": 'title',
    "Units sold": 'number',
    "List price": 'price',
    "Royalty": 'paid'
})

#df = df1.merge(df2)
df = pd.concat([df1, df2])

df['total paid'] = df.number * df.price
df.groupby(['title', 'currency'])[['total paid']].sum()