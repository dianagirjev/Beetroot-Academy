'''
Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys. Make the function 
print out the values of the dictionary to make sure that it works as intended.'''

def make_country(name: str, capital: str) -> None:
    country_dict = {}
    country_dict['name'] = name
    country_dict['capital'] = capital
    print(country_dict)

if __name__ == "__main__":
    make_country("Moldova", "Chisinau")