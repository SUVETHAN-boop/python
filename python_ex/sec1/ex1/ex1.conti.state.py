#condition statement

#1.if condition
print("/...if condition.../\n")

num = 10
if num > 0:
    print("positive")

else:
    print("negative")

#2.nested if condition
print("/...nested if condition.../\n")

age = 23

if age >= 18:
    if age <=30:
        print("Young Adult")
    else:
     print("Adult")

else:
   print ("Child")


#3.for Statement
print("/...for statement.../\n")

fruits = ["apple","orange","banana"]
count =1
for fruit in fruits:
   print(count,".",fruit)
   count = count+1


#4.while statement
print("/...while statement.../\n")

count = 5
while count>0:
   print(count)
   count = count-1

print("outside")

#5.break statement 
print("/...break statement.../\n")

for i in range(1,10):
   if i==7:
      break
   print(i)


#6.continue statement
print("/...continue statement.../\n")

for i in range(10):
   if i%2 == 0:
    continue
   print(i)
      
