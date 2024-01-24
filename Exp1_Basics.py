#### Object #### -> var type : class | var : object of class

from operator import concat
import numpy as np

a = 1 # This is an object (int)
print("----------\n\nType of a=1: ", type(a))
a1 = 1.2 # This is an object (float)
print("Type of a1=1.2: ", type(a1)) # returns type of variable
b = a1 + 3
print("\n(a1=1.2 + 3) = b = ", b)
print("Type of b: ", type(b))
c = a*a1
print("\n(a=1 * a=1.2) = c =", c)
print("Type of c: ", type(c))

b_1 = True #Object bool
print("\n----------\n\nb_1 is: ", b_1)
print("Type of b_1", type(b_1))
c_1 = b_1 + b_1 # + operation amon bool -> converts object type to int
print("\nb_1 + b_1 = c_1 = ", c_1)
print("Type of c_1: ", type(c_1)) #-> returns answer of int type and considers true + true as 1+1 = 2

# Object type String
s_1 = "SAAC"
print("\n----------\n\ns_1:", s_1)
print("s_1 type", type(s_1))
s_2 = "SAAP"
print("\ns_2: ", s_2)
print("s_2 type: ", type(s_2))
s_3 = s_1 + s_2 
print("\nHorizontal Concatenation :\ns3 = s_1 + s_2: ", s_3) #returns concatenated output
print("s_3 type: ", type(s_3))
print("s_3 val w/ concat funciton: ", concat(s_1, s_2)) #also returns concatenated output
#hw : print vertical concatenation
print("\nVertical concatenation :\n")
for x in range(4):
    print(s_1[x] + s_2[x], end="") 
#printing concated string : char from each string
#end function -> prevents printing in next line, instead no ending ("")
#ex: ending(" ") -> ends the current print statement w. space
# ^ then output: SS AA AA CP 

#Multiple assignment:
a, b, c = 1, 2, "john"
print("\n----------\n\nMultiple assignment:\n", a, " ", b, " ", c)

# Object tyoe Lists
l1 = [1, 1.2, 'cc', True]
print("\n----------\n\nL-1: ", l1)
l2 = [3, '66', False]
print("L-2: ", l2)
l3 = l1 + l2
print("L-3 = L-1 + L2 =", 13)
print("L-3 Type: ", type(l3))

#Retrival of elements in lists:
k1 = l1[0]
print("\n----------\n\nk1 = L1[0] = ", k1)
print("k1 type: ", type(k1))
k2 = l1[0:2]
print("\nk2 = L1[0:2] = ", k2)
print("k2 type: ", type(k2),)
k3= l1[-1]
print("\nk3 = L1[-1] = ", k3)
print("k3 type: ", type(k3))

#converting lists to arrays using numpy libraries: import numpy as np -> numerical operations in form of matrix for arrays
#hw : find different libraries in py used for ML and DL
aa_1 = np.array(l1)
print("\n----------\n\narr1: ", aa_1)
print("arr1 type: ", type(aa_1))

aa_n = [1, 1.2, 3, 4.5]
aa_n1 = [1, 3, 4]
aa_n = np.array(aa_n)
aa_n1 = np.array(aa_n1)

print("aa_n array : ", aa_n)
print("aa_n1 array : ", aa_n1)
aa_2 = aa_n*aa_n #cannot multiply n1 and n -> because different sizes
print("\narr2 = aa_n*aa_n (vector multiplication) = ", aa_2)
print("arr2 type:  : ", type(aa_2) , "\n")