             # calcullate corelation between features

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# data loard
url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

correlation_matrix = df.corr(numeric_only=True)

#vesuvalisatiom

sns.heatmap(correlation_matrix,cmap ="coolwarm",annot = True)
plt.title("feature of correlation")
plt.show()