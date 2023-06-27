
def world(func):
    print("Decorate me!")
    print(func.__name__)

    def inner():
        print("Inner")
        return func()
    
    print("Dupa inner")

    return inner

@world # decorator
def hello():
    print("Hello")

hello()