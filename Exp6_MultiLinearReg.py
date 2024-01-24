import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Multiple_linear_regression_1(x1,x2,y):
 y = np.array(y)
 x1 = np.array(x1)
 x1 = np.matrix(x1)
 x1 = x1.transpose()
 x2 = np.array(x2)
 x2 = np.matrix(x2)
 x2 = x2.transpose()
 on1 = np.ones(len(x1))
 on1 = np.matrix(on1)
 on1 = on1.transpose()
 X = np.hstack((on1,x1,x2))  ## Appending the column matrices tp form the matrix
 Y = np.matrix(y)
 Y = Y.transpose()
 XT = X.transpose()
 alpha = XT*X
 beta = XT*Y
 W = np.linalg.inv(alpha)*beta
 return W

## reading the excel sheet
df1 = pd.read_excel(r'SampleData/Multiple_LR.xlsx')
print("\n\ndf1:\n", df1)
print("df1 type: ", type(df1))

# output attribute
y = list(df1[:]['sales'])
print("\n\ny:\n", y)

# input attributes
x1 = list(df1[:]['cost'])
print("\nx1:\n", x1)

x2 = list(df1[:]['time'])
print("\nx2:\n", x2)
 
W = Multiple_linear_regression_1(x1,x2,y) # Modelling multiple LR

#Getting value for the unknown sample
x_unknown = [80, 20]
pred_x_unknown_sales = W[0] + W[1]*x_unknown[0] + W[2]*x_unknown[1]
print("\n\nPredict unknown sales:\n", pred_x_unknown_sales)

#### plotting the function f(x1,x2) = W0 + W1X1 + W2X2 
X_1 = np.linspace(68, 175, num=50) ### generation of samples
X_2 = np.linspace(4, 23, num=50) ### generation of samples

X_k1, X_k2 = np.meshgrid(X_1, X_2)

W = np.array(W)
Z = W[0] + W[1]*X_k1 + W[2]*X_k2

######### plotting original points
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter(x1,x2,y, cmap="viridis", linewidth=1.5);
#plt.show()
##### plotting the relation
ax.plot_wireframe(X_k1, X_k2, Z, color="black")
ax.set_title("wireframe");
plt.show()