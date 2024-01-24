
import numpy as np
a = ["abc", 2342, 1244, "xyz"]
print("\nNumpy - lists:\nType of list-a = ", type(a))
print("Shape and length of list-a = ", np.shape(a), "&", len(a))
print("Elements in list-a = ", a[0], a[1:3], a[2:1], a[-1])

#Find sum of 2 arrays:
import numpy as np
a = np.array([1,3,5])
b = np.array([2,4,6])
print(f'Sum of arrays-a,b: {a+b}')

#reshape array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print("\nNew reshaped array:\n", newarr)

#Find Square root of number in array:
a = np.array([1,4,9])
print("Square root of no. in array = ", np.sqrt(a));

#concat and stack arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("\nConcatenated array: ",arr)
arr = np.dstack((arr1, arr2))
print("\nStacked array:\n",arr)

#split arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print("\nSplit arrays:\n",newarr)


#Find Random Values
x = np.random.rand(6,7)
print("\n-----\n\nRandom Numbers:\n", x)

#Find random int values
c = np.random.randint(2, size=10)
print("\n-----\n\nRandom Int-values: ", c)