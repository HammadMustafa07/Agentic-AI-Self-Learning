
# ---

### ✅ **Class Level**

# * Shared by **all objects**
# * Same for every instance
# * Defined with **ClassName.variable** or **ClassVar**
# * Changed by **class methods**

# ```python
class MyClass:
    language = "English"  # Class level
# ```

# ---

# ### ✅ **Instance Level**

# * **Unique for each object**
# * Defined inside ****init**** with **self**
# * Changed by **instance methods**

# ```python
class MyClass:
    def __init__(self, name):
        self.name = name  # Instance level
# ```

# ---

# **💡 Summary:**

# > **Class Level = Shared by All**
# > **Instance Level = Unique per Object**

# ---

