
#8/3/2022, PMF for DRV (similar to prev code but discretized o/p)

#%%

import numpy as np 
import matplotlib.pyplot as plt

elements_samplespace = [2,3,4,3,4,2,4,5,3,5,6,7,7,6,7,8,9,9]
elements_samplespace = np.array(elements_samplespace)
N_S = len(elements_samplespace)
print("\n\nb. PMF for DRV\nArray/list size: ", N_S)
U, NU = np.unique(elements_samplespace, return_counts = True)
print("Distinct values present: ", U)
print("Frequency of each value: ", NU)

P_U = NU/N_S
print("\nProbability = frequency/size:\n", P_U)
import matplotlib.pyplot as plt
plt.stem(U,P_U)
plt.xlabel('unique sample')
plt.ylabel('probability')
# %%