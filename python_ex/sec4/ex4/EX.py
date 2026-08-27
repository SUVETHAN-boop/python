             #two sample T- test

import numpy as np
from scipy.stats import ttest_ind

group1 = [12,14,15,16,17,18,19]
group2 = [11,13,14,15,16,17,18]

t_stats,p_value = ttest_ind(group1,group2)
print("T - statistic : ",t_stats)
print("P - value : ",p_value)

alpha = 0.05

if p_value <= alpha:
    print("Reject the null hypothises : siginificant difference")

else:
    print("Fail to Reject the null hypothises : no siginificant difference")