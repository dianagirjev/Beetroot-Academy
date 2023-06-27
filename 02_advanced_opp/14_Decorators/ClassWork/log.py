
def default(message):
    print("Message is " + message)

def logger(func):
    
    def inner_log(*args):
        result = func(*args)
        print(f"Se executa {func.__name__}, rezultat = {result}")
        return result

    return inner_log

def verify(func):
    
    def inner_ver(*args):
        result = func(*args)
        if result < 0:
            print("Mai mic decat 0")
            return False
        else:
            return True

    return inner_ver

@default("Test")
@verify
@logger
def add(a, b):
    return a + b

@logger
@verify
def sub(a, b):
    return a - b

s = sub(2, 4)
print(s)
a = add(2, 3)
print(a)