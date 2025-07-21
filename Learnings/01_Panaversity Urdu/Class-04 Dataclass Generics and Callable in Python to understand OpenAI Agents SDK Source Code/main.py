from dataclasses import dataclass, field
from typing import TypeVar, Generic, ClassVar, List

T = TypeVar("T")

@dataclass
class Stack(Generic[T]):
    items: List[T] = field(default_factory=list)  # You can ignore the warning here
    limit: ClassVar[int] = 10

    def push(self, item: T) -> None:
        if len(self.items) >= self.limit:
            raise OverflowError("Stack limit reached")
        self.items.append(item)

    def pop(self) -> T:
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()
