import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

outcome = [1, 2, 3, 4, 5, 6]
probability = [1/6]*6

# discreate random :
plt.bar(outcome,probability,color = "blue",alpha =0.7)
plt.title("Probabiliy of dice")
plt.xlabel("outcomes")
plt.ylabel("probability")
plt.show()

# continous random variable uniform distribution

x = np.linspace(0,1,100)
pdf = uniform.pdf(x,loc = 0, scale =1)
plt.plot(x, pdf)
plt.title("pdf of uniform(0,1)")
plt.xlabel("x")
plt.show()