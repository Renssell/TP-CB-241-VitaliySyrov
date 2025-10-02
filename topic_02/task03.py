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
    a = float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    op = input("Operation mod: +,-,*,/ ")
    match op:
        case"+":
            result = add(a,b)
        case"-":
            result = sub(a,b)
        case"*":
            result = mul(a,b)
        case"/":
            result = div(a,b)
        case _:
            print(f"Wrong mod")
            return
    
    
    print(f"Result: {result}")

calc()