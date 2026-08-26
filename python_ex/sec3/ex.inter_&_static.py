             #Intrvala and Statistical

import scipy.stats as stats

data = [10,20,30,40,50,]
data_len = len(data)

# Sample_mean
sample_mean = sum(data) / data_len

# Z Score
z_score = 1.96

#Standrad deviatiom
variance = sum(( x - sample_mean)**2 for x in data) / data_len
std = variance**0.5

# CI
ci = (sample_mean - z_score * std / data_len**0.5,
sample_mean + z_score * std / data_len**0.5)

print("95  confidence Interval : ",ci)