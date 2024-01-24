
#%%
import numpy
first_array = numpy.array([1,2,3])
print(first_array) #for first_array[-1], op: 3 (-ve -> counts from last to first)
print(type(first_array))
print(len(first_array))
print(first_array.shape) #op: (3,) -> one dimensional array with 3 elements


# %%
import numpy as np
second_array = np.array([[1,2,3], [4,5,6]]) #after 1st square bracket -> array
print("\n\n", second_array)
print(type(second_array))
print(len(second_array)) #op: 2
print(second_array.shape) #op: 2,3
print(len(second_array[0]) + len(second_array[1]))
print(second_array.shape[1])
print(second_array[0])
print(second_array[-2][-1])
#index of 4 : [-1][-3]


# %%
#3d array, each consisting of 5 elements
import numpy as np
third_array = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
print("\n\n", third_array)
print(type(third_array))
print(len(third_array))
print(third_array.shape) #op is an array
print("Index of 9: ", third_array[1,3])
print("Index of 10: ", third_array[-2,-1])
print("Total no. of elements [third_array]: ", third_array.shape[0] * third_array.shape[1])


# %%
