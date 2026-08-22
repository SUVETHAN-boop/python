import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,46,50]

#line plot

graf2 = plt.plot(x,y,label =("mark"))
plt.xlabel("X value")
plt.ylabel("Y value")
plt.legend()
plt.show()