
# coding: utf-8

# In[2]:

get_ipython().magic(u'pylab inline')


# ## Unsupervised Learning in Scikit-Learn
# 
# Unsupervised learning is used when the data is unlabeled. With unsupervised learning, it's possible to pull out patterns and relationships within the data without knowing what's there. Unsupervised learning is an exploratory kind of learning, and it's good for trying to find hidden structure and correlation in the data. 
# 
# The two main types of unsupervised learning are clustering and dimensionality reduction. 
# 
# ### Clustering
# 
# Clustering, as you can probably infer from the name, clusters similar data instances into groups. The main purpose of clustering is to determine what relationships might exist. Clustering algorithms group data together in a way such that data within the same group are more similar to each other than to those in other groups. 
# 
# #### K-means clustering
# 
# K-means clustering is one of the simplest types of clustering. This algorithm alternates between two steps: assigning each data point to the centroid (or cluster) it is most similar to, and then updating the cluster center by calculating the mean of the data points within the cluster. The algorithm is finished when the assignment of instances to clusters no longer changes. 
# 
# The K-means clustering algorithm in scikit-learn allows you to choose how many cluster centers to pick, which can deliver poor results if you pick the wrong number of clusters. There are several methods for determining the number of clusters to choose, which is beyond the scope of this talk, but more information can be found *here* (link).
# 
# Before I give an example of K-means clustering, I'm going to explain dimensionality reduction, and how it's useful in conjunction with clustering.
# 
# ### Dimensionality reduction
# 
# Dimensionality reduction is the process of reducing the number of random variables and the number of dimensions in your data. For example, you might have a dataset with hundreds of features. It's likely that not all of these features will be useful for your analysis, so dimensionality reduction can help to pull out the features that are important to finding patterns in the data and to reduce the number of dimensions. 
# 
# #### Principal component analysis
# 
# Principal component analysis (PCA) is a method that reduces the number of features, or dimensions, of a dataset by transforming it into a set of linearly uncorrelated variables, referred to as principal components. The number of principal components is less than or equal to the number of original values. PCA is useful for processing high-dimensional datasets into something easier to work with, while still retaining as much of the variance in the dataset as possible.
# 
# There are a lot of dimensions in the digits dataset, so here we use PCA to shrink the number of dimensions before clustering the instances. The plot shows a scatterplot of the instances with the cluster centers overlaid.

# In[13]:

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

digits = load_digits()

X = digits.data
y = digits.target
target_names = digits.target_names

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

kmeans = KMeans(n_clusters=9)
kmeans.fit(X_r)
centroids = kmeans.cluster_centers_

plt.figure()
for c, i, target_name in zip(['b', 'r', 'g', 'c', 'm', 'y', 'k', 'burlywood',
                              'chartreuse', '0.75'],
                             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], target_names):
    plt.plot(X_r[y == i, 0], X_r[y == i, 1], 'k.', c=c, markersize=3, label=target_name)
    plt.scatter(centroids[:, 0], centroids[:, 1])
plt.legend()
plt.show()


# In[ ]:



