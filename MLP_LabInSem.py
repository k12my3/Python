import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

n_samples = 1500
n_features = 2
n_clusters = 5
random_state = 40
x,y = make_blobs(n_samples = n_samples, n_features = n_features, centers = n_clusters, random_state=random_state)

kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=25)
y_kmeans = kmeans.fit_predict(x)

centers = kmeans.cluster_centers_
labels = np.unique(y_kmeans)

plt.figure(figsize=(8,6))
for i in range(n_clusters):
    plt.scatter(x[y_kmeans==i,0], x[y_kmeans==i,1], label = f'Cluster{i+1}')
plt.scatter(centers[:,0], centers[:,1], c="red", s=200, marker='X', label = "Cluster Centers")
plt.xlabel("Feature-1")
plt.ylabel("Feature-2")
plt.legend()
plt.show()