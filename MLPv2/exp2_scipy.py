# Sci-Py -----------------------
# Finding Eigen Values and Vectors
from scipy import linalg
import matplotlib.pyplot as plt
import numpy as np

e = np.array([[1,2], [2,1]])
egvalues, egvector = linalg.eig(e)
print("\n-----\n\nEigen-values: ", egvalues, "\nEigen-vectors: ", egvector)

#Find Inverse(a)
a = np.array([[1,2,3], [4,5,6],[1,5,1]])
print("Inverse of array-a = ", np.linalg.inv(a))

#Interpolate fucntion in SciPy
from scipy import interpolate
x = np.arange(0,20)
y = x**2
temp = interpolate.interp1d(x,y)
xnew  = np.arange(0,9,0.2)
ynew = temp(xnew)
plt.title("Interpolation")
plt.plot(x,y,'*', xnew, ynew, '-', color="green")
plt.show()

from scipy.stats import normaltest
v = np.random.normal(size=100)
print("Normal Test output: ", normaltest(v))

from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print("Hamming distance between given plots: ", res)