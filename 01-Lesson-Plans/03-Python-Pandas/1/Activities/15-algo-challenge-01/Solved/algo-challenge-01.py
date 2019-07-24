# Import the `random` library.
import random

# Answer each question with the correct coding solution.

# QUESTION 1: Create a function called `number_guess` that takes in an integer as an argument.
# If the number is 42, print(true). If it isn't 42, print(false)
def number_guess(number):
    if number == 42:
        print(True)
    else:
        print(False)

# This code is to help you test your function
test_num = random.randint(40, 45)
print("Number " + test_num)
number_guess(test_num)

# QUESTION 2: Write a function that takes in a list of numbers. the function should print the smallest number in the given list
def find_smallest(list_param):
    minimum = 0

    for number in list_param:
        if minimum == 0:
            minimum = number
        elif number < minimum:
            minimum = number

    print(f"The smallest number in the list is {minimum}")

# This code is to help you test your function
nums = [10, 11, 3, 123, 54, 6, 67]
find_smallest(nums)

# QUESTION 3: Write a function which takes in a list of strings. The function should print the shortest string in the list.
def find_shortest(arr):


# This code is to help you test your function
strings = ["hey there", "yo", "a", "hello", "what up", "hello, my name is farley", "howdy"]
find_shortest(strings)

#QUESTION 4: Write a function that takes in three arguments: a high value, a low value and a list of numbers.
# The function should print a new list of numbers where none of the elements are less than the low value and none of the elements are greater than the high value
def filter_list(high, low, arr):
    print("replace this print statement with your code")

# This code is to help you test your function
down = 10
up = 20
arr = [2,5,99,15,23,18,11,21]

filter_list(up, down, arr)
