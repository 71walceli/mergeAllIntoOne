"""
This file was created to understand why module or external value does not
change. 

Hypothesis: module value cannot change because of the following reasons:

1. A variable is always passed  as an object reference.

2. Primitives such as integers cannot be changed.

https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
"""

value = -1

def setValue(data):
  value = data

setValue(1)
print(value)
