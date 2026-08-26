             #mean,median and mode

data = [10,20,30,40,50]
data_len = len(data)
data_sorted = sorted(data)
#mean
mean = sum(data) / data_len
print("mean : \n",mean)

#median
                                                                # \ - next line
median = data_sorted[data_len // 2] if data_len % 2 != 0 else \
(data_sorted[data_len // 2 -1] + (data_sorted[data_len // 2])) /2

print("median : \n",median)

#mode
from statistics import mode
print("mode : \n",mode(data))


                 #variance and Standrad deviation

#variance
variance = sum((x - mean)**2 for x in data) / data_len
print("variance : \n",variance)

#Standrad deviation
std = variance ** 0.5
print("Standrad deviation : \n",std)