# without TypeVar, the type checker cannot reliably infer or enforce the types, and it will treat your inputs/outputs 
# as Any.

# With generics, type checkers like MyPy, Pylance, or Pyright can catch them before running.

# I write once with generics — my Type Manager handles the rest.


# from typing import TypeVar

# T = TypeVar("T")

# def generic_first_element(items: list[T]):
#     return items[0]


# nums = [1, 2, 3, 4]
# strs = ["Hammad", "Abro", "rough"]

# num_result = generic_first_element(nums)
# strs_result = generic_first_element(strs)

# print(num_result)
# print(strs_result)



# with sequence

from typing import TypeVar, Sequence

T = TypeVar("T")

# def generic_first_element(items: list[T]): # it is only accepting list but with sequence 
def generic_first_element(items: Sequence[T]): # it will accept everything that is in sequence bot no for set bcoz no indexing,
    return items[0]


print(generic_first_element(["Hammad Abro", "Moiz Abro"]))

