import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

corrrelation = df.corr(numeric_only=True)

sns.heatmap(corrrelation,annot = True,cmap = "coolwarm")
plt.title("Correlation Heatmap")
plt.show()