from file import read_phonebook, write_phonebook
from tools import phonebook_reader, phonebook_update

phonebook = read_phonebook()
try:
    while True:
        print("===============================================")
        command = input("Introduceti o comanda (w, l, r, u, d, s): ")
        if command == 'w':
            np = input("Introduce NP: ")
            phonebook[np] = {
                "tel": input("Numar de Telefon: "),
                "oras": input("Oras: "),
            }
        elif command == 'l':
            for i, person in enumerate(phonebook.keys()):
                print(f"{i + 1} - {person}")
        elif command == 'r':
            phonebook_reader(phonebook)
        elif command == 'u':
            phonebook_update(phonebook)
        elif command == 'd':
            try:
                name = input("Numele persoanei: ")
                phonebook[name]
            except KeyError:
                print("Aceasta persoana nu exista")
            else:
                del phonebook[name]
        elif command == 's':
            params = {
                1: "tel",
                2: "oras"
            }
            parameter = int(input("Alege parametru de cautare (1 - telefon, 2 - oras)"))
            value = input("care este valoarea parametrului? ")
            for k, v in phonebook.items():
                if value == v[params[parameter]]:
                    print(f"Persoana este {k}")
except KeyboardInterrupt:
    write_phonebook(phonebook)




