         #EX1 conduct t-test

from scipy.stats import ttest_1samp,ttest_ind,ttest_rel

#one-sample t-test

data = [12,14,15,16,17]
population = 15

t_stats , p_value = ttest_1samp(data,population)

print("one - sample t-test : ",t_stats,p_value)

#two-sample t-test

group1 = [12,14,15,16,17]
group2 = [11,13,14,15,16]

t_stats,p_value = ttest_ind(group1,group2)

print("two sample t-test : ",t_stats,p_value)

#paired test

pre_test = [12,14,15,16,17]
post_test = [11,13,14,15,16]

t_stats,p_value = ttest_rel(pre_test,post_test)

print("paired t-test : ",t_stats,p_value)