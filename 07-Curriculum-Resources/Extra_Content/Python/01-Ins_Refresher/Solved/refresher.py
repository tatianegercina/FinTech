# -*- coding: utf-8 -*-
"""
Python refresher activity.

This script showcases basic operations in Python such as variables,
conditionals, lists, dicts, for loops, and functions.
"""

# Conditionals
x = 30

if x > 10:
    print(f"{x} is greater than 10")
else:
    print(f"{x} is less than 10")

# Lists
fruits = ["apple", "pear", "banana"]

# Loop over list
for fruit in fruits:
    print(fruit)

# Dicts
car = {
    "make": "Nissan",
    "model": "Maxima",
    "type": "Sedan"
}

# Loop over key-value pairs
for key, value in car.items():
    print(f"{key}, {value}")

# Define a function
def squared(number):
    """
    Calculates the squared value of a given number

    Args:
        number (int): The number to be squared.
    Returns:
        The squared value of the given number
    """

    result = number * number
    return result

# Call the function
print(squared(5))
