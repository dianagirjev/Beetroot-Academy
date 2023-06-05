o_lista = ['a', 'b', 'c', 'aaa']
item = 'd'
ignore = True

if item in o_lista:
    print(True)
else:
    print(False)

if 'a' not in o_lista:
    print(True)
else:
    print(False)

if 'a' in o_lista and 'z' not in o_lista:
    print('Alfabet')
else:
    print('Incomplet')

if 'a' in o_lista and 'z' in o_lista or ignore:
    print('Alfabet')
else:
    print('Incomplet')

if 'Aaa'.lower() in o_lista and 'z' in o_lista or ignore:
    print('Alfabet')
else:
    print('Incomplet')