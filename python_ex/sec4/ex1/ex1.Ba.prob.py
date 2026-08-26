from itertools import product

#sample_soace : Dice roll
sample_space = list(range(1,7))

#probability of rolling an even number
even_no = [2,4,6]
p_even = len(sample_space)/len(even_no)
print("p(Even) : ",p_even)