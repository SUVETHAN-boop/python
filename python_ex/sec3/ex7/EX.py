#task 1 : Implement the mathematical formula for linear regression
#task 2 : Use grandient descent to optiniza the made parameters
#task 3 : Calculate evaluvation metrics

import numpy as np

np.random.seed(42)
x = 2 * np.random.rand(100,1)
y = 4 + 3 * x +np.random.randn(100,1)

x_b = np.c_[np.ones((100,1)),x]

theta = np.random.randn(2,1)
learing_rate = 0.001
iteration = 1000

# linear regression
def predict(x,theta):
    return np.dot(x,theta)

# grandient descent 
def grandient_des(x,y,theta,learing_rate,iteration):
    m = len(y)
    for _ in range(iteration):
     prediction = np.dot(x,theta)
     error = prediction - y
     gardient = (1/m) * np.dot(x.T,error)
     theta -= learing_rate * gardient

    return theta


#msr and r^2
def mean_squared_error(y_true,y_pred):
   return np.mean((y_true - y_pred)**2)

def r_squared(y_true,y_pred):
   ss_res = np.sum((y_true - y_pred)**2)
   ss_tot = np.sum((y_true - np.mean(y_true))**2)
   return 1-(ss_res/ss_tot)

# perfome gradient decent
optimized_theta = grandient_des(x_b ,y,theta ,learing_rate ,iteration)

# perdiction and evaluvation
y_pred = predict(x_b , optimized_theta)
mse = mean_squared_error(y,y_pred)
r2 = r_squared(y,y_pred)

print("Optimized theta : \n",optimized_theta)
print("MSE : ",mse)
print("R^2 : ", r2)