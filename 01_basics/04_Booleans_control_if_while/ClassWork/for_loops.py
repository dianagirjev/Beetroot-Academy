lista = range(10)
for i in lista:
    print(i, end = ' ')
print('\n')

lista = ['a', 'b', 'c', 'd']
for i in lista:
    print(i, end = ' ')
print('\n')

lista = ['a', 'b', 'c', 'd']
for i, value in enumerate(lista):
    print(f'Indexul {i} are valoarea {value}')
print('\n')

# pot fi adaugate greseli daca amitem value cu enumerate
lista = ['a', 'b', 'c', 'd']
for i, value in enumerate(lista):
    print(f'Indexul {i} are valoarea {lista[i]}')

for tuplu in enumerate(lista):
    i, value = tuplu
    print(tuplu, i, value)
    if i == 1:
        break
else:
    print("ELSE")

for tuplu in enumerate(lista):
    i, value = tuplu
    print(tuplu, i, value)
else:
    print("ELSE")
