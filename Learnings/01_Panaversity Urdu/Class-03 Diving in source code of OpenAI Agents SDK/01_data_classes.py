# ✅ **Theory: What is a Dataclass?**

# * `dataclasses` is a module in Python (since Python 3.7).
# * It reduces the boilerplate code needed to create **classes that store data**.
# * With `@dataclass` decorator, Python automatically generates:

#   * `__init__` (constructor)
#   * `__repr__` (for printing)
#   * `__eq__` (for comparisons)
#   * `__hash__` (optional)

# ---

# ✅ **Why use Dataclasses instead of normal classes?**

# | Normal Class                  | Dataclass                     |
# | ----------------------------- | ----------------------------- |
# | You write everything manually | Python auto-generates for you |
# | Tedious for many attributes   | Cleaner & Shorter code        |
# | No built-in comparison        | Comes with comparison methods |

# ---

# ✅ **Simple Example Without Dataclass**


# ```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


p = Person("Hammad", 22)
print(p)
# ```

# ---

# ✅ **Same Example With Dataclass (Simple & Cleaner)**

# ```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p = Person("Hammad", 22)
print(p)  # Person(name='Hammad', age=22)
# ```

# ---

# ✅ **Features of Dataclasses with Example**

### 1️⃣ Default Values


# ```python
@dataclass
class Person:
    name: str
    age: int = 18  # Default age


p = Person("Hammad")
print(p)  # Person(name='Hammad', age=18)
# ```

# ---

### 2️⃣ Comparison Support


# ```python
@dataclass
class Person:
    name: str
    age: int


p1 = Person("Ali", 20)
p2 = Person("Ali", 20)
print(p1 == p2)  # True ✅
# ```

# ---

### 3️⃣ Frozen Dataclass (Immutable like namedtuple)


# ```python
@dataclass(frozen=True)
class Person:
    name: str
    age: int


p = Person("Sara", 25)
# p.age = 30  # ❌ Error because frozen=True
# ```

# ---

### 4️⃣ Post-Init Processing


# ```python
@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        print(f"{self.name} has been created with age {self.age}")


p = Person("Usman", 23)
# ```

# ---

# ✅ ✅ Real Life Example (Practical)

# ```python
from dataclasses import dataclass
from typing import List


@dataclass
class Product:
    id: int
    name: str
    price: float
    tags: List[str]


p = Product(1, "Laptop", 1500.0, ["Electronics", "Computers"])
print(p)
# ```

# ---

# ✅ Summary:

# * **Dataclasses** save you from writing common methods.
# * Best for **data-holding classes** (like DTOs or API Models).
# * Cleaner, maintainable, and readable code.
# * You can customize behavior easily.


# Sir Junaid Example of Code:

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class American:
    name: str
    age: int
    language: ClassVar[str] = "English" # using  ClassVar the 'language' will be treated as class variable not instanse variable 

    @staticmethod
    def country_lang():
        return American.language


hammad = American("Hammad Abro", 18)
print(hammad)
print(hammad.name)
print(hammad.age)
print(American.language)
