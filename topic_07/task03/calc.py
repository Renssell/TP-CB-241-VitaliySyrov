from operations import Calculator

def main():
    calc = Calculator()
    while True:
        calc.get_number()
        calc.operationing()
        calc.show_result()
        again = input("\nTry one more? y/n: ").lower()
        if again != "y":
            print("Thx, gl")
            break

if __name__ == "__main__":
    main()
