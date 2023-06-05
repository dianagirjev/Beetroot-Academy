text = 'Hello, world!'
print(text)
print('Alt text')
print(f'Iaca cheva nou {text}')

# Tipuri de date
numar_n = 21425 # integer
numar_r = 3.14 # float
text_1 = 'Hi' # string
biti = b'Hello' # biti
adevarat = True # boolean/bool
fals = False # boolean/bool

lista = [1, numar_n, 'sdr'] # list - modificam ordinead elementelor - MUTABLE
print(lista)
print(lista[0])

tuplu = (1, 2, 3, 'str', text) # tuple - IMUTABLE - la returnare e folosit bine
print(tuplu)

dictionary = {
    'ana': 5,
    'vasile': "marinar"
} # dict
print(dictionary)
print(dictionary["ana"])

lets_go = 'Acesta este un text ' + text
print(lets_go)

nou = f'Acesta este un text {text}'
print(nou)

nou = f'Acesta este un text {dictionary}'
print(nou)

#nou = f'Acesta este un text {dictionary['cifra']}' #
#print(nou)

nou = f'Acesta este un text {dictionary["ana"]} {tuplu[1]}' 
print(nou)

lista_pentru_set = [34, 5, 34, 9]
setul = set(lista_pentru_set) # set - toate valorile sunt unice, IMUTABLE, 
set2 = set([1, 2, 5, 6, 5])
print(setul)
print(set2)

text = 'Acesta este un text'
text_nou = text.strip()
print(text_nou)

text_nou = text.lower()
print(text_nou)

text_nou = text.split('e')
print(text_nou)

PI = 3.14 # sa o tratam ca si constanta conventie
print(PI * 5)