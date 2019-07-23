# Return to functions

By including a return value, we can have functions build upon each other. We can use those return values elsewhere in our code. Otherwise, we can't refer to values created within functions outside of them.

## Instructions

Perform the following:

1. Define a function "warble" that takes in a string as an argument,

2. Adds " arglebargle" to the end of it, and returns the result.

3. Print the result of calling your "warble" function with the argument "hello".

4. Define a function "wibble" that takes a string as an argument,

5. Prints the argument, prepends "wibbly " to the argument, and returns the result

6. Print the result of calling your "wibble" function with the argument "bibbly"

7. Define a function "print_sum" that takes in two numbers as arguments and prints the sum of those two numbers.

8. Define a function "return_sum" that takes in two numbers as arguments and returns the sum of those two numbers

9. Using either "return_sum" and no mathematical operators, define a function "triple_sum" that takes in 3 arguments and returns the sum of those 3 numbers.

10. Define a function "dance_party" that takes in a string as an argument, that prints "dance!", updates the string from calling "wibble" function with that argument, updates the string from calling "warble" function with that argument, returns the updated string

11. Print the result of calling your "dance_party" function with your name as the argument

```
# Should result in:
# dance!
# MyName
# wibbly MyName arglebargle
```
