import math

def add(a:float, b: float):
    return a+b
def sub(a:float,b:float):
    return a-b
def mul(a:float,b:float):
    return a*b
def div(a:float,b:float):
    if b!=0:
        return a/b
    else:
        return "Impossible"

def calc():
    while True:  
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Operation mod (add, sub, div, mul): ").strip().lower()
        if op=="add":
            result = add(a,b)
        elif op=="sub":
            result = sub(a,b)
        elif op=="mul":
            result = mul(a,b)
        elif op=="div":
            result = div(a,b)
        else:
            print("Невідома операція!")
            return
        
        print(f"Result: {result}")

   
        while True:
            answer = input("Enter Y if you want to use calc one more time or N to quit: ").strip().lower()
            if answer == "y":
                break
            elif answer == "n":
                print("Goodbye!")
                exit()  
            else:
                print("Invalid input! Please enter Y or N.")

calc()

