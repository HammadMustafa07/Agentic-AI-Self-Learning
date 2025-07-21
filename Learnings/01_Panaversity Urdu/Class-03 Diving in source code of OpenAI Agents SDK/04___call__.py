class Greeter:
    def __call__(self, name):
        print(f"Hello, {name}!")

g = Greeter()
g("Hammad")  # ✅ Acts like a function: prints "Hello, Hammad!"


# __call__() is a special method in Python that makes an instance behave like a function.

# When you write obj(), Python runs obj.__call__().

# It’s useful for making callable classes, often in decorators, agents, or factories.
