# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Ja'
age = 31

# CONCATENATION
print("Hi, I am " + name + " and I am " + str(age) + " years old.")

# String Formatting
# POSITIONAL ARGUMENTS
print('Hi, My name is {name} and I am {age} years old'.format(
    name=name, age=age))

# F-STRING FORMATTING
# Works with python v3.6+
print(f"Hi, My name is {name} and I am {age} years old")


# String Methods
s = "hEllo World"

# Capitalizes the first character of string
print(s.capitalize())
# Converts given string to uppercase
print(s.upper())
# Converts string to lower-case for caseless comparison
print(s.casefold())
# Gets the number as to where the first character or word is located within the string
print(s.count("World"))
# Determines whether the given string starts with the given parameter
print(s.startswith("hello"))
# Determines whether the given string ends with the given parameter
print(s.endswith("d"))
# Locates the given parameter's position within the string
print(s.find("r"))
# Splits the given string according to the given delimeter, "space" is used by default
print(s.split())
# Checks whether the given string is Alpha-numeric
print(s.isalnum())
# Checks whether the given string is Alphabetic, results to false as string contains white space
print(s.isalpha())
# Checks whether the given string is Numeric
print(s.isnumeric())
