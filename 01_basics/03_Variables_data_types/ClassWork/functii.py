print('functii.py:', __name__)
PI = 3.14

def functia_test():
    print("Functia TEST", PI)

print("Fisierul functii.py a fost procesat")


if __name__ == "__main__": # din alte fisiere aici e False
    functia_test()
    print("Am executat fisierul functii.py")