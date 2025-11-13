from operations import operationing

def main():
    while True:
        operationing()
        again = input("One more? (y/n): ").lower()
        if again != "y":
            print("Good luck")
            break

if __name__ == "__main__":
    main()