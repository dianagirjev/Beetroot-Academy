'''The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers'''

import random

length = 10
i = 0
random_list = []
while i < length:
    random_list.append(random.randint(0, 100))
    i += 1
print(f"The largest number from list {random_list} is {max(random_list)}")