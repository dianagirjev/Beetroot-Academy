def test():
    print("hello")
    def world():
        print("world")
    return world

temp = test # functia o putem atribui la o variabila
temp()

print(temp())
print(temp()())