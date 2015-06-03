
# coding: utf-8

# ## Choose Pandas!
# #### PyCon 2014 Lightning Talk

# In[1]:

get_ipython().magic(u'pylab inline')
import pandas as pd

cd "~/Dropbox/Projects/TreeBoa/pandas/data"
car_eval = pd.read_csv('car_data.txt')
car_eval.head()


# In[2]:

pivoted_car = car_eval.pivot_table(values='doors', 
                                   rows='lug_boot', 
                                   cols='class', 
                                   aggfunc='mean')
pivoted_car


# In[3]:

class_counts = car_eval['class'].value_counts()
class_counts.plot(kind='bar', rot=0)

