# joint Normal/Gaussian Probability density function (JPDF) of multiple CRVs co-occuring, ex :take 2

#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
random_seed=1000
 
# List containing the variance / values: 
var_x = 1
var_y = 1
cov_val = -0.4

#Let mean of the distribution be at (0,0)
mean = np.array([0,0])
cov = np.array([[var_x, cov_val], [cov_val, var_y]])
     
# Generating a Gaussian bivariate distribution with given mean and covariance matrix
distr = multivariate_normal(cov = cov, mean = mean, seed = random_seed)
sigma_1, sigma_2 = cov[0,0], cov[1,1]
     
x = np.linspace(-3*sigma_1, 3*sigma_1, num=30)
y = np.linspace(-3*sigma_2, 3*sigma_2, num=30)
X, Y = np.meshgrid(x,y)


Z_pdf = np.zeros(X.shape)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
      Z_pdf[i,j] = distr.pdf([X[i,j], Y[i,j]])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z_pdf, color='black')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title('Covariance between x1 and x2 = {val}')
plt.show()

fig = plt.figure()
plt.contourf(X, Y, Z_pdf, cmap='viridis')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title('Covariance between x1 and x2')
plt.tight_layout()
plt.show()


# %%
