             # perform T - test

from scipy.stats import ttest_ind

group1 = [2.1,2.5,2.8,3.0,3.2]
group2 = [1.8,2.0,2.4,2.7,2.9]

t_test,p_value = ttest_ind(group1,group2)
print("T - test : ",t_test)
print("P - value : ",p_value)

alpa = 0.5

if p_value < alpa:
    print("Reject the null hypothesis : siginificant difference")

else:
    print("Failed to reject the null hypothesis : no siginificant difference")