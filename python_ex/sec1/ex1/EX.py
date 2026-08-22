# EX1:1.prime number

num = int(input("enter the number: "))

if num>1:
  for i in range(2,int(num**0.5)+1): #num^+1 
    if num%2 == 0:
      print(f"this number is {num} not prime number ")  
      break
    else:
            print(f"this number is {num} prime number ")  

else:
          print(f"this number is {num} not prime number ")  



#2.calculatoe
print("/...calculator.../\n")

def add(a,b):
     return a+b

def sub(a,b):
     return a-b

def mult(a,b):
     return a*b

def div(a,b):
     if b == 0:
          print("not division")

     else:
          return a/b


while True:
     print("//.menu.//\n")
     print("1. Add\n")
     print("2. Sub\n")
     print("3. Mul\n")
     print("4. Div\n")
     print("5. exsist\n")


     choice = int(input("choice you menu:"))
     if choice == 5:
          print("prosess...")
          break
     num1 =float(input("enter the first number:" ))
     num2 =float(input("enter the second number:" ))
          
     if choice == 1:
          print("Result: ",add(num1,num2))

     elif choice == 2:
               print("Result: ",sub(num1,num2))

     elif choice == 3:
               print("Result: ",mult(num1,num2))

     elif choice == 4:
               print("Result: ",div(num1,num2))

     else:
           print("exsisting")
                   


    
