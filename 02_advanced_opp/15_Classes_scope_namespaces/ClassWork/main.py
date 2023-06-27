import types
from typing import Any


class Calculator:
    def __init__(self, a, b):
        print("Initializam clasa")
        self.a = a
        self.b = b
    def __eq__(self, __value: object) -> bool:
        print("Self:", self.a, self.b)
        print("Other:", __value.a, __value.b)
        if self.a == __value.a:
            return True
        return False
    # def __str__(self) -> str:
    #     return f"String Clasa de tip Calculator {self.a}, {self.b}"
    def __repr__(self) -> str:
        return f"Reprezentare Clasa de tip Calculator {self.a}, {self.b}"
    def __or__(self, __value: Any) -> UnionType:
        pass
    def add(self):
        result = self.a + self.b
        print(f"Add: {result}")
    def sub(self, a, b):
        return a + b
    

x = Calculator(2, 3)
y = Calculator(2, 2)
x.add()
print(x == y)
print(x.__eq__(y))
print(str(x))
print(x)

int()
