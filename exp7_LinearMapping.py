import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def MLR_single_neuron(x1,x2,y,W):
  N = len(x1)
  for i in list(range(N)):
    v = W[0]+ W[1]*x1[i] + W[2]*x2[i]
    W[0] = W[0] + 0.00001*(y[i]-v)*1
    W[1] = W[1] + 0.00001*(y[i]-v)*x1[i]
    W[2] = W[2] + 0.00001*(y[i]-v)*x2[i]
  
  # Computation of error of an iteration
  error_E = 0
  for i in list(range(N)):
    v = W[0] + W[1]*x1[i] + W[2]*x2[i]
    error_E = error_E + (y[i]-v)**2
  ### Total error of an iteration
  error_E = error_E/N
  return error_E, W

df1 = pd.read_excel(r'SampleData\Multiple_LR.xlsx') #Reading excel sheet //data
print('df1 = ', df1)
print(type(df1))

y = list(df1[:]['sales']) #output data
print('y =', y)

# input attributes :
x1 = list(df1[:]['cost'])
print('x1 =', x1)
x2 = list(df1[:]['time'])
print('x2 =', x2)

# Randomly initialize weight based on the dimensionality of input point
L = 2;
import random
# seed random number generator -> random.seed(1)
W0 = random.random()
W1 = random.random()
W2 = random.random()
W = [W0, W1, W2]

'''
#modeling a multiple linear regression 
Error_v = []
for i in list(range(100)):
  E, W = MLR_single_neuron(x1,x2,y,W)
  Error_v.append(E)
'''

#iteratively modifying the weights
i = 1
E_t = 0
Error_v = []
iteration = 0
error_diff = 1000
while iteration < 1000000:
 E, W = MLR_single_neuron(x1,x2,y,W)
 error_diff = abs(E_t-E)
 Error_v.append(E)
 E_t = E
 iteration = iteration + 1
 #print(i) 

plt.plot(Error_v) #Plotting error for each iteration
plt.show


#test case
xp1 = 500 # cost
xp2 = 12  # time of delivery
sales = W[0] + W[1]*xp1 + W[2]*xp2
print(sales)



##plotting f(x1,x2) = W0 + W1X1 + W2X2 
X_1 = np.linspace(68, 175, num=50) # generating samples
X_2 = np.linspace(4, 23, num=50) # generating samples

X_k1, X_k2 = np.meshgrid(X_1, X_2)

W = np.array(W)
Z = W[0] + W[1]*X_k1 + W[2]*X_k2

# plotting original points
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x1,x2,y, cmap='viridis', linewidth=1.5);
#plt.show()

# plotting relation
ax.plot_wireframe(X_k1, X_k2, Z, color='black')
ax.set_title('wireframe');
plt.show()