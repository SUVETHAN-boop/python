             #Impelement Stochastic Gradient Descent for Liner model

import numpy as np

np.random.seed(42)
x = 2 * np.random.rand(100,1)
y = 4 + 3 * x +np.random.randn(100,1)

x_b = np.c_[np.ones((100,1)),x]

def stochastic_gardient_descent(x,y,theta,iteration,learning_rate):
    m=len(y)
    for iter in range(iteration):
        for i in range(m):
            random_int = np.random.randint(1,100)
            xi = x[random_int:random_int + 1]
            yi = y[random_int:random_int + 1]
            guess = xi @ theta
            error = guess - yi
            gardients = 2 * xi.T @ error
            theta -= learning_rate * gardients
    return theta


theta = np.random.randn(2,1)
learning_rate = 0.01
iteration = 50

theta_opt = stochastic_gardient_descent(x_b,y,theta,iteration,learning_rate)
print("Optimized theta : \n",theta_opt) 
