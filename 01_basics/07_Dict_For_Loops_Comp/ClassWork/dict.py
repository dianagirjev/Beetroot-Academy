dictionar = {
    True: "Adevarat",
    False: "Fals"
}
print(dictionar[True], dictionar[False], all(dictionar), any(dictionar), len(dictionar))
nou_dict = sorted(dictionar)
print(nou_dict)
print(dictionar.clear())
# del dictionar # - sterge cu totul
print(dictionar)

dictionar = {
    True: "Adevarat",
    False: "Fals"
}
print(dictionar, dictionar.keys(), dictionar.values())
print(list(dictionar.keys())[0], list(dictionar.values())[0])

dictionar = {
    1: "Adevarat",
    3.14: "Fals"
}
dictionar.setdefault(40, "Test")
print(dictionar[40])
dictionar[40] = "Aici nu este 40"
print(dictionar[40])

lista = []

for i in range(10):
    new_dict = {}
    new_dict.setdefault(i, "impar")
    if i % 2 == 0:
        new_dict[i] = i
    lista.append(new_dict)
print(lista)

lista_adrese = []

for i in range(10):
    adrese = {
        "oras": "",
        "strada": "",
        "cod_postal": "",
    }
    adrese.setdefault("tara", "RO")
    lista_adrese.append(adrese)
print(lista_adrese)

adresa = {
    "tara": "Moldova", 
    "oras": "Causeni",
}
for k, v in adresa.items():
    print(k,v)

for i, k in enumerate(adresa):
    print(i, k, adresa[k])

for k in adresa:
    print(k)
for k in adresa.keys():
    print(k)
print("%%%%%%%%")
for v in adresa.values():
    print(v)
print("%%%%%%%%")
for k, v in adresa.items():
    print(k, v)
for i, obj in enumerate(adresa.items()): # obj sunt niste upluri cu keysi valoarea
    k, v = obj
    print(i, k, v)