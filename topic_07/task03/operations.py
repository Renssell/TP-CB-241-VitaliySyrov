from functions import Operations
class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.result = None

    def get_number(self):
        while True:
            try:
                self.a = float(input("Введіть перше число: "))
                self.b = float(input("Введіть друге число: "))
                break
            except ValueError:
                print("Будь ласка, введіть коректне число!")

    def operationing(self):

        op = input("Операція (add, sub, mul, div): ").strip().lower()

        if op == "add":
            self.result = Operations.add(self.a, self.b)
        elif op == "sub":
            self.result = Operations.sub(self.a, self.b)
        elif op == "mul":
            self.result = Operations.mul(self.a, self.b)
        elif op == "div":
            self.result = Operations.div(self.a, self.b)
        else:
                print("Wrong operation.")
                self.result = None

        return self.result

    def show_result(self):
        if self.result is not None:
            print(f"Результат: {self.result}")