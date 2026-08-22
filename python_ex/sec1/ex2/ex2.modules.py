#import an entire module

import math
print(math.sqrt(16))

#import specific function

from math import sqrt
print(sqrt(16))

#use aliases

import math as m 
print(m.sqrt(16))
