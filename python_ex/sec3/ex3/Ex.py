             # Impilement of gradent descent for linear regression

import numpy as np

def gradient_descent(X,y,theta,iterations,learning_rate):
    m = len(y)
    for _ in range(iterations):
      guess = np.dot(X,theta)
      error = guess - y
      gradient = (1/m)*np.dot(X.T,error)
      theta -= learning_rate * gradient
    return theta

#sample data
X = np.array([[1,1],[1,2],[1,3]])
y = np.array([2,2.5,3.5])
theta =np.array([0.1,0.1])
learning_rate = 0.1
iterations = 1000

#perfomance

optmized_theta = gradient_descent(X,y,theta,iterations,learning_rate)
print("Optimized Parameters : \n",optmized_theta)