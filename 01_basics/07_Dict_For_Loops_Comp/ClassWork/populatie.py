import requests, json

response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")

data = response.json()["data"]
# print(data)

data = [item["Population"] for item in data][::-1]
print(data)

calculat = []
statistica = {}
first_year = 2013
for i in range(len(data) - 1):
    anul = f"{first_year + i} - {first_year + i + 1}"
    diferenta = data[i + 1] - data[i]
    statistica[anul] = diferenta
    calculat.append(diferenta)
print(calculat)
print(statistica)
print("Modificarea pe an:", sum(calculat) / len(calculat))

for k, v in statistica.items():
    print(f"Diferenta la populatia anului: {k} --- {v}")