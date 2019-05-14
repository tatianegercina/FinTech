# E-Commerce Traffic

In this activity, you will parse through a text file and sum the total number of customers and the count of days (assume each line is equal to a day's worth of customers) in the text file to calculate the daily average of customer traffic for your e-commerce business.

## Instructions

* Using the starter file provided, walk through the following steps.

  * Import the Pathlib library.

  * Set the file path for the `customer_traffic.txt` data file.

  * Initialize the `customer_total` and `day_count` variables that will hold the total and count of the number in the text file, respectively.

  * Use the file path pointing to the `customer_traffic.txt` data file to open the file as an object.

  * Iterate over each line in the file and cumulatively add to the `customer_total` and `day_count` variables. You will need to convert the number from the text file as an int to perform numerical calculations.

  * Write the contents of the `customer_total`, `day_count`, and `daily_average` to an `output.txt` file:

  * Your `output.txt` file should look similar to the following code block:

    ```
    The total and count of the numbers in the text file are 4945 and 100, respectively. The average is 49.45.
    ```

## Hints

* You already know a lot of the concepts needed to complete this activity! Remember your variables, for loops, and formatted strings. Just take it step-by-step and don't let file paths and reading/writing from/to a file throw you off!