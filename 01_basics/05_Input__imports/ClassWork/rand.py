import random


# calculator = random.randint(1, 5)

# numar = int(input("Introdu un numar: "))

# counter = 0
# while numar != calculator:
#     numar = int(input("Introdu un numar: "))
#     counter += 1
#     print("Numarul era", calculator)
# print(f"Dupa {counter} incercari ai ghicit.")

# random.seed(123) # de fiecare dara acelasi numar random
# print(random.randint(1, 10))

lista = list(range(10))
print(f"Lista este: {lista}")

# lista_random = random.sample(lista, k = 3)
# print(f"Lista random este {lista_random}")

random.shuffle(lista)
print(f"Lista noua este {lista}")
