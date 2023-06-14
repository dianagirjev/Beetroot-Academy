def phonebook_reader(phonebook: dict):
    name = input("Numele persoanei: ")   
    try:
        print(f"Tel - {phonebook[name]['tel']}")
        print(f"Oras - {phonebook[name]['oras']}")
    except KeyError:
        print("Nu am gasit aceasta persoana, insa avem cateva sugestii: ")
        index = 0
        for person in phonebook.keys():
            index += 1
            if name in person:
                print(f"{index} - {person}")

def phonebook_update(phonebook: dict):
    try:
        person = phonebook[input("Numele persoanei: ")]
    except KeyError:
        print("Aceasta persoana nu exista")
    else:
        for k, v in person.items():
            new_value = input(f"Doresti sa modifici: {k} - {v}: ")
            if new_value:
                person.update({k: new_value})