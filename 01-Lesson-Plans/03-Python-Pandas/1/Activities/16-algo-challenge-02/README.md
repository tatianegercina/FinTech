# Password Strength Checker

In this activity, you will create a validation function for checking the strength of a password. The focus of this activity is the logic behind the checker. You will be given the HTML and the rest of the JavaScript; you should not have to modify any part of the code given to you.

Password strengths are as follows:

  * A _very weak_ password contains 6 or fewer characters consisting only of numbers.

  * A _very strong_ password has more than 6 characters consisting of at least one number and at least one letter.

  * Any other type of password is of average strength.

## Instructions

Open the [starter file](Unsolved/algo-challenge-02.py) and perform the following:

1. Import the `string` library.

2. Use the `string` library to initialize string variables representing all valid letters and digits, respectively.

3. Define a function called `check_strength` that takes in a string parameter called `password`.

    * Create two Boolean variables called `contains_number` and `contains_letter`. Set them to `False`.

    * Initialize a `count` variable and set it to 0.

    * Loop through each character in the `password` and increment the `count` variable by 1 for each character.

    * Create an if-else statement that loops through each character in `password` and updates `contains_number` or `contains_letter` to `True`.

4. Create an if-else statement for the following:

    * If `password` contains 6 or fewer characters and consists only of numbers, print "Your password is too weak".

    * Else if `password` contains more than 6 characters and consists of at least one number and at least one letter, print "Your password is a strong password".

    * Else, print "Your password is of average strength".

5. Declare a variable as `user_input_password` with an input stating "Input your password:"

6. Call the `check_strength` function with `user_input_password`.


---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
