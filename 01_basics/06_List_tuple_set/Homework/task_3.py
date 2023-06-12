'''Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration.'''

first_list = list(range(1, 101))
new_list = []
i = 0
while i < len(first_list):
    if first_list[i] % 7 == 0 and first_list[i] % 5 != 0:
        new_list.append(first_list[i])
    i += 1
print(new_list)