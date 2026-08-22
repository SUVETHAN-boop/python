import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = np.random.rand(5,5 )
sns.heatmap(data,annot = True , cmap = "coolwarm")
plt.title("heat map")
plt.show()