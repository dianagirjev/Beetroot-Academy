import requests, time, csv, os
from datetime import datetime

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_data(timeout = 1):
    response = requests.get(url).json()
    price = response["bpi"]["USD"]["rate_float"]
    date = datetime.now()
    return {
        "price": price,
        "date": date,
        "timeout": timeout,
        }

def harvest(timeout: int):
    file_name = str(datetime.now().date()) + ".csv"
    data = read_data(file_name)
    try:
        while True:
            print("TIMEOUT", len(data))
            time.sleep(timeout)
            data.append(get_data(timeout))
    except KeyboardInterrupt:
        write_data(file_name, data)

def exchange(target, amount):
    price = get_data()["price"]

    if target == "USD":
        print(amount / price, "BTC")
    elif target == "BTC":
        print(amount * price, "USD")

def read_data(file_name):
    data = []
    try:
        with open(f"data/{file_name}", "r") as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
    except (FileNotFoundError, IndexError):
        print("Fisierul nu a fost gasit")
    else: # se executa dupa try
        temp = []
        for item in data:
            print(item)
            temp.append({
            "price": item[0],
            "date": item[1],
            "timeout": item[2],
            })
        data = temp
    finally: # se executa mereu
        return data
    
def write_data(file_name: str, data: list):
    os.chdir("data")
    print(f"We are writing in {file_name} file.")
    with open(file_name, "w", newline="") as f:
        csv_writer = csv.writer(f)
        for item in data:
            csv_writer.writerow(item.values())
    os.chdir("..")