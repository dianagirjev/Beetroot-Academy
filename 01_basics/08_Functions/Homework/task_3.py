'''
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
(to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. 
Then return the sum or product of all the numbers in the arbitrary parameter. For example:

the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return 30
the call make_operation('*', 7, 6) should return 42  
'''

def make_operation(operator: str, *args):
    if operator == "+":
        sum = 0
        for arg in args:
            sum += arg
        return sum
    elif operator == "-":
        diff = 0
        for arg in args:
            diff -= arg
        return diff
    elif operator == "*":
        prod = 1
        for arg in args:
            prod *= arg
        return prod

if __name__ == "__main__":
    print(make_operation('+', 7, 7, 2))
    print(make_operation('-', 5, 5, -10, -20))
    print(make_operation('*', 7, 6))
    