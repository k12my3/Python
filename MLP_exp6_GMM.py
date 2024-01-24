import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

#Generate Synthetoc data for demo
n_samples = 1500
n_features = 2
n_components = 4

x, y_true  =make_blobs(n_samples=n_samples, n_features=n_features, centers = n_components, random_state=None)

#Create GMM
gmm = GaussianMixture(n_components=n_components, random_state=None)

#fit gmm to data
gmm.fit(x)

#get cluster assignments for each datapoint
labels = gmm.predict(x)

#plot datapoints w diff colors for each cluster
plt.figure(figsize=(8,6))
plt.scatter(x[:,0], x[:, 1], c=labels, cmap="viridis", s=50)
plt.title("GMM CLustering")
plt.show()