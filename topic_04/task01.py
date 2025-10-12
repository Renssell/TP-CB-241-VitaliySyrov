import math

def add(a:float, b: float):
    return a+b
def sub(a:float,b:float):
    return a-b
def mul(a:float,b:float):
    return a*b
def div(a:float,b:float):
    try:
        return a / b
    except Exception as ex:
        print(type(ex))
        print(ex.args)
        print(ex)
        return None

def get_number(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Будь ласка, введіть коректне число!")

def calc():
     while True:
        a = get_number("Введіть перше число: ")
        b = get_number("Введіть друге число: ")

        while True:
            op = input("Операція (add, sub, mul, div): ").strip().lower()

            try:
                if op == "add":
                    result = add(a, b)
                elif op == "sub":
                    result = sub(a, b)
                elif op == "mul":
                    result = mul(a, b)
                elif op == "div":
                    result = div(a, b)
                    if result is None: 
                        continue
                print(f"Result: {result}")
                break  

            except Exception as ex:
                print(type(ex))
                print(ex.args)
                print(ex)
                continue

        while True:
            answer = input("Enter Y if you want to use calc one more time or N to quit: ").strip().lower()
            if answer == "y":
                break
            elif answer == "n":
                print("Goodbye!")
                return
            else:
                print("Invalid input! Please enter Y or N.")
calc()

