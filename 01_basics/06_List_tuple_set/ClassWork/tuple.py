tuplu = tuple([1, 2, 3]) # tuplu imutable
tuplu = (1, 2, 3)
print("rezultat:", tuplu)
tuplu = (1)
print("rezultat:", tuplu)
tuplu = (1, )
print("rezultat:", tuplu)

tuplu = (1, 2, 3, 4, 5)
tuplu2 =tuplu[::-1]
print("Rezultat:", tuplu)
print("Rezultat:", tuplu2)

coords = ('n', 's', 'e', 'v', 'e') * 2
print("Rezultat:", coords.count('e'))
print("Rezultat:", coords.index('e'))

coords = ('n', 's', 'e', 'v', 'e') * 2
coordonatele = sorted(coords)
print(coordonatele)
# coords.sort()
# print(coords)

for i, item in enumerate(tuplu):
    print(i, item)
