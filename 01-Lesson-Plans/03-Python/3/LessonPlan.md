## 3.3 Lesson Plan: Functions and Files (10:00 AM)

### Overview

In today's class, students will focus on financial functions, file IO, and working with CSVs. This lesson will be an opportunity for students to practice basic financial analysis principles in the context of both internal (hard-coded) and external (file IO) manipulation of data.

### Class Objectives

By the end of class, students will be able to:

* Recap previous Python concepts and implementations: variables, conditionals, lists/dicts, for loops, and functions
* Define what Time Value of Money is and how it relates to Net Present Value via discounted future values/cash flows
* Perform basic financial analysis from user-defined financial functions (NPV)
* Import additional Python libraries, both standard and custom
* Read/Write text files
* Recognize what tabular data is and its form
* Read/Write CSV files

- - -

### Instructor Notes

* Be mindful of pacing when reviewing the financial concepts of Time Value of Money, Zero-Coupon Bonds, and Net Present Value introduced in today's class; it's important that students understand Python's basic operations and how to implement them, but they should also begin to develop mental frameworks for solving financial use cases using such concepts. Therefore, they will need to have a thorough comprehension of what the financial concepts mean and why they are used.

* This course will include a diverse array of students with varying backgrounds in Finance. As a result, try to find the proper balance of walking through the financial sections of this class with care for the newcomers, but also make it interesting enough as a refresher for the veterans.

* For those students that may still be struggling with the pace and concepts of Python, make sure TAs are circulating and giving extra attention to the students who need it. If class is moving ahead of schedule there may be extra time for students to review or revisit concepts to help those that are struggling.

* Students may need reminders to activate their conda environment to access libraries like Numpy. Another common error is that their conda environment may not have included the anaconda tools, so students may need to run `conda install anaconda` or `conda install numpy` if they have issues importing the Numpy library.

* Make sure that students are properly setting their file paths when reading in files. Specifically, emphasize the difference between relative and absolute paths, and ensure that their paths are properly set. 

* The Pathlib library allows students to ignore the differences between Windows OS `\` black-slashes and Unix-based OS `/` forward-slashes in regards to file paths; however, students should still be aware of these differences in case they are not able to access the Pathlib library.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

- - -

### 1. Instructor Do: Welcome Class (5 mins)

**Files:**

* [Welcome-Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit?usp=sharing)

Welcome students back and explain that today is going to be really fun and interesting as we begin tying Python implementation with financial concepts and use cases! Use the slide deck to provide a quick overview of the day's agenda as well as the topics previously covered so far. 

Quickly re-cap the following topics:

* What are variables?

  > Variables are reserved memory allocations that are used to store information that can be referenced and manipulated later.

  ```python
  # Creates a variable with a string "Frankfurter"
  title = "Frankfurter"
  years = 23
  hourly_wage = 65.40
  expert_status = True
  ```

* What are conditionals?

  > Conditionals are if-else statements that make true or false comparisons which determine corresponding actions for either scenario.

  ```python
  # Declare variables and values for evaluation
  x = 1
  y = 10

  # Checks if one value is equal to another
  if x == 1:
      print("x is equal to 1")
  ```

  ```
  x is equal to 1
  ```

* What are lists?

  > Lists are mutable (changeable) and ordered data structures that hold data of a single type.

  ```python
  # Create a list of Pokemon
  print("Creating a list of Pokemon...")
  pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Garydos", "Dragonite", "Onyx"]
  print(pokemon)
  ```

  ```
  ['Pikachu', 'Charizard', 'Bulbasaur', 'Garydos', 'Dragonite', 'Onyx']
  ```

* What are dicts?

  > Dicts are mutable (changeable) and unordered data structures that holds key-value pairs of potentially varying data types.

  ```python
  # Initialize a dictionary
  trading_pnl = {
      "title": "Trading Log",
      "03-18-2019": -224,
      "03-19-2019": 352,
      "03-20-2019": 252,
      "03-21-2019": 354,
      "03-22-2019": -544,
      "03-23-2019": -650,
      "03-24-2019": 56,
      "03-25-2019": 123,
      "03-26-2019": -43,
      "03-27-2019": 254,
      "03-28-2019": 325,
      "03-29-2019": -123,
      "03-30-2019": 47,
      "03-31-2019": 321,
      "04-01-2019": 123,
      "04-02-2019": 133,
      "04-03-2019": -151,
      "04-04-2019": 613,
      "04-05-2019": 232,
      "04-06-2019": -311
  }
  ```

  ```
  {'title': 'Trading Log', '03-18-2019': -224, '03-19-2019': 352, '03-20-2019': 252, '03-21-2019': 354, '03-22-2019': -544, '03-23-2019': -650, '03-24-2019': 56, '03-25-2019': 123, '03-26-2019': -43, '03-27-2019': 254, '03-28-2019': 325, '03-29-2019': -123, '03-30-2019': 47, '03-31-2019': 321, '04-01-2019': 123, '04-02-2019': 133, '04-03-2019': -151, '04-04-2019': 613, '04-05-2019': 232, '04-06-2019': -311}
  ```

* What are for loops?

  > For loops are blocks of code that allow you to repeat a process a fixed number of times.

  ```python
  # Loop through a range of numbers (0 through 4)
  for x in range(5):
      print(x)
  ```

  ```
  0
  1
  2
  3
  4
  ```

* What are functions?

  > Functions are callable blocks of reusable code that perform an action.

  ```python
  # Define a main function that accepts a string argument
  def main(stock_ticker):
      print(stock_ticker + " is booming right now!")

  stock_ticker = "SBUX"
  main(stock_ticker)
  ```

  ```
  SBUX is booming right now!
  ```

* How to traverse nested objects?

  > Specify the index for each level of iteration

  ```python
  # List of Dicts
  ceo_nested_dict = [
      {
          "name": "Warren Buffet",
          "age": 88,
          "occupation": "CEO of Berkshire Hathaway"
      },
      {
          "name": "Jeff Bezos",
          "age": 55,
          "occupation": "CEO of Amazon"
      },
      {
          "name": "Harry Markowitz",
          "age": 91,
          "occupation": "Professor of Finance"
      }
  ]

  print(ceo_nested_dict[0]['occupation'])
  ```

  ```
  CEO of Berkshire Hathaway
  ```

- - -

### 2. Instructor Do: Refresher (10 mins)

**Files:**

* [refresher.py](Activities/01-Ins_Refresher/Solved/refresher.py)

Open the refresher.py file and ask students to guide you through the following examples:

* Creating a conditional that prints out `x is greater than 10` or `x is less than 10`

* Creating a list named `fruits`, initialize with `apple`, `pear`, `banana`

* Looping through and printing each fruit in `fruits`

* Creating a dict named `car` and adding in `make`, `model`, `type` as keys and their corresponding values

* Looping through and printing each key-value pair in `car`

* Creating a function `squared()` that calculates the square of a `number` input parameter

- - -

### 3. Students Do: Refresher (15 mins)

In this activity, students will act as analysts who categorize customers based on their revenue and assign a business tier: Platinum, Gold, Silver, or Bronze. Depending on the assigned business tier, different phrases are generated for each customer. 

This use case can be extremely practical as it allows firms to target specific cohorts within their customer base, either by directing personalized messages as is the case with this activity or even going so far as distributing e-mail promotion codes to specific cohorts.


**Files:**

* [Starter-Code](Activities/02-Stu_Refresher/Unsolved/marketing.py)

**Instructions**

* [README.md](Activities/02-Stu_Refresher/README.md)

### 4. Instructor Do: Review Refresher (5 mins)

**Files:**

* [Solution](Activities/02-Stu_Refresher/Solved/marketing.py)

Open the solution and explain the following:

* The `customers` list is a nested list of dictionaries which represents a collection of customer records, with each record containing `first_name`, `last_name`, and `revenue` key-value pairs.

  ```python
  # List of dicts
  customers = [
      { "first_name": "Tom", "last_name": "Bell", "revenue": 0 },
      { "first_name": "Maggie", "last_name": "Johnson", "revenue": 1032 },
      { "first_name": "John", "last_name": "Spectre", "revenue": 2543 },
      { "first_name": "Susy", "last_name": "Simmons", "revenue": 5322 }
  ]
  ```

* The `create_greeting()` function takes in three parameters `first_name`, `last_name` and `revenue` and returns the dynamically generated `greeting`.

* An if-else statement is also used to create the conditional logic that determines the business tier for each customer based on their revenue. Thereby defining the appropriate `greeting` to generate.

  ```python
  # Define a function that accepts a customer first_name, last_name, and revenue and returns a custom greeting using the full name.
  # Use these ranges to determine the business tier (and corresponding message) for each customer.
  #   Platinum = 3001+
  #   Gold = 2001-3000
  #   Silver = 1001-2000
  #   Bronze = 0-1000
  def create_greeting(first_name, last_name, revenue):
  """Creates a customer greeting based on revenue status.

  Args:
      first_name (str): The first name of the customer.
      last_name (str): The last name of the customer.
      revenue (int): The revenue of the customer.

  Returns:
      A customized greeting string.
  """

  if revenue > 3000:
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a platinum member."
  elif (revenue > 2000 and revenue <= 3000):
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a gold member."
  elif (revenue > 1000 and revenue <= 2000):
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a silver member."
  elif (revenue >= 0  and revenue <= 1000):
      greeting = f"Hi {first_name} {last_name}! Thank you for your business of ${revenue}! You are a bronze member."

  return greeting
  ```

* Since each customer in the list is a dict datatype, students will have to call the `first_name`, `last_name`, and `revenue` keys of each customer to pass it into the `create_greeting()` function.

  ```python
  # Loop through the list of customers and use your function to print custom greetings for each customer.
  for customer in customers:
      greeting = create_greeting(customer['first_name'], customer['last_name'], customer['revenue'])
      print(greeting)
  ```

Ask for any remaining questions before moving on.

- - -

### 5. Instructor Do: Time Value of Money (10 mins)

Now that students are warmed up, this activity will demonstrate some core financial calculations in Python. Use the slides provided to explain the concepts related to the time value of money. Make sure students understand that these calculations are fundamental to financial analysis and that they will get to actually write the code for each of these formulas!

Some students with more in-depth backgrounds in Finance may already know what TVM is. If so, engage the class by asking students if they can help explain what TVM is and how it's used!

**Files:**

* [Welcome-Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit?usp=sharing)

* [time_value.py](Activities/03-Ins_Time_Value_of_Money/Solved/time_value.py)

Navigate to the Unit 3.3 slides and use slides 10-16 to discuss the concepts around the time value of money. Be sure to highlight the following:

* The time value of money describes the additional value that is created through receiving money today compared to receiving money at a later date as money today can continue to grow with interest.

* The time value of money can change due to factors such as interest rate, compounding periods, and the length of time.

* The formula for the future value of money can be reversed to obtain the present value given a future amount. This allows you to properly evaluate the value of a future cash flow or asset in terms of what it's worth today.

Open `time_value.py` and explain the following:

* The purpose of a function is to allow us to re-use blocks of code. With the `calculate_future_value` function, the logic required to calculate the future value of money is all contained within the function. The function can be called over and over with new inputs and a future value is calculated for each of those inputs. In programming, this concept of code reuse is called DRY (**D**on't **R**epeat **Y**ourself).

* Functions don't always have to be user-defined. There are many built-in Python functions already available for use. For example, list objects have multiple functions such as `append()`, `len()`, and `remove()`; dict objects have multiple functions such as `keys()` and `items()`.

* In previous examples, functions are called by supplying values for each of the parameters. However, functions can also be called using variables to pass in the values for the parameters. The parameters for `calculate_future_value` are `present_value`, `interest_rate`, `compounding_periods`, and `years`.

* Functions often return one or more values. The value that the function returns can be assigned to a variable for use in other parts of the code. In this example, `future_value` is assigned the value that the `calculate_future_value` function returns.

- - -

### 6. Students Do: Zero-Coupon Bonds (25 mins)

In this activity, students will use the concept of TVM to discount the future value of a zero-coupon bond to determine its present value, and compare the present value to its current selling price and decide whether or not to purchase the bond.

Encourage students to work in pairs for this activity. Motivate students to help each other by explaining that the best way to learn is to teach, so taking the time to help their neighbor will really reinforce the concepts.

**Files:**

* [Starter-Code](Activities/04-Stu_Time_Value_of_Money/Unsolved/zero_coupon_bonds.py)

**Instructions**

* [README.md](Activities/04-Stu_Time_Value_of_Money/README.md)

### 7. Instructor Do: Review Zero-Coupon Bonds (5 mins)

**Files:**

* [Solution](Activities/04-Stu_Time_Value_of_Money/Solved/zero_coupon_bonds.py)

Open the solution and explain the process of valuing a zero-coupon bond:

* The `present_value` function allows us to value the promised future value of the bond upon its maturity. Because the `present_value` formula is merely a manipulation of the `future_value` formula in the previous exercise, its parameters are generally equivalent as well:

  * `future_value` - The 'face value' or 'maturity value' of the bond. The lump sum distributed at the end of the duration of the bond.
  * `interest_rate` - The rate at which we discount the future value or maturity value over the duration of the bond.
  * `compounding_periods` - The compounding periods (assumed 1 for bonds)
  * `years` - The number of years representing the duration of the bond

* After calculating the present value of the bond, now we can compare it to its market price. Based on whether or not the bond is selling at a `discount` or `premium` in relation to its present value should determine the purchasing decision of that bond.

Ask for any remaining questions before moving on.

- - -

### 8. Instructor Do: Imports (10 mins)

Explain that this activity is really exciting because it showcases the power of imports in Python. Use the following motivational points to help students understand how powerful imports can be:

> Imports are a really powerful concept and is especially useful as it allows developers to share and use code that others have written. It's a way to "stand on the shoulder of giants" and leverage existing tools and libraries to build even more sophisticated programs. Instead of building everything from scratch each time, you can use tools that have been built by other brilliant people to enhance your own code and build even greater programs!

**Files:**

* [NPV Slides 25-27](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit#slide=id.g57bb043f18_0_4663)

* [imports.py](Activities/05-Ins_Imports/Solved/imports.py)

Explain that we will be importing some really cool financial functions to calculate things like net present value. Use the slides to talk about the theory behind NPV. 

Walk through the demo and highlight the following:

* Imports allow us to call upon other Python programs and gain access to their functions and variables.

* There are two ways of performing imports:

  1. Importing the additional Python program as a reference object

    ```python
    # Call the print_hello() function via a reference to the imported module functions.py
    import functions
    functions.print_hello()
    ```

    ```
    hello!
    ```

  2. Importing the specific attribute (ex. function, variable) of the additional Python program into the namespace of the current Python program

    ```python
    # Call the print_hello() function imported directly from functions.py
    from functions import print_hello
    print_hello()
    ```

    ```
    hello!
    ```

* What is NumPy?

  > NumPy is a Python library provides fast I/O on multidimensional or nested array objects. Among other things, NumPy can be used as a scientific computing or financial analysis tool.

* It isn't necessary to re-invent the wheel! Leveraging code from other developers can make life easy; The built-in NPV function from the NumPy library makes calculating NPV values simple.

  ```python
  # Import the NumPy library
  import numpy

  # Initialize variables
  interest_rate = .1
  cash_flows = [-1000, 400, 400, 400, 400]

  # Call the NPV function from the NumPy library
  net_present_value = numpy.npv(interest_rate, cash_flows)
  print(f"NPV = {net_present_value}")
  ```

- - -

### 9. Students Do: Net Present Value (15 mins)

**Files:**

* [Starter-Code](Activities/06-Stu_Imports/Unsolved/Core/net_present_value_core.py)

**Instructions**

* [README.md](Activities/06-Stu_Imports/README.md)

### 10. Instructor Do: Review Net Present Value (5 mins)

**Files:**

* [Solution](Activities/06-Stu_Imports/Solved/Core/net_present_value_core.py)

Open the solution and explain the process of performing financial analysis using Net Present Value (NPV):

* NumPy's built-in NPV function makes it easy to calculate NPV values.

* Each list of cash flows represents a project proposal; the first element of each list represents the project's initial investment, while the remaining elements of the list represent the cash flows as a result of the initial investment.

* Resolving the return values of the NPV functions as key-value pairs let's us easily retrieve the NPV value of an associated scenario, for example, when looking to determine the scenario associated with the calculated max NPV value.

Ask for any remaining questions before moving on.

- - -

### 11. Instructor Do: File_IO (10 mins)

Data will not (and should not) always be hard-coded within a Python file. Often times, data is saved within a file and needs to be accessed externally, so as to perform some kind of manipulation or analysis. File pathing is extremely important when attempting to access files saved within a folder structure. Luckily, Python natively supports the input and output of files and the Pathlib library makes file pathing easy.

**Files:**

* [file_io.py](Activities/07-Ins_File_IO/Solved/file_io.py)

First, start by opening the terminal (or git-bash for Windows) and navigate to the project folder. Run `pwd` to show where the current folder is located.

Next, open a finder window (Mac) or Explorer window (Windows) and show the students the location of the script files and the resource file. It is important they they understand the absolute and relative locations of the project folder and the files before explaining how to utilize `Pathlib` and its associated functions.

Walk through the demo and highlight the following:

* The `Path.cwd()` allows us to check our *current working directory* from where the Python program is executing.

* Windows and Mac operating systems treat file paths differently; Windows uses `\` back slashes and Mac uses `/` forward slashes as file path separators.

* Absolute paths are the fully qualified path to a specified file, while relative paths are paths that take into account the current working directory of the executing program.

  * For example, the following pair of code blocks target the same file:

    * Absolute Path

      ```python
      from pathlib import Path

      # Absolute path to the file
      absolute_filepath = Path("/Users/trilogyed/Desktop/File_IO/Resources/file.txt")

      with open(absolute_filepath, 'r') as file:
          print(file.read())
      ```

      ```
      I'm a text file header!
      Line 1
      Line 2
      Line 3
      ```

    * Relative Path

      ```python
      from pathlib import Path

      # Current working directory is "/Users/trilogyed/Desktop/File_IO/"
      cwd = Path.cwd()
      print(f"Current Working Directory: {cwd}")
      print()

      # Relative path to the file, equivalent to "{cwd}/Resources/file.txt"
      relative_filepath = Path("Resources/file.txt")

      with open(relative_filepath, 'r') as file:
          print(file.read())
      ```

      ```
      Current Working Directory: /Users/trilogyed/Desktop/File_IO/

      I'm a text file header!
      Line 1
      Line 2
      Line 3
      ```

* The `..` keyword means "go one level up" from the current working directory

  * For example, examine the following folder structure:  

    ```
    /Users
      /trilogyed
        /File_IO
          /Resources
            file.txt
          /Solved
            file_io.py
    ```

  * If executing code from `file_io.py`, the relative path `../Resources/file.txt` can be used to target `file.txt`.

  * This is because `file_io.py` resides at `/Users/trilogyed/File_IO/Solved/file_io.py`. The `..` keyword goes one level up from `/Users/trilogyed/File_IO/Solved/` to `/Users/trilogyed/File_IO/` and descends into `Resources/file.txt` to hit the file. 

* The Pathlib library allows us to set filepaths irrespective of the operating system (OS)

  ```python
  filepath = Path("../Resources/input.txt")
  ```

* The `with open(filepath, 'r') as file:` operation opens a file residing at a specified `filepath` as a file object.

* We can read in the entirety of the text file by calling upon the `read()` function on the text file object `file`

* Files can be read line-by-line using a loop. This will read every line of text until the end of the file.

  ```python
  line_num = 1
  for line in file:
      print(f"line {line_num}: {line}")
      line_num += 1
  ```

* After a file is read and reaches the last line, no more lines can be read for that file object. That is why if we run both methods of reading in the file at one time, only the preceding file read operation (all lines at once) will output, as the subsequent file read operation (line by line) will have already reached the end of the file by this point.

* Writing to a text file is very similar to reading in a text file; the main difference is we use the `write()` function vs the `read()` function.

- - -

### 12. Students Do: File Manipulation (15 mins)

**Files:**

* [Starter-Code](Activities/08-Stu_File_IO/Unsolved/ecommerce_traffic.py)

**Instructions**

* [README.md](Activities/08-Stu_File_IO/README.md)

### 13. Instructor Do: Review File Manipulation (5 mins)

**Files:**

* [Solution](Activities/08-Stu_File_IO/Solved/ecommerce_traffic.py)

Open the solution and explain the following:

* It is important to understand from where a program is executing. Knowing the current working directory facilitates the use of relative paths and can be a good diagnosis as to why students may get potential `file not found` errors. The `Path.cwd()` function allows us to see the current working directory.

  ```python
  # Check the current directory where the Python program is executing from
  print(f"Current Working Directory: {Path.cwd()}")
  ```

* Reading text from files will first be interpreted as strings. In order to do any numerical calculations, we'll have to convert the values from string datatypes to int or float datatypes. The `int()` datatype conversion function converts a string to an integer.

  ```python
  # Open the file in "read" mode ('r') and store the contents in the variable 'file'
  with open(file, 'r') as file:
      # Parse the file line by line
      for line in file:

          # Convert the number in the text file from string to int (allows for numerical calculations)
          number = int(line)

          # Sum the total and count of the numbers in the text file
          customer_total += number
          day_count += 1
  ```

* The operation `num_total += number` is equivalent to the more verbose operation `num_total = num_total + number`.

* When writing data to a text file, the content will have to be string datatypes. Therefore any data being written to a text file that is not of the string datatype will need to be converted.

Ask for any remaining questions before moving on.

- - -

### 14. BREAK (40 mins)

- - -

### 15. Instructor Do: Tabular Data (5 mins)

**Files:**

* [Welcome-Slides](https://docs.google.com/presentation/d/1OUvK19EjgPd3WQ7ioMV5Gb5tuNkbXuNSvsrpjkFhnss/edit?usp=sharing)

Walk through slides 28-30. Explain that tabular data is data in "table" format where rows, columns, and values for each row-column intersection exist. A simple example is an excel spreadsheet, where columns are headers, rows are records, and values are cells located at the intersection of each row and column.

- - -

### 16. Instructor Do: CSV Reader (5 mins)

**Files:**

* [csv_reader.py](Activities/09-Ins_CSV_Reader/Solved/csv_reader.py)

Walk through the demo and highlight the following:

* CSV stands for *Comma Separated Values* and follows a tabular form in which the first line is usually a header containing column names, while each line is a row containing values that intersect with each row-column pair.

* The csv module makes it easier to access csv data by doing the heavy lifting of parsing and making data easily accessible. The csv module includes a `reader()` function that parses csv data by a separator or delimiter, and creates a `row` list object that contains the values for every row in the csv data.

  ```python
  csvreader = csv.reader(csvfile, delimiter=',')
  
  # Read each row of data after the 
  for row in csvreader:
      # Print the row
      print(row)
      # Set salary variable equal to the value in the 4th column of each row
      salary = int(row[3])
      # Append the row salary value to the list of salaries
      salaries.append(salary)
  ```

* Writing to a csv file is very similar syntactically to reading a csv file. We use the `writerow()` function to write a list or row of data to the output csv file.

  ```python
  # Open the output path as a file object
  with open(output_path, 'w') as csvfile:
      # Set the file object as a csvwriter object
      csvwriter = csv.writer(csvfile, delimiter=',')
      # Write the header to the output file
      csvwriter.writerow(header)
      # Write the list of metrics to the output file
      csvwriter.writerow(metrics)
  ```

- - -

### 17. Students Do: Sales Analysis (15 mins)

**Files:**

* [sales_analysis.py](Activities/10-Stu_CSV_Reader/Unsolved/Core/sales_analysis_core.py)

**Instructions**

* [README.md](Activities/10-Stu_CSV_Reader/README.md)

### 18. Instructor Do: Review Sales Analysis (5 mins)

**Files:**

* [sales_analysis.py](Activities/10-Stu_CSV_Reader/Solved/Core/sales_analysis_core.py)

Open the solution and explain the following:

* Python's csv module parses csv data and creates `row` list objects, making it easier to access specific column values for each row.
 
* Reading in data from CSVs is interpreted as strings, in order to perform numerical calculations, we'll need to convert the strings into ints (or floats).

  ```python
  for row in csvreader:
      # Print the row
      print(row)

      # Set the 'name', 'count', and 'revenue' variables for better readability, convert strings to ints for numerical calculations
      name = row[0]
      count = int(row[1])
      revenue = int(row[2])

      # Calculate the average and round to the nearest 2 decimal places
      average = round(revenue / count, 2)
  ```

* Adding data to each row of the input CSV data is as easy as appending to the `row` list object

  ```python
  # Append the average to the row
  row.append(average)
  ```

* The `csvwriter.writerow()` takes in lists and outputs the data to a csv file using the specified `delimiter`.

  ```python
  # Open the output path as a file and pass into the 'csv.writer()' function
  # Set the delimiter/separater as a ','
  with open(output_path, 'w') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',')

  # Loop through the list of records and write every record to the output csv file
  for record in records:
      csvwriter.writerow(record)
  ```

* The use of the `analysis` dictionary combined with if-else conditionals allows us to group and aggregate data by making checks to see if a particular key exists. If the key does not exist, then we add the key and intialize the nested dictionary value containing the `count` and `revenue` key-value pairs.

    ```python
    # If name is not already in the analysis dict, initialize the nested dict
    # Else continue to add to the existing key and nested key-value pairs
  if name not in analysis.keys():
      analysis[name] = {
          "count": count,
          "revenue": revenue
      }
  else:
      analysis[name]['count'] += count
      analysis[name]['revenue'] += revenue
  ```

* It's possible to write nested dicts to a csv by first adding the contents to a list and then using `csvwriter.writerow()`.

  ```python
  # Open the output path as a file and pass into the 'csv.writer()' function
  # Set the delimiter/separater as a ','
  with open(aggregate_path, 'w') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=',')

      # Write the header as the first row
      csvwriter.writerow(header)

      # Loop over every key in analysis and write the associated key (name) and nested key-value pairs (metrics)
      for name in analysis:
          csvwriter.writerow([name, analysis[name]['count'], analysis[name]['revenue'], round(analysis[name]['revenue'] / analysis[name]['count'], 2)])
  ```

- - -

### 19. Instructor Do: Structured Office Hours (35 mins)

Please use the entire office hours time to review questions with the students.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### End Class

- - -

Trilogy Education Services © 2019. All Rights Reserved.
