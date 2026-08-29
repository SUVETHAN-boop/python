# fit simple linear regaration

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)
x = np.random.rand(100,1) * 10
y = 3 * x + np.random.randn(100,1) *2

module = LinearRegression()
module.fit(x,y)

slop = module.coef_[0][0]
intercept = module.intercept_
r_squared = module.score(x,y)

plt.scatter(x,y,color = "blue",label = "Data")
plt.plot(x,module.predict(x),color = "red",label="regeression line")
plt.title("Linear regeression")
plt.legend()
plt.show()

