lista = list(range(20))

print("Lista originala", lista)
print(lista[1])

# List Slicing
start_index = 0
end_index = len(lista)
step = 1
print("Rezultat:", lista[start_index : end_index : step])

start_index = 5
end_index = 16
step = 2
print("Rezultat:", lista[start_index : end_index : step])

print(lista[-2])
start_index = 2
end_index = -2
step = 1
print("Rezultat:", lista[start_index : end_index : step])
print("Rezultat:", lista[ : : -1])

# run = True
# index = 0
# step = -1
# while run:
#     print(lista[index * step])
#     index +=1
#     if index == (len(lista) - 1) / 2:
#         break    


coordonate = [
    "W", 
    "N", 
    "E", 
    "S", 
    "Oras",
    "Judetul",
    "Tara",
]
print(coordonate[4:])
print(coordonate[:-3])

# Functii utile:
lista.insert(1, '55')
print(lista)

x = lista.pop(1)
print(lista)
print(x)

coords = ['n', 's', 'e', 'v', 'e'] * 2
print(coords.index('v'))

print(coords.count('n'))

out = []
start = 0
stop = len(coords)
for i, item in enumerate(coords):
    if item == 'e':
        out.append(i)
# gasit = -1
# while start != stop:
#         gasit = coords[start:stop].find('e')
#     print(gasit)
#     start = gasit + 1
# print(out)

coords = ['n', 's', 'e', 'v', 'e'] * 2
coords.sort()
coordonatele = sorted(coords)
print(coords)
print(coordonatele)