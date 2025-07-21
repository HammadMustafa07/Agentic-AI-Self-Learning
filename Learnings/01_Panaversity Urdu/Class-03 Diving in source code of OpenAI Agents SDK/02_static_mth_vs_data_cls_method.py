# ---

### ✅ **Static Method**

# * Doesn’t use **self** or **cls**
# * Belongs to the class but doesn’t touch class or object
# * Used for utility/helper functions
# * Call with: `ClassName.method()`

# ```python
@staticmethod
def greet():
    print("Hello!")
# ```

# ---

### ✅ **Class Method**

# * Uses **cls** (represents the class)
# * Can change class variables
# * Works on class level, not instance level
# * Call with: `ClassName.method()`

# ```python
@classmethod
def set_lang(cls, lang):
    cls.language = lang
# ```

# ---

# **💡 Summary:**

# > **Static = Helper**
# > **Class = Change Class Data**

# ---
