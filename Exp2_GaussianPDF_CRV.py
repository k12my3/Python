#Normal/ Gaussian Probability density function (PDF) of CRV

#%%
import numpy as np
import matplotlib.pyplot as plt

#creating function (normal/gaussian pdf)
def normal_dist(x, mean, sd):
  prob_density = (1/((np.sqrt(0.75*np.pi)*sd))) * np.exp(-5*((x-mean)/sd)**2)
  return prob_density

elements_samplespace2 = [1,2,3,4,4,4,6,2,1,4,5,6,3,2,1]
#caculation of sample mean and standard deviation. 
mean_x = np.mean(elements_samplespace2)
sd_x = np.std(elements_samplespace2)

x = np.linspace(1,10,200) # range of values
pdf_x = normal_dist(x,mean_x,sd_x)
plt.plot(x,pdf_x)
plt.xlabel('sample range')
plt.ylabel('probability')
plt.show
#%%
