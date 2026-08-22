             # 1. Access the element 

#Access by index 
gread =["A","B","C","S"]
print(gread[3])
print(gread[0])

#Access the negative indix
print(gread[-1])
print(gread[-4])


             # 2.Modify the list

fruits =["apple","orange","banana"]

# 1)Append function
fruits.append("grapes")
print(fruits)

# 2)insert function
fruits.insert(2,"jery")
print(fruits)

# 6) Slice function
slice = fruits[1:4]
print(slice)

# 3)Remove function
fruits.remove("orange")
print(fruits)

# 4)Delete function
del fruits[0]
print(fruits)

# 5)pops function
fruits.pop()
print(fruits)