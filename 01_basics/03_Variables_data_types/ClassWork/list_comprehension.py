lista = [
    (11, 'a'),
    (12, 'b'),
    (13, 'c'),
    (14, 'd'),
]
print(f'Lista = {lista}')

comprehensible = []
for item in lista:
    if item[0] % 2 == 0:
        comprehensible.append(item[0])
    elif item[0] % 2 == 1:
        comprehensible.append(item[1])
print(f'comprehensible: {comprehensible}')

comprehensible = []
for i, item in enumerate(lista):
    if i % 2 == 0:
        comprehensible.append(item[0])
    elif i % 2 == 1:
        comprehensible.append(item[1])
print(f'comprehensible: {comprehensible}')

comprehensible = [item[0] for item in lista]
print(f'comprehensible: {comprehensible}')

comprehensible = [item[0] if i % 2 == 0 else item[1] for i, item in enumerate(lista)]
print(f'comprehensible: {comprehensible}')