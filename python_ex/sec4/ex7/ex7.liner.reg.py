import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df = df[["Fare", "Age"]].dropna()

x = df["Fare"].values.reshape(-1,1)
y = df["Age"].values

model = LinearRegression()
model.fit(x,y)

print("Slop : ",model.coef_[0])
print("Interceot : ", model.intercept_)
print("R - square : ",model.score(x,y))

sns.scatterplot(x =df["Fare"],y=df["Age"],color = "blue")
plt.plot(df["Fare"],model.predict(x),color="red",label="regersion line")
plt.legend()
plt.show()