import pandas as pd
import seaborn as sns
import  matplotlib.pyplot as plt

url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.info())
print(df.describe())

#versuvalissation
sns.histplot(df["Age"],kde = True)
plt.title("distrimution of sex")
plt.show()

#corelationheatmap
sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
plt.title("correlation heatmap")
plt.show()

