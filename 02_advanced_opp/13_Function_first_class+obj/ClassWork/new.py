def calc(operation, a, b):
    funcs = {
        "add": lambda a, b: a + b,
        "substract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
    }
    # print(funcs.keys())
    # test = lambda funcs, operation: operation not in funcs.keys()
    if lambda: operation not in funcs.keys():
        print("The operation is not defined")
        return
    return funcs[operation](a, b)

taskuri = [
    ("add", 1, 0),
    ("substract", 5, 4),
    ("multiply", 1, 1),
    ("add", -1, 2),
    ("divide", 2, 1),
]

for task in taskuri:
    print(task, calc(*task))