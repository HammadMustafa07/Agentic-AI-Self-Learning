from dataclasses import dataclass
from typing import Callable

@dataclass
class Calculator:
    operation: Callable[[int, int], int]

    def __call__(self, a: int, b: int) -> int:
        return self.operation(a, b)

# Example Usage
def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

calc = Calculator(operation=add)
print(calc(10, 4))  # Output: 6
