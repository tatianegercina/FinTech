# Making a Calculator

This activity is going to combine everything we've covered today along with some tools from yesterday. We're going to be making a very basic arithmetic calculator that takes in user input and returns the result of the calculation. This is a challenging activity, so remember that there's always the hints folder for you to lean on.

## Instructions

1. Declare a variable called user_input_list and set it to an empty list for now

2. Create a string of all the valid_inputs for our validation logic to check against user's input

3. Define a function that takes in user_input_list to check the operator's sign

    1. if the operator is a '+' sign, return the value of the first number added to the second number

    2. else if the operator is a '-' sign, return the value of the first number subtracted from the second number

    3. else if the operator is a '*' sign, return the value of the first number multiplied by the second number

    4. else if the operator is a '/' sign, return the value of the first number divided by the second number

## Hints

* This calculator should only take numbers, `+`, `-`, `*` and the `/` key as valid inputs

* It is highly recommended you use functions to section out your logic and validate each of the user's input so that they are unable to add multiple operators.
