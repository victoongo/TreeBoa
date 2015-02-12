
# coding: utf-8

# ## Testing and Validation in Scikit-Learn
# 
# Once you have your estimator and you've made your predictions, it's useful to know how accurate your model is and what you can expect from it. Scikit-learn has a few different methods for doing this.
# 
# The score() function comes with each estimator, and it calculates how many labels the model got right, or how accurate the prediction is. Going back to our Naive Bayes example from the supervised learning notebook:

# In[2]:

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB

digits = datasets.load_digits()

train_X, test_X, train_y, test_y = train_test_split(digits.data, digits.target, test_size=0.33)

nb_estimator = GaussianNB()
nb_estimator.fit(train_X, train_y)
nb_estimator.score(test_X, test_y)


# This means that our model accurately predicted labels around 80% of the time. It's a decent result, but not great.
# 
# Another method for testing the accuracy of the estimator is cross-validation, which splits up the dataset randomly and computes the score of the model several times, by comparing predicted labels to the actual labels. You can choose how many times to split up and test your model; I've chosen 6 below. As you can see, the accuracy score works out to be around 80% again.

# In[4]:

from sklearn import cross_validation

cross_validation.cross_val_score(nb_estimator, test_X, test_y, cv=6)

