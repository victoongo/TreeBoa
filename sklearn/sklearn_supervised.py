
# coding: utf-8

# In[9]:

get_ipython().magic(u'pylab inline')


# ## Supervised Learning in Scikit-Learn
# 
# Supervised learning is the task of learning from labeled data. Using a set of labeled data, called training data, you can train supervised algorithms to infer the relationship between each data instance and its label. That relationship can then be mapped to new data, in order to predict patterns or categories. For example, if you have a dataset with observations about email spam, each instance might have a label of "spam" or "not spam", or something like a 1 for spam and a 0 for not spam. Or, as another example, you might want to predict the relationship between housing prices and square footage based off of data where that relationship is already apparent.
# 
# The two main types of supervised learning are classification and regression.
# 
# ### Classification
# 
# Classification algorithms predict categorical labels, like our email spam example, and can tell us the likelihood that a new data instance belongs to a certain category. The categories can be discrete, nominal, ordinal, integer-valued, or real-valued. Our much-loved email spam example is an example of classification. 
# 
# #### Naive Bayes Classification
# 
# In Naive Bayes classification, the classifier assumes that the features in your dataset are independent of each other; that is, one feature being a certain way has no effect on what values the other features take. This is a naive assumption because this doesn't always hold true in reality, but despite this naivety and oversimplified assumptions, the classifier performs decently and even quite well in certain classification situations.
# 
# In scikit-learn, the Naive Bayes classifier is fast. However, some of the more sophisticated methods we'll discuss have been shown to perform better. Scikit-learn comes with several different variations on the Naive Bayes classifer, like Gaussian Naive Bayes, which is what I'll show in the example.
# 
# To build the classifier, first create the model by setting a variable equal to the Naive Bayes object. The GaussianNB() estimator assumes a normal distribution. Then, fit the model to the training dataset and the training labels. Finally, predict on a new set of data.

# In[3]:

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB

digits = datasets.load_digits()

train_X, test_X, train_y, test_y = train_test_split(digits.data, digits.target, test_size=0.33)

nb_estimator = GaussianNB()
nb_estimator.fit(train_X, train_y)
pred = nb_estimator.predict(test_X)


# Comparing the first 8 predicted labels to what the first 8 labels actually are:

# In[12]:

print 'Predicted labels:', pred[0:8]
print 'Actual labels:', test_y[0:8]


# ### Regression
# 
# Regression is used to predict continuous target variables, like the relationship between housing prices and square footage. In a regression model, we look at how the value of a dependent variable changes when the other independent variables change. 
# 
# #### Linear Regression
# 
# Linear regression is used when the target value is expected to be a linear combination of the input variables. The goal of linear regression, in creating a linear model, is to minimize the sum of squared residuals between the observed data and the responses predicted by linear approximation. 
# 
# Linear regression models make a few assumptions about the dataset you're using to train them. Feature independence, similar to that in the Naive Bayes algorithm, is assumed, as is linearity, which means that the target value is a linear combination of the parameters and the predictor variables. 
# 
# Here's linear regression used on housing prices.

# In[18]:

from sklearn import linear_model
import matplotlib.pyplot as plt

houses = datasets.load_boston()
# Use only one feature
houses_X = houses.data[:, np.newaxis]
houses_X_temp = houses_X[:, :, 2]

X_train, X_test, y_train, y_test = train_test_split(houses_X_temp, houses.target, test_size=0.33)

lreg = linear_model.LinearRegression()
lreg.fit(X_train, y_train)

plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, lreg.predict(X_test), color='green', linewidth=3)

plt.show()

