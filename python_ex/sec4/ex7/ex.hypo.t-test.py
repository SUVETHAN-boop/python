import pandas as pd
from scipy.stats import ttest_ind


url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df['Sex'].unique())
print(df['Sex'].value_counts())

male_age = df[df['Sex'] == 'male']['Age'].dropna()
female_age = df[df['Sex'] == 'female']['Age'].dropna()

print("Male count:", len(male_age))
print("Female count:", len(female_age))

t_stat,p_value = ttest_ind(male_age,female_age)

print("T-Statistic : ",t_stat)
print("P-value : ",p_value)

alpha = 0.05

if p_value <= alpha:
    print("Reject all null hypotesis : siginificant difference")

else:
    print("Reject all null hypotesis : siginificant difference")
