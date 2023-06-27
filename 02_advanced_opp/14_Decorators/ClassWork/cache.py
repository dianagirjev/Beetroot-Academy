import functools

@functools.cache # creeaza dictionar in memorie
def transformer(text):
    result = text.upper()
    print(f"Text original: {text}, Text modificat {result}")
    return result

x = transformer("Hello World!")
print(x)
x = transformer("Hello World!")
print(x)
x = transformer("Test")
print(x)
x = transformer("Test")
print(x)
x = transformer("Hello World!")
print(x)