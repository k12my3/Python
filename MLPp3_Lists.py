
#%%
import numpy as np
list1 = ["Kaamya", 2010040027, "ECE", 23.3]
print("List1:", list1)
print("Type:", type(list1))
print("Length:", len(list1))
print("Shape:", np.shape(list1))
print(list1[0], " ", list1[1:3], " ", list1[2:], " ", list1[-1])
#[x:y] display values at list indices from x to y-1
#if y not specified -> till the end / last index
# ':' -> indicates range
print("Index of 23.3:", list1.index(23.3))


# %%
#combined lists:
import numpy as np

list2 = [[1,2,3],[4,5,6]]
print("\n\nList2:", list2[1])
print(np.shape(list2[0][1]))
print(np.shape(list2[0]))
print("No. of elements in list2:", np.shape(list2)[0]*np.shape(list2)[1])
print(list2[1].index(4))

list3 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print("\nList3:", list3)
print("Shape:", np.shape(list3))
print("No. of elements in list3:", np.shape(list3)[0]*np.shape(list3)[1])

l4 = [123, "john"]
print(l4*3)
print(list1 + l4) #l4 is appended to l1 in o/p -> concatenation of lists

list1.append(1)
print(list1)
list1.append(l4[0])
print(list1)
# %%
