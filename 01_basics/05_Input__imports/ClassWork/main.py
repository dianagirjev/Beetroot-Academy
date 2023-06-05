# import const
# from const import PI, G
# from const import *
# import const as cst
from utils import PI
import utils

text = input("Introdu ceva: ")
print(text)

numar = input("Introdu un numar: ")
print(type(numar))

try:
    numar = int(numar)
except ValueError:
    print("Tip de date gresit")

if type(numar) == int:
    print("Numarul este: ", numar)
else:
    print("Eroare")

cerc = 2 * PI * numar
print("Circumferinta este:", cerc)

print(utils.get("http://google.com"))