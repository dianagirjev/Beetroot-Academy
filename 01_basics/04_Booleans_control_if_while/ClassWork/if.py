x = None
x = bool(x)
print(x)
if not x: 
    print("x exista")
elif x > 5:
    print("x > 5")
else:
    print("x nu exista")

a = 314
if a != None: 
    print("a exista")
    if x > 5:
        print("a > 5")
    else:
        print("a nu exista")

if x is 33:
    print("x = 33")
# False, 0, [], {}, None, ""