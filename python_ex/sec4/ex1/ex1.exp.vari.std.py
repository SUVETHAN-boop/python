import numpy as np

#random variable : dice roll
outcome = np.array([1,2,3,4,5,6])
probability = np.sum((1/6)*6)

#expatation
expatation = np.sum(outcome*probability)
print("Expatation (Mean) : ",expatation)

#variance and standrad deviation
variance = np.sum((outcome*expatation)**2*probability)
std =np.sqrt(variance)
print("Variance : ",variance)
print("Standrad deviation : ",std)