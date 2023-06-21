def add(a, b):
    print("Adunare")
    return a + b

def substract(a, b):
    return a - b 

def prod(a, b):
    return a * b

def div(a, b):
    return a / b

def calc(op, a, b, map):
    ops = {}
    for item in map:
        if item[0] == '_':
            continue
        ops[item] = eval(item)
    return ops[op](a, b) # mapping

# add.__call__(1, 2)
# print(add.__dir__()) 
# print(dir())

# x = 2
# test = 'ana'
# print(eval('x'))
# print(eval('test'))

print(calc("div", 1, 2, dir()))