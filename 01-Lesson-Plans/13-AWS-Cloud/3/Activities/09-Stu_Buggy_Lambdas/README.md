# Testing Lambdas

As you already know not everything is hunky-dory on coding, there are sometimes when bugs and errors appear to add some noise to your code. In this activity, you will test your own Lambda using the starting test event, next you will play a little with the partner next to you to provoke and find runtime errors.

## Instructions

### Create test events

1. Open the test event code provided by the instructor.

2. Create a new test event for your `convertUSD` Lambda by copying and pasting the code provided and recreate the `convertOkTest` test event on your AWS Lambda console.

3. Run the test and corroborate that the test succeeded.

4. Create a new test event that provides a negative value on the `usdAmount` slot. Name the test as `convertErrNegAmount`.

5. Run the test and analyze the results.

6. Create a new test event that provides a date of birth from the 19th century. Name the test as `convertOldAge`.

7. Run the test and analyze the results.

### Provoke runtime errors

1. Create a backup copy of your Lambda code.

2. Work in pairs with the partner next to you, now both of you will mess-up a little bit the Lambda's code.

3. Make two slight changes to the code of your partner, for example, rename a variable name, delete an imported library, drop a parenthesis, or rename a function name. Take note of what you changed!

4. Ask your partner to test the code and to find and fix the bugs you just introduced.

5. Comment between both of you about your experience debugging the Lambda's code.

6. Undo the changes or restore your Lambda function from your backup copy.
