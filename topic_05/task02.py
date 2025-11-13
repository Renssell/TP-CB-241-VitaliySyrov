import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")


amount = float(input("Enter amount: "))
currency = input("Enter exchange rate (from currency USD, EUR, PLN): ").upper()
rate = None
for elem in response.json():
    match currency:
        case "USD" if elem["cc"] == "USD":
            rate = elem["rate"] 
            break
        case "EUR" if elem["cc"] == "EUR":
            rate = elem["rate"] 
            break
        case "PLN" if elem["cc"] == "PLN":
            rate = elem["rate"] 
            break

if rate:
    converted = amount * rate
    print(f"{amount:.2f} {currency} = {converted:.2f} UAH")
else:
    print("Wrong currency")
