import requests, json

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(response.text)
data = response.json()
print(data, type(data))

# with open("data.json", "w") as f:
#     f.write(json.dumps(data))
try:
    cantitate = float(input("Introdu cantitatea pentru conversie: "))
except ValueError:
    print("cantitatea trebuie sa fie un numar!")
    cantitate = float(input("Introdu cantitatea pentru conversie: "))
valuta = input("Introdu valuta: ").upper()

if valuta not in ["USD", "GBP", "EUR"]:
    valuta = input("Sunt disponibile doar USD, GBP, EUR: ").upper()

pret = data["bpi"][valuta]["rate_float"]
conversia = cantitate * pret
print(f"{cantitate} Bitcoin = {conversia} {valuta}")