import json

def write_phonebook(data):
    with open("phonebool.json", 'w') as f:
        f.write(json.dumps(data))

def read_phonebook() -> dict:
    try:
        with open("phonebool.json", 'r') as f:
            data = f.read()
        return json.loads(data)    
    except FileNotFoundError:
        return {}
    