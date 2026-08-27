             #perform hypothesis test

import numpy as np
from scipy.stats import ttest_1samp

data = [12,14,15,16,17,18,19]

sample_mean = np.mean(data)
population_mean = int(sample_mean)

t_stat,p_value = ttest_1samp(data,population_mean)

print("T - statistic : ",t_stat)
print("P- value : ",p_value)

print("population mean (guess mean) : ",population_mean)
print("sample_mean(true mean) : ",sample_mean)

alpha = 0.05

if p_value <= alpha:
    print("Reject the null hypothises : siginificant difference")

else:
    print("Fail to Reject the null hypothises : no siginificant difference")