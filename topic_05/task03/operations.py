from functions import add, sub, mul, div
def get_number():
    while True:
        try:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))
            return a, b
        except ValueError:
            print("Будь ласка, введіть коректне число!")

def operationing():

    a,b = get_number()
    op = input("Операція (add, sub, mul, div): ").strip().lower()

    if op == "add":
            print(f"Результат: {add(a, b)}")
    elif op == "sub":
            print(f"Результат: {sub(a, b)}")
    elif op == "mul":
            print(f"Результат: {mul(a, b)}")
    elif op == "div":
            print(f"Результат: {div(a, b)}")
    else:
            print("Wrong operation.")
