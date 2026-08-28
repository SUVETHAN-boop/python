from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,6,8,10])

module = LinearRegression()
module.fit(x,y)

print("slpoe : ",module.coef_[0])
print("Intercept : ",module.intercept_)
print("R-square : ",module.score(x,y))