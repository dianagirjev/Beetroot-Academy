class Terminal:
    def __init__(self):
        self.last_ticket = 1
        self.clients = []
        self.current_client = {}
        self.operators = [{
            "name": "Ion",
            "specialitate": "C"
        }]


    def create(self, type:str):
        # C - consultanta, S - suport
        client = {
            "type": type,
            "number": self.last_ticket,
            "code": f'{type}{self.last_ticket}'
        }
        print(f"Client nou: {client['code']}")
        self.clients.append(client)
        # FIFO first in first out pop(0)
        # LIFO first in first out pop(-1)

        self.last_ticket += 1
        return client
    
    def add_operator(self, name, spec):
        operator = {
            "name": name,
            "specialitate": spec
        }
        self.operators.append(operator)
        print(f"Lista de operator: {self.operators}")

    def extract(self, name):
        if len(self.clients) == 0:
            return False
        # spec = ""
        # for item in self.operators:
        #     if name in item["name"]:
        #         spec = item["specialitate"]
        spec = [item["specialitate"] for item in self.operators if name == item["name"]][0]
        print(f"Toti clientii sunt: {self.clients}")
        for index, item in enumerate(self.clients):
            if spec in item["code"]:
                self.current_client = self.clients.pop(index)
        print(f"Clientul curent: {self.current_client['code']}, Ramasi: {len(self.clients)} index: {index}")
        return self.current_client


atm = Terminal()
atm.create('C')
atm.create('S')
atm.create('C')
atm.add_operator("Ana", "S")
atm.extract("Ana")
atm.extract("Ion")
atm.extract("Ion")