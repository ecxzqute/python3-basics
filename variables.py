# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# INDIVIDUAL VARIABLE ASSIGNMENT
x = 1           # int
y = 2.9         # float
name = "John"   # str    String
isTrue = True   # bool  Boolean

# MULTIPLE ASSIGNMENTS
x2, y2, name2, isTrue2 = (100, 2.345, "Kaycee", True)


# BASIC MATH
x3 = x + x2
y3 = y + y2

#print(x3, y3)
# OUTPUT >> 101 5.245

# CHECK VARIABLE TYPE
#print(type(x), type(y), type(name), type(isTrue))
# OUTPUT >> <class 'int'> <class 'float'> <class 'str'> <class 'bool'>

# TYPE CASTING
#x = str(x)
# print(type(x))
# OUTPUT >> <class 'str'>

# OUTPUT
# BASIC
print('hello')

# MULTIPLE
print(x, y, name, isTrue)
