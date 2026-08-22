#local scope

def add(a,b):
    c=a+b
    return c

#global scope

name = "suve"
def say_hello():
    print("my name is",name)

def say_hello():
    print(name)
