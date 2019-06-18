## Conditionally Yours Part II

In this activity, you will use the pseudocode you created in the previous activity to develop a program that recommends purchasing or selling stock based on a percent increase or decrease of its stock price.

### Background

Harold just returned from a meeting with his supervisor with a huge grin on his face. Thanks to your program, Harold was able to spend more time making decisions about which stocks to buy and sell; he now has the second highest profit earnings for the week. 

While on your lunch break together, you start posing ideas about how the program can be taken to the next level. Harold's ears perk up when you mention that you can add logic that identifies whether or not a stock should be purchased based on the percent increase or decrease in stock price. 

Harold knows that this would allow him to focus only on buying and selling; the program would handle all decision making and get him one step closer to securing the title of top trader for weeks to come. You begin considering the requirements for the enhanced program.

### Task

For this activity, work with a partner to create pseudocode for a program that will:

* Calculate percent increase or decrease for a stock and use conditional statements. (Formulas are provided below.)

* Determine whether or not a stock should be purchased or sold.

When the pseudocode is complete: 

* Implement the pseudocode in a Python file. 

* Test the logic of the program with Netflix stock prices. Yesterday at 4:00 PM, Netflix's stock price was $360.35. Right now, the stock price is $293.33. 

* Calculate the percent increase using the formulas below, and then print a message to the screen indicating if the stock should be bought or sold.

    * Increase = Current Price - Original Price

    * Percent Increase = Increase / Original x 100

### Instructions

Using the [starter-file](Unsolved/conditionally_yours.py) provided, complete the following steps:

1. Pseudocode your solution. 

2. Create variables for the following: 
 
    * `original_price`

    * `current_price`

    * `increase`

    * `percent_increase`

    * `recommendation`

    * `threshold_to_buy`

    * `threshold_to_purchase`

3. Derive `increase`. 

4. Derive `percent_increase`. 

5. Print `original_price`, `current_price`, and `percent_increase` to the screen with formatting. 

6. Compare `percent_increase` to `threshold`. 

7. Set `recommendation` to equal "buy" or "sell" based on your Step 5 evaluation. 

8. Print `recommendation`. 

### Challenge

Add a layer of sophistication to your program by creating a `balance` variable. This will serve as the amount of excess equity or money available in a portfolio. 

Create logic that will take into consideration `balance` when determining a recommendation. Only recommend to buy if `balance` is five times the amount of the stock's current price.

### Hint

Use a [format specifier](https://www.python.org/dev/peps/pep-0498/#format-specifiers) with the f-string.

---

© 2019 Trilogy Education Services
