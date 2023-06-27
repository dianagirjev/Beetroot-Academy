'''Write a function called oops that explicitly raises an IndexError exception when called. 
Then write another function that calls oops inside a try/except state­ment to catch the error. 
What happens if you change oops to raise KeyError instead of IndexError?'''


def oops(numbers: list):
    for i in range(len(numbers)):
        numbers[i] = numbers[i + 1]
        print(numbers[i])

my_list = list(range(10))
# The lines below are generation IndexError
# oops(my_list)

try:
    oops(my_list)
except IndexError:
    print("Be carreful, you are trying to access an invalid position")

try:
    oops(my_list)
except KeyError:
    print("Be carreful, you are trying to access an invalid position")