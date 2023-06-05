for i in range(10):
    print((i + 1) * '#')

for i in range(10):
    for j in range(i + 1):
        print('#', end = '')
    print()

for i in range(10):
    print(f'{(i + 1)}' * (i + 1))

for i in range(10):
    for j in range(i + 1):
        print(j, end = '')
    print()

line = "abcdefghij"
for i in line:
    print(i)