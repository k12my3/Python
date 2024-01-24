name = input("Enter your name: ")
print("Hello " + name)

#Variables:
num = 10
pi = 3.14159
is_student = True
print("\n-----\n\nVariables-O/P: ", num, pi, name, is_student)

#Datatypes:
a,b,c = 1, 2.0, "Kaamya"
print("\n-----\n\nDatatypes-OP:\nType of a = ", a, "is ", type(a))
print("Type of b = ", b, "is ", type(b))
print("Type of c = ", c, "is ", type(c))

#Numpy + Lists:
import numpy as np
a = ["abc", 2342, 1244, "xyz"]
print("\n-----\n\nNumpy - lists:\nType of list-a = ", type(a))
print("Shape and length of list-a = ", np.shape(a), "&", len(a))
print("Elements in list-a = ", a[0], a[1:3], a[2:1], a[-1])
newvar = input("Please enter an input: ")
a.append(newvar)
a.index(2342)
b = [[3,4,5,5], [2,3,5,8], [3,4,5,2]]
print("Shape of list-b = ", np.shape(b))
len(a[0]) + len(b[1])
tinylist = [36381983, "test"]
print(tinylist*3)
print(a+tinylist)