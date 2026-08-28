# T- test

from scipy.stats import chi2_contingency

group1 =[[50,30],[20,40]]

chi2, p_value, dof, expected = chi2_contingency(group1)

print("chi - Square statistic : ",chi2)
print("p-value : ",p_value)
print("Expected frequence : \n",expected)
print("dof : ",dof)