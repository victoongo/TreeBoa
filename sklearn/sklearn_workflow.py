
# coding: utf-8

# ## A Beginner's Guide to Machine Learning in Scikit-Learn
# 
# This is the IPython notebook that directly accompanies the "A Beginner's Guide to Machine Learning with Scikit-Learn" talk I gave at PyData NYC 2013 and will  be giving at PyTennessee 2014. The slides can be found at http://www.slideshare.net/SarahGuido/a-beginners-guide-to-machine-learning-with-scikitlearn. 
# 
# This notebook contains the full machine learning workflow I cover in my talk, starting with data preprocessing, moving into supervised and unsupervised learning, and finishing with testing and validation. I don't cover the topics linearly in my talk, because my main goal of the talk is to introduce you to important machine learning concepts and give you a taste of what scikit-learn can do, but here they are in a linear process.
# 
# My first step, not shown here, is to save the data in one file and the labels in another. This was the simplest way I could find, for the purposes of this talk.
# 
# Next is to read it in.

# In[2]:

get_ipython().magic(u'pylab inline')
import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

car_data = list(csv.DictReader(open('git repos/skl-talk/data/cardata.csv', 'rU')))
car_target = open('git repos/skl-talk/data/cartarget.csv', 'rU').read().splitlines()

print 'Data instance:', car_data[10]
print 'Label:', car_target[10]


# Next is to vectorize and encode my categorical variables, as discessed in the data preprocessing notebook.

# In[3]:

vec = DictVectorizer()
car_data = vec.fit_transform(car_data).toarray()

print 'Vectorized:', car_data[10]
print 'Unvectorized:', vec.inverse_transform(car_data[10])


# I also have to encode the labels, since they're currently in text form. You can get the original label using the inverse_transform() function.

# In[4]:

le = preprocessing.LabelEncoder()
le.fit(["unacc", "acc", "good", "vgood"])
target = le.transform(car_target)

print 'Transformed:', target[10] 
print 'Inverse transformed:', le.inverse_transform(target[10])


# After prepping the data and labels by encoding them, it's time to split up the dataset using train_test_split(), to avoid overfitting later on.

# In[5]:

car_data_train, car_data_test, target_train, target_test = train_test_split(car_data, target)

print 'Training set:', len(car_data_train)
print 'Test set:', len(car_data_test)


# It's now time to build our classifier! Using the Naive Bayes classifier is easy (if you want to learn more about it, check out the supervised learning notebook).

# In[6]:

nb_estimator = GaussianNB()
nb_estimator.fit(car_data_train, target_train)
pred = nb_estimator.predict(car_data_test)

print 'Predicted labels:', pred[0:8]
print 'Actual labels:', target_test[0:8]

print 'Predicted labels inverse:', list(le.inverse_transform(pred[0:8]))
print 'Actual labels inverse:', list(le.inverse_transform(target_test[0:8]))


# So our classifier was sort of accurate, but got a few labels wrong. Let's take a look at how accurate the classifier actually is using come testing and validation measures.

# In[7]:

print 'Score:', nb_estimator.score(car_data_test, target_test)

print 'Cross validation scoring:', cross_validation.cross_val_score(nb_estimator, 
                                                                    car_data_test, 
                                                                    target_test, cv=4)


# Let's pretend we don't have labels for this dataset. Is there anything we can learn by clustering? 
# 
# Also, and I don't cover this is my talk due to time limits, I'm reducing the dimensionality of my dataset here for the sake of simplicity. Again, you can find descriptions of clustering and dimensionality reduction in the unsupervised learning notebook.

# In[23]:

pca = PCA(n_components=2)
X_test_r = pca.fit(car_data_test).transform(car_data_test)

kmeans = KMeans(n_clusters=10)
kmeans.fit(X_test_r)
centroids = kmeans.cluster_centers_
target_names = le.classes_

plt.figure()
for c, i, target_name in zip(['b', 'r', 'g', 'c'],
                             [0, 1, 2, 3], target_names):
    plt.plot(X_test_r[target_test == i, 0], X_test_r[target_test == i, 1], 'o', 
             c=c, markeredgecolor='k', markersize=8, label=target_name)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=300, linewidths=5, 
                color='chartreuse', zorder=10)

plt.legend()
plt.show()


# This is particularly interesting because while the car evaluation dataset has 4 labels, it appears that there are 10 significant clusters in the dataset! 
