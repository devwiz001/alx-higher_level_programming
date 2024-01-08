#!/usr/bin/python3
from __import__('0-add_integer') import add_integer

# Test cases
print(add_integer(1, 2))        # Should print 3
print(add_integer(100, -2))     # Should print 98
print(add_integer(2))           # Should print 2 (default b to 0)
print(add_integer(100.3, -2))    # Should print 98 (floats are cast to integers
try:
    print(add_integer(4, "School"))  # Should raise a TypeError
except Exception as e:
    print(e)
try:
    print(add_integer(None))   # Should raise a TypeError
except Exception as e:
    print(e)
