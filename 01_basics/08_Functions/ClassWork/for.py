def iterator(n):
    for i in range(n):
        if i % 2 != 0:
            continue
        print(i)

def iterator1(n):
    for i in range(n):
        print(f"Suntem la iteratia {i}")
        yield i + 11

def test():
    def _proprie():
        print("Functia interioara")
    _proprie()

if __name__ == "__main__":
    rezultat = iterator(5)
    print(f"Rezultat: {rezultat}")
    for k in iterator1(5):
        print(f"Se executa functia a {k} oara")
    test()