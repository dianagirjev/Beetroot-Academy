def calc(operation, a, b):
    return funcs[operation](a, b)


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
print(list(filter(
    lambda x: x % 2 == 0,
    numere
)))

print(list(filter(
    functie,
    numere
)))