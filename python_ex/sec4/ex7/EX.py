             #REAL WORLD - analyse the statistic data

# 1) perfer explore the data analysis
# 2) conduct hypothesis test
# 3) apply linear regeration

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.linear_model import LinearRegression

url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.info())
print(df.describe())

df["Age"] = df["Age"].fillna(df["Age"].mean())
survived = df["Survived"].dropna()

contingency_table = pd.crosstab(df["Age"],survived)
print("contingency table : \n",contingency_table)

ch2,p_value,dof,excepted = chi2_contingency(contingency_table)

print("chi- square statistis :",ch2)
print("expeted statistic : ",excepted)
print("p - value : ",p_value)

alpha= 0.05
if p_value <= alpha:
    print("reject the null hypothises :variable are dependent")

else:
    print("fail to reject the null hypothises :variable are dependent")


x = df["Age"].values.reshape(-1,1)
y = df["Survived"]

model = LinearRegression()
model.fit(x,y)

print("slope : ",model.coef_[0])
print("intercept : ",model.intercept_)
print("R - square : ",model.score(x,y))

sns.scatterplot(x = df["Age"],y = df["Survived"],color= "blue",label="Data")
plt.plot(df["Age"],model.predict(x),color="red",label="regeration line")
plt.legend()
plt.title("Linnear Regaration")
plt.show()
