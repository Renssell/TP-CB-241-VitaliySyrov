from functions import add, sub, mul, div
from log import write_log
def get_number():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            write_log(f"Entered numbers: a={a}, b={b}")
            return a, b
        except ValueError:
            print("Будь ласка, введіть коректне число!")
            write_log("Error: incorrect number")

def operationing():

    a,b = get_number()
    op = input("Операція (add, sub, mul, div): ").strip().lower()
    write_log(f"Choose mod: {op}")

    if op == "add":
            print(add(a, b))
    elif op == "sub":
            print(sub(a,b))
    elif op == "mul":
            print(mul(a,b))
    elif op == "div":
            print(div(a,b))
    else:
            write_log(f"Wrong mod operation: {op}")     
            print("Wrong operation.")
