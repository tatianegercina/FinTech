# Password Strength Checker

We're going to be creating a validation function for checking the strength of a password. The important part of this activity is the logic behind the checker, so you are given the html and the rest of the javascript. You should not have to modify any part of the code given to you. Just work within the area allotted to you to fulfill the objectives.

* Password strengths are as follows:

  * A very weak password contains equal to or fewer than 6 characters and consists only of numbers
  * A very strong password has more than 6 characters and consists of at least one number, at least one letter
  * Anything other type of password is of average strength

* Your password strength checker function should only return one output per password given

* Your function should return the greatest strength level that the password satisfied from weak all the way up to strong with average being in the middle of the two.

## Instructions

Open the [starter file](Unsolved/algo-challenge-02.py) and perform the following:

1. Import the `string` library.

2. Use the `string` library to initialize string variables representing all valid letters and digits, respectively.

3. Define a function called `check_strength` that takes in a string parameter called `password`.

    1. Create two boolean variables called `contains_number` and `contains_letter`. Set them to False.

    2. Initialize a `count` variable and set it to 0.

    3. Loop through each character in the `password` and increment the `count` variable by 1 for each character.

    4. Create an if-else statement that loops through each character in `password` and updates `contains_number` or `contains_letter` to True.

4. Create an if-else statement for the following:

    1. If `password` contains equal to or fewer than 6 characters and consists only of numbers, print "Your password is too weak."

    2. Else if `password` contains more than 6 characters and consists of at least one number and at least one letter, print "Your password is a strong password".

    3. Else, print "Your password is of average strength."

5. Declare a variable as `user_input_password` with an input stating "Input your password: ".

6. Call the check_strength function with the `user_input_password`.

7. Execute the Python program.

    1. Open your terminal/git bash.

    2. From within the terminal/git bash run `source activate PythonData` to activate your virtual environment.

    3. Navigate to the directory that is holding this code drill.

    4. Run `python filename.py` to test your output.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
