import numpy as np

#dise roll - 10,000 times
roll = np.random.randint(1,7,size = 10000)

#probability
even_p = np.sum(roll%2 == 0) / len(roll)
odd_p =np.sum(roll%2 != 0) / len(roll)
p_greater_than_4 = np.sum(roll > 0) / len(roll)

print("probability of even number : ",even_p)
print("probability of odd number : ",odd_p)
print("probability of greater than 4 : ",p_greater_than_4)

#prim number probability in dise roll

prime_p = np.sum((roll == 2) | (roll == 3) | (roll == 5)) / len(roll)
not_prime_p = np.sum(~((roll == 2) | (roll == 3) | (roll == 5))) / len(roll)

print("Probability of  prime number : ",prime_p)
print("Probability of not prime number : ",not_prime_p)