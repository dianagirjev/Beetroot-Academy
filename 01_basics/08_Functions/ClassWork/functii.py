# positional arguments (args)
# type definition
def test(x: int, text: str) -> str:
    print(f"x este: {x}")
    print(f"Textul este: {text}")
    temp = str(x) + text
    return temp

# keyword arguments (kwargs)
# define funtion(args, kwargs)
def test1(x: int, text: str ="llo") -> str:
    temp = text * x
    return temp

# unpacking operator *, **
def test2(*args) -> str:
    return args

def test2(*args) -> str:
    return args

def test3(x, *args) -> str:
    return args

def test4(*args, **kwargs) -> str:
    print("args: ", args)
    print("kwargs: ", kwargs)

def test5(x, *args, text = "Hello", **kwargs) -> str:
    print("args: ", args)
    print("kwargs: ", kwargs)

if __name__ == "__main__":
    result = test(9, "Hello")
    print(result)
    result1 = test1(9, "Hello")
    print(result1)
    result1_1 = test1(9)
    print(result1_1)
    result2 = test2(9, "Hello", 8, "hi")
    print(result2)
    result3 = test3(9, "Hello", 8, "hi")
    result4 = test4(9, "Hello", num = 8, text = "hi")
    result5 = test5(9, "Hello", num = 8, text = "hi")

    print("----------------------")
    lista = [1, 2, 3]
    print(lista, *lista,)
    print(lista[0], lista[1], lista[2])
    print("----------------------")

    dictionar = {
        'sep': "//", 
        'end': "]]",
    }
    print(1, 3, 5, **dictionar)

