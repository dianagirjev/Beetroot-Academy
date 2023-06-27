def calc(operation, a, b):
    funcs = {
        "add": lambda a, b: a + b,
        "substract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
    }
    print(funcs.keys())
    test = lambda f, o: o not in f.keys()
    return funcs[operation](a, b) if test(funcs, operation) else "The operation is not defined"
    # if test(funcs, operation):
    #     print("The operation is not defined")
    #     return
    # return funcs[operation](a, b)

taskuri = [
    ("add", 1, 0),
    ("substract", 5, 4),
    ("multiply", 1, 1),
    ("add", -1, 2),
    ("divide", 2, 1),
]

for task in taskuri:
    print(task, calc(*task))

print(calc.__code__.co_varnames)