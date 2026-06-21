# Class Method
**A class method in Python is a method that operates on the class itself, not on an individual object (instance). It receives the class (cls) as its first argument instead of self.**

You define a class method using the @classmethod decorator.

**Key Points**
1.First argument is cls (the class).
2.Can access and modify class variables.
3.Does not require creating an object to be called.
4.Often used for factory methods (methods that create objects in special ways).

# Use of class Method as alternative constructor.
**A class method receives the class itself (cls) as the first argument instead of an instance (self).
Because of this, it can:**

1.Create and return new instances of the class.
2.Provide multiple ways to create objects, improving readability and flexibility.
3.Act like extra constructors besides the normal __init__.
4.You typically mark them with @classmethod.

# dir()
Purpose: Lists all valid attributes of an object.

Shows methods, variables, and inherited attributes.
Useful for exploration and debugging.

# __ dict__
Purpose: Stores an object’s writable attributes in a dictionary.

Only shows attributes defined directly on the object.
Not all objects have a __dict__ (e.g., built‑in types often do not).
# help
help() provides detailed documentation about an object, module, function, or class.
