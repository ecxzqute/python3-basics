# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "grapes", "pears"]

# Creating a list via constructor
numbers2 = list((1, 2, 3, 4, 5))


# print(numbers)
# print(numbers2)

# Printing lists specific value
print(fruits[2])

# Getting the length of a list
print(len(fruits))

# Appending item to a list
fruits.append("banana")
print(fruits)

# Inserting item to a specific position in a list
fruits.insert(1, "strawberries")

# Replacing an item in a list
fruits[0] = "mango"

# Remove item from a list
fruits.remove("oranges")
print(fruits)

# Remove item by position
fruits.pop(1)
print(fruits)


# Reverse list items
fruits.reverse()
print(fruits)


# Sort list items
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)
