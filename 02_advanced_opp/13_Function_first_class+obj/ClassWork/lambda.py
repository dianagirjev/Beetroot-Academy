
def lam(a, b):
    return a + b

test = lambda a, b: a + b # functie anonima
print(dir()) # nu se gaseste lambda aici
print(lam(1, 2))
print(test(1, 2))

numere = [1, 2, 3, 4]
def functie(x):
    if x % 2 == 0:
        return True
    return False

functie2 = lambda x: x % 2 == 0

print(list(filter(
    functie2,
    numere
)))

print(list(filter(
    functie,
    numere
)))

######################
def functie(x):
    if x % 2 == 0:
        return True
    return False
lista_noua = []
for item in numere:
    if functie(item):
        lista_noua.append(item)

print(lista_noua)
#######################