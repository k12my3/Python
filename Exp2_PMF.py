
#%%

import numpy as np 
import matplotlib.pyplot as plt

#probability mass function (PMF) of DiscreteRandomVars

elements_samplespace = [1, 7, 3, 3, 4, 2, 1, 4, 4, 5, 7, 5, 6, 7, 5, 6]
elements_samplespace = np.array(elements_samplespace)
N_S = len(elements_samplespace) # array size
print("\n\na. PMF using for loop\nArray size : ", N_S)
U, NU = np.unique(elements_samplespace, return_counts=True) 

"""
U : returns the distinct values present in list / array 
NU : returns the frequency of the values
"""
print("Distinct values present: ", U)
print("Frequency of distinct value present: ", NU)

print("\nUsing for loop:")
for i in range(0, N_S):
        # Check if the picked element
        # is already printed
        d = 0
        for j in range(0, i):
            if (elements_samplespace[i] == elements_samplespace[j]):
                d = 1
                break
        # If not printed earlier,
        # then print it
        if (d == 0):
            print(elements_samplespace[i], end=" ")
        #end -> avoid printing in next line for for loop
        #instead ending symbol : " " -> space

P_U = NU/N_S #frequency / size = scale or probability.
print("\n\nProbability = frequency / size :\n", P_U) #Probability

#Plotting PMF : import matplotlib.pyplot as plt
plt.plot(U, P_U)
plt.xlabel("Unique Samples")
plt.ylabel("Probability")
# %%

'''
# generating probabilities of unique elements of samples
P = []
for el in U:
  N_el = elements_samplespace.count(el)
  P_el = N_el/N_S
  P.append(P_el)
'''