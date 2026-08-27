             #construction confidence interval

import numpy as np
from scipy.stats import t

# for Mean

data = [12,13,14,15,16,17,18,19]

mean = np.mean(data)
data_len = len(data)
probability = 0.975

#Standrad deviation (population) / use : ddof = 0 
std = np.std(data,ddof=0)
t_value = t.ppf(probability,df = data_len - 1)

margine_error = t_value *(std/np.sqrt(data_len))
ci = (mean - margine_error),(mean + margine_error)

print("95% Confidence Interval (population) : \n",ci)




#Standrad deviation (sample) / use : ddof = 1
std = np.std(data,ddof=1)
t_value = t.ppf(probability,df = data_len - 1)

margine_error = t_value *(std/np.sqrt(data_len))
ci = (mean - margine_error),(mean + margine_error)

print("95% Confidence Interval (sample) : \n",ci)