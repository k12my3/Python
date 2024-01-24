#Find sum of 2 arrays:
import numpy as np
a = np.array([1,3,5])
b = np.array([2,4,6])
print(f'Sum of arrays-a,b: {a+b}')

#Find Square root of number in array:
a = np.array([1,4,9])
print("Square root of no. in array = ", np.sqrt(a));

#Find Random Values
x = np.random.rand(6,7)
print("\n-----\n\nRandom Numbers:\n", x)

#Find random int values
c = np.random.randint(2, size=10)
print("\n-----\n\nRandom Int-values: ", c)

# Sci-Py -----------------------
# Finding Eigen Values and Vectors
from scipy import linalg
import matplotlib.pyplot as plt
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

# Pandas -----------------------
import pandas as pd
arrays = [[1,2,3],["xyz", "abc", "pqr"]]
mi = pd.MultiIndex.from_arrays(arrays, names = ("ids", "student"))
print("\n-----\n\nThe MultiIndex:\n", mi)
print("Names of levels in Multi-Index:\n", mi.names)

#multiindex-ex.2
cities = [["Punjab", "Hyderaba", "Bombay", "Kerala"], ["Melbourne", "Zurich", "Chicago", "Berlin"]]
mi = pd.MultiIndex.from_arrays(cities, names=("india_cities", "usa_cities"))
print("\n\nMultiIndex - 2:\n", mi)
print("Levels in Multi-Index-2:\n", mi.levels)
print("Names of levels in Multi-Index-2:\n", mi.names)

#Multi-index-ex.3
employees = [["E101", "E102", "E103", "E104"], ["emp1", "emp2", "emp3", "emp4"]]
mi = pd.MultiIndex.from_arrays(employees, names = ("emp_ids", "names"))
print("\n\nMultiIndex - 3:\n", mi)
print()
print("Levels in Multi-Index-3:\n", mi.levels)
print()
new_levels = [["E1", "E2", "E3", "E4"],
              ["abc", "pqr", "xyz", "def"]]
newmi = mi.set_levels(new_levels)
print("Setting new levels:\n", newmi)
print("Updated names of levels in Multi-Index-3:\n", mi.names)