1. ## Object Initialization & Representation
Method	                                         Purpose
__init__(self, ...)	               Constructor — called when an object is created.
__del__(self)	                    Destructor — called when an object is about to be destroyed.
__str__(self)	                    Defines human-readable string representation (print(obj)).
__repr__(self)	                    Defines official string representation (for debugging).
2. ## Operator Overloading
Method	                 Operator
__add__(self, other)	    +
__sub__(self, other)	    -
__mul__(self, other)	    *
__truediv__(self, other)	/
__floordiv__(self, other)	//
__mod__(self, other)	    %
__pow__(self, other)	    **
__eq__(self, other)	        ==
__lt__(self, other)     	<
__le__(self, other)	        <=
__gt__(self, other)	        >
__ge__(self, other)	        >=
3. ## Attribute Access
Method	                                        Purpose
__getattr__(self, name)	               Called when an attribute is not found.
__setattr__(self, name, value)	       Called when setting an attribute.
__delattr__(self, name)	               Called when deleting an attribute.
4. ## Container Emulation
Method	                                      Purpose
__len__(self)	                    Returns length (len(obj)).
__getitem__(self, key)	            Access item (obj[key]).
__setitem__(self, key, value)	    Set item (obj[key] = value).
__delitem__(self, key)	            Delete item (del obj[key]).
__iter__(self)	                   Returns iterator (for x in obj).
__contains__(self, item)	        Membership test (item in obj)