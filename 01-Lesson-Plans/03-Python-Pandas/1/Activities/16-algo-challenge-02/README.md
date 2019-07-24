# Password Strength Checker

We're going to be creating a validation function for checking the strength of a password. The important part of this activity is the logic behind the checker, so you are given the html and the rest of the javascript. You should not have to modify any part of the code given to you. Just work within the area allotted to you to fulfill the objectives.

* Password strengths are as follows:

  * A very weak password contains equal to or fewer than 6 characters and consists only of numbers
  * A very strong password has more than 6 characters and consists of at least one number, at least one letter
  * Anything other type of password is of average strength

* Your password strength checker function should only return one output per password given

* Your function should return the greatest strength level that the password satisfied from weak all the way up to strong with average being in the middle of the two.

## Instructions

1. Import the `string` library.

2. Define a function called `check_strength` that takes in a string parameter called `password`.

3. Create a boolean variable called `weak_password` that acts as a check if fewer than 6 characters are present.

4. Declare and set two boolean variables called `contains_number` and `contains_letter` as False.

5. Create an if-else statement that loops through each character in `password` and updates `contains_number` or `contains_letter` to True.

6. Create an if statement for the following:

    1. If `weak_password` is True, print "Your password is too weak."

    2. Else if weak_password is False and `contains_letter` is True, print "Your password is of average strength".

    3. Else print "Your password is a strong password."

7. Declare a variable as user_input_password with an input stating "Please enter a password."

8. Initiate the check_strength function with the user_input_password
