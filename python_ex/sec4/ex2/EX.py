             #Analyse a dataset distribution

from scipy.stats import skew,kurtosis
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#load setdata
url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

#Analysis
feature = df["Age"]

print("Skew : ",skew(feature))
print("Kuetosis : ",kurtosis(feature))

#Graf plot
sns.histplot(feature,color="blue",kde = True)
plt.title("distribution of Age ")
plt.show()
