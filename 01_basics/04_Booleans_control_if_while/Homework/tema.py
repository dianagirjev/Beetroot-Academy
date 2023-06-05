# TASK 1
my_string = input("Sample String: ")
if len(my_string) >= 2:
    print("Expected Result: " + my_string[0:2] + my_string[-2] + my_string[-1])
else:
    print("Expected Result: " + "")


# TASK 2
phone_number = input("Please insert a phone number: ")
count = 0
for i in phone_number:
    try:
        digit = int(i)
    except ValueError:
        print("Your phone number is invalid, it should contain only numerical characters.")
        break
    count += 1
if count == len(phone_number):
    print("Your phone number contains only numerical characters.")
    if len(phone_number) == 10:
        print("And your phone number has a valid length, so CONGRATS IT IS VALID.")    
    else:
        print("But your phone number has an invalid length, so SORRY IT IS INVALID.")

# TASK 3
my_name = "diana"
input_name = input("Please insert your name: ")
print(my_name == input_name.lower())


