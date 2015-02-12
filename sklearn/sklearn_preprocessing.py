
# coding: utf-8

# ## Data Preprocessing in Scikit-Learn
# 
# The first step to any data analysis workflow is getting your data into a usable format. The estimators in scikit-learn have very specific requirements for what they'll take in. This notebook will cover different ways of preprocessing your data into a more scikit-learn-friendly format.
# 
# ### Getting Data into Scikit-Learn
# 
# One of the great things about scikit-learn is that it comes with several toy datasets. If all you want to is play around with certain algorithms, these built-in datasets are a good way to do that. Here's an example of the classic iris dataset.

# In[4]:

from sklearn import datasets

iris = datasets.load_iris()
print iris.data[0:10]


# Scikit-learn also comes with the handwritten digits dataset, the diabetes dataset, a house prices dataset, and sample images.
# 
# A really important thing to know is that scikit-learn estimators **only take in continuous data in the form of NumPy arrays**. If your data is already continuous, this isn't a problem. There's a function in NumPy called loadtxt() that can read in a CSV file and convert it to an array with ease. For example, here's both the first five data instances and their labels from the glass identification dataset.

# In[8]:

from sklearn import preprocessing
import numpy as np

glass_data = np.loadtxt('../data/glass_data.csv', delimiter=',')
glass_target = np.loadtxt('../data/glass_target.csv')
print glass_data[0:5], glass_target[0:5]


# And you're ready to go. However, with categorical data, it's a bit more complicated.
# 
# In my presentation and in the sklearn_workflow notebook, I use the car evaluation dataset from the UCI machine learning repository. This is a great dataset to work with because it's simple and is great for classification, but all of the values in the dataset are categorical. This means that I have to transform these categorical values into continuous ones.
# 
# One of the easiest ways I've found for importing categorical data is to read in a file from a csv and put it into a list of dictionaries, which can easily be encoded into 1s and 0s in scikit-learn. For the target variables, that simply gets read into a list and is then encoded.

# In[1]:

import csv

car_data = list(csv.DictReader(open('../data/cardata.csv', 'rU')))
car_target = list(csv.reader(open('../data/cartarget.csv', 'rU')))


# Here's what the first dictionary in the list looks like:

# In[2]:

car_data[10]


# The first step in vectorizing our categorical values is to create a DictVectorizer() object and then use fit_transform() and toarray() to get the values into a NumPy array.

# In[3]:

from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer()
car_data = vec.fit_transform(car_data).toarray()


# Here's a vectorized item and the unencoded item beneath.

# In[4]:

print 'Vectorized:', car_data[10]
print 'Unvectorized:', vec.inverse_transform(car_data[10])


# Because the labels are also categorical, those need to be transformed as well. There's a special LabelEncoder() object specifically for this task.

# In[5]:

from sklearn import preprocessing

le = preprocessing.LabelEncoder()
le.fit(["unacc", "acc", "good", "vgood"])
target = le.transform(car_target[0])


# Here's the transformed label and what it means.

# In[6]:

print 'Transformed:', target[10] 
print 'Inverse transformed:', le.inverse_transform(target[10])


# ### Splitting Up the Dataset
# 
# Another preprocessing step is to split up the dataset, in order to avoid overfitting. The train_test_split() function is a really simple way to do that. By default, the size of the test set is 25%.

# In[7]:

from sklearn.cross_validation import train_test_split

car_data_train, car_data_test, target_train, target_test = train_test_split(car_data, target)


# The length of the whole data set is 1728 instances. After train_test_split():

# In[8]:

print 'Training set:', len(car_data_train)
print 'Test set:', len(car_data_test)

