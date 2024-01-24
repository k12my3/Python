import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

n_samples = 1500
n_features = 2
n_clusters = 3
random_state = 40
x, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=random_state)

kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=25)
ykmeans = kmeans.fit_predict(x)

centers = kmeans.cluster_centers_
labels = np.unique(ykmeans)

plt.figure(figsize=(8,6))
for i in range(n_clusters):
    plt.scatter(x[ykmeans==i,0], x[ykmeans==i,1], label = f'Cluster{i+1}')
plt.scatter(centers[:, 0], centers[:, 1], s=200, c="red",marker="X", label = "Cluster Centers")

plt.xlabel("Feature-1")
plt.ylabel("Feature-2")
plt.title("K-Means Clustering")
plt.legend()
plt.show()
