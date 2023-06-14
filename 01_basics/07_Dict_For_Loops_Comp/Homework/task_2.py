'''Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above, then computes and returns the total price of stock.'''

def total_price_of_stock(dict_1: dict, dict_2: dict) -> dict:
    return {key: dict_1[key] * dict_2[key] for key in dict_1.keys()}

if __name__ == "__main__":
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    total = total_price_of_stock(stock, prices)
    print(total)