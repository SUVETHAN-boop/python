             # mean, variance and standrad deviation to simple methode using numpy method

import numpy as np

data = [10,20,30,40,50]

#calculate
mean = np.mean(data)
variance = np.var(data)
standrad_devi = np.std(data)

print("Mean : ",mean)
print("Variance : ",variance)
print("Standrad Deviation : ",standrad_devi)