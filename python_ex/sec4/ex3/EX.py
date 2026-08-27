# calculate confidence interval

import numpy as np
from scipy.stats import norm

data = np.random.normal(loc = 50 ,scale= 10 , size =100)

#sample
mean = np.mean(data)
std = np.std(data,ddof=1)
data_len = len(data)

#95% confidence interval
z_value = norm.ppf(0.975)
margine_error = z_value * (std/np.sqrt(data_len))
ci = (mean - margine_error),(mean + margine_error)

print("sample mean : ",mean)
print("95% confidence interval (sample) : ",ci)