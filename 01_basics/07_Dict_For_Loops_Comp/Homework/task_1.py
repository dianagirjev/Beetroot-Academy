'''Make a program that has some sentence (a string) on input and returns a dict containing 
all unique words as keys and the number of occurrences as values. '''

# input_string = input("Please insert a sentence here: ")
input_string = "Ana are mere banane . Ana nu are pere ."
resulted_list = input_string.split(" ")
print(resulted_list)
resulted_dict = {key: resulted_list.count(key) for key in resulted_list}
print(resulted_dict)

dict_2 = {}
for item in resulted_list:
    if item not in dict_2:
        dict_2[item] = resulted_list.count(item)

print(dict_2)