# Pearsonr and spermanr

import numpy as np
from scipy.stats import pearsonr,spearmanr

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

r, _ = pearsonr(x,y)
rho , _ = spearmanr(x,y)

print("person correlation : ",r)
print("spearmanr correlation : ",rho)
