             # Bay's theorem
#problems
# - A desease is affected by 1% of population
# - A text is 95% accurate for diseasted indiduvals and 90% accurate for non-diseased indiduval
# - Find the probability of having the disease given a positive test result

def bays_theorem(prior,sensitivity,specificity):
    posterior = (sensitivity * prior) / specificity
    return posterior

prior = 0.1               # 1% of desease affected population
sensitivity = 0.95          # true positive rate
specificity = 0.90        # true negative rate

posterior = bays_theorem(prior,sensitivity,specificity)
print("Probability of deseas given positive test : ",posterior)


             #Gaussion (normal) distribution using scipy.stats function

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,100)
y = norm.pdf(x,loc =0 ,scale =1)
plt.plot(x,y)
plt.title("Gaussion Distribution")
plt.show()