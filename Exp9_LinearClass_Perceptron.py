import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Perceptron_single_neuron(x1,x2,y,W):
  N = len(x1)
  for i in list(range(N)):
    v = W[0]+ W[1]*x1[i] + W[2]*x2[i]
    f_v = 1./(1+np.exp(-v))
    W[0] = W[0] + 0.000005*(y[i]-f_v)*1
    W[1] = W[1] + 0.000005*(y[i]-f_v)*x1[i]
    W[2] = W[2] + 0.000005*(y[i]-f_v)*x2[i]

  # Computation of error of an iteration
  error_E = 0
  for i in list(range(N)):
    v = W[0] + W[1]*x1[i] + W[2]*x2[i]
    error_E = error_E + (y[i]-f_v)**2
  ### Total error of an iteration
  error_E = error_E/N
  return error_E, W


# Reading the excel sheet
df1 = pd.read_excel(r'SampleData/Book1.xlsx')
print('df1 = ', df1)
print(type(df1))

y = list(df1[:]['Y'])
print('y =', y)
x1 = list(df1[:]['X1'])
print('x1 =', x1)
x2 = list(df1[:]['X2'])
print('x2 =', x2)

# Randomly initialize the weight based on the dimensionality of input point
L = 2;
import random
# seed random number generator
#random.seed(1)
W0 = random.random()
W1 = random.random()
W2 = random.random()
W = [W0, W1, W2]

'''
# modeling a multiple linear regression 
Error_v = []
for i in list(range(100)):
  E, W = MLR_single_neuron(x1,x2,y,W)
  Error_v.append(E)
'''

# iteratively modifying the weights
i = 1
E_t = 0
Error_v = []
iteration = 0
error_diff = 1000
while iteration < 10000:
 E, W = Perceptron_single_neuron(x1,x2,y,W)
 error_diff = abs(E_t-E)
 Error_v.append(E)
 E_t = E
 iteration = iteration + 1
 #print(i) 


# Plotting error for each iteration
plt.plot(Error_v)
plt.show


# plotting
W = np.array(W)
# plotting the function f(x1,x2) = W0 + W1X1 + W2X2 
X_1 = np.linspace(0, 15, num=100) ### generation of samples
X_2 = []
for ii in X_1:
 element = -(W[0]+W[1]*ii)/W[2]
 X_2.append(element)


indx_class_1 = [i for i, n in enumerate(y) if n == 1]
indx_class_2 = [i for i, n in enumerate(y) if n == 0]

from operator import itemgetter
fig = plt.figure()
######### plotting original points
plt.scatter(list((itemgetter(*indx_class_1)(x1))),list((itemgetter(*indx_class_1)(x2))));
plt.scatter(list((itemgetter(*indx_class_2)(x1))),list((itemgetter(*indx_class_2)(x2))));

plt.plot(X_1,X_2)
plt.show()