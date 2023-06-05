lista = list(range(10))
lista_noua = [i**2 if i == 4 else 0 for i in lista]
print(lista)
print(lista_noua)

lista_noua = [i**2 for i in lista if i >= 4]
print(lista)
print(lista_noua)

adresa = {
    "tara": "Moldova", 
    "oras": "Causeni",
    "strada": "Vitanski",
    "numar": "15"
}

dictionar = {}
for i in range(10):
    dictionar[str(i)] = i
print(dictionar)

dictionar_nou = {str(i): i for i in range(10)}
print(dictionar_nou)

dictionar_nou = {str(i): i for i in range(10) if i % 2 == 0}
print(dictionar_nou)

dictionar_nou = {str(i): i for i in range(11) if i % 2 == 0 if i % 5 == 0}
print(dictionar_nou)

dictionar_nou = {str(i): i if i % 2 == 0 else 0 for i in range(11)}
print(dictionar_nou)