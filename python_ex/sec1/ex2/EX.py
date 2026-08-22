# factorial without any loop

def factorial(num):
    if num == 1 or num ==0:
        return 1
    else:
        return num*factorial(num-1)

def main(num):
    result = factorial(num)
    print(f"factorial number {num} = {result}")

main(5)
