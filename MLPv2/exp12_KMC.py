import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#Generate random data points using scikit learn's make blobs
n_samples = 1500
n_features = 4
n_clusters = 3
random_state = 30
x,y = make_blobs(n_samples = n_samples, n_features = n_features, centers = n_clusters, random_state=random_state)

#Apply KMC
kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=25)
y_kmeans = kmeans.fit_predict(x)

#Extract Cluster centers and labels
centers = kmeans.cluster_centers_
labels = np.unique(y_kmeans)

#Plot Datapoints and Cluster Centers
plt.figure(figsize=(8,6))
for i in range(n_clusters):
    plt.scatter(x[y_kmeans==i,0], x[y_kmeans==i,1], label = f'Cluster{i+1}')
plt.scatter(centers[:, 0], centers[:, 1], s=200, c="red", marker='X', label = "Cluster Centers")
plt.xlabel("Feature - 1")
plt.ylabel("Feature - 2")
plt.title("K-Means Clustering")
plt.legend()
plt.show()

#Example - 1:
n_samples = 1000
n_features = 2
n_clusters = 5
random_state = 40

# Example – 2:
# n_samples = 1000
# n_features = 2
# n_clusters = 2
# random_state = 40

# Example – 3:
# n_samples = 1500
# n_features = 4
# n_clusters = 3
# random_state = 30