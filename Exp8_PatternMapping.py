
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression

# data / samples generation:
Xo_1 = np.linspace(-3, 1, num=50)
Xo_2 = np.linspace(-1, 3, num=50)

Xo_k1, Xo_k2 = np.meshgrid(Xo_1, Xo_2)

xxo1 = Xo_k1.ravel()
xxo2 = Xo_k2.ravel()

yo = np.cos((xxo1**2)/4 + (xxo2**2)/2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xxo2, xxo1, yo, color='black')
plt.show() # original data plot

#----------------------------------------------------------------------
# Generating input data to ANNs (datapoints: 100):
X_1 = np.linspace(-3, 1, num=25) ### generation of samples
X_2 = np.linspace(-1, 3, num=25) ### generation of samples

X_k1, X_k2 = np.meshgrid(X_1, X_2)

xx1 = X_k1.ravel()
xx2 = X_k2.ravel()

y = np.cos((xx1**2)/4 + (xx2**2)/2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xx2, xx1, y, color='black')
plt.show()   #original data plot


#------------------------------------------------------------------------
# Developing ANNs which approximate the original function using these 100 points
X = np.vstack([xx1, xx2]).T
print(np.shape(X))
Y = y.T
regr = MLPRegressor(hidden_layer_sizes=(20,15), activation = 'tanh', random_state=1, max_iter=5000).fit(X, Y)
# yc = regr.predict(X_test)
# print(yc)

############# Plotting for new points
Xt_1 = np.linspace(-3, 1, num=50) ### generation of samples
Xt_2 = np.linspace(-1, 3, num=50) ### generation of samples

Xt_k1, Xt_k2 = np.meshgrid(Xt_1, Xt_2)
xxt1 = Xt_k1.ravel()
xxt2 = Xt_k2.ravel()
X_test = np.vstack([xxt1, xxt2]).T
yc = regr.predict(X_test)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xxt2, xxt1, yc, color='black')
plt.show()