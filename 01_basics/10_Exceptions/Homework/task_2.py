'''
Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
and then returns the value of squared a divided by b, construct a try-except block which raises 
an exception if the two values given by the input function were not numbers, and if value b was zero 
(cannot divide by zero). 
'''

def calc(a, b):
    try:
        return a * a / b
    except ZeroDivisionError:
        print("Unfortunately you can't divide by 0.")

try:
    a = int(input("Please insert a valid number for a: "))
except ValueError:
    print("Given value for a is not a number.")

try:
    b = int(input("Please insert a valid number for b (not 0): "))
except ValueError:
    print("Given value for b is not a number.")

try:
    print(f"The result is: {calc(a, b)}")
except NameError:
    print("You should try again to run the code.")