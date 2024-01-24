print("\nHello World")
acc=99
print("\nacc = ", acc, ", acc type: ", type(acc))

#Multiple assignment:
a, b, c = 1, 2.0, "john"
print("\na: ",a,", Type of a: ",type(a),"\nb: ",b,", Type of b: ",type(b),"\nc: ", c, ", Typeof c: ", type(c))

#'del' -> python keyword to remove variables from console

#%%
#Conversion of datatypes-----
#ex: age=18 -> print("Age is: ", str(age))
name = "Kaamya"
age = 19
roll = 2010040027
print("\nMy name is " + name + ", age: " + str(age) + ", roll no: " + str(roll))
#%%

import keyword
print(keyword.kwlist)
# %%

#%%
#Defining function:-------------- 
#keyword: def
def area(r, PI=3.14):
    return (PI*r*r)

calcarea = area(10)
print("\nCalculated area with radius 10 = ", calcarea)
#%%