## 3.2 Lesson Plan: Data Structures and Functions (6:30 PM)

### Overview

Today’s class will focus on list and dict data structures and how to iterate over them. Students will work with nested lists and dicts, as well as utilize and define reusable code blocks known as functions. This lesson will introduce more advanced Python operations, such as accessing and manipulating data from data structures, and showcase the efficiency of working with functions.

### Class Objectives

By the end of class, students will be able to:

* Recap previous Python concepts and implementations: variables, conditionals, and for loops.
* Identify the differences between homogeneous (same data type) and heterogeneous data (different data type). 
* Access and manipulate data within list and dict objects using index-based elements and key-value pairs, respectively. 
* Iterate over lists and dicts. 
* Visualize and iterate over nested lists and dicts. 
* Define and call functions. 

- - -

### Instructor Notes

* This lesson will introduce students to more advanced Python concepts. Be mindful of pacing, as students will need a solid understanding of Python basics before they can formulate application behaviors and implement them in Python. 

* Be sure to explain the differences between accessing data in lists vs. data in dicts: data in lists is represented as a set of elements accessed via a zero-based index, while data in dicts are represented as a set of keys associated with values.

* Nested lists and dicts may take some time to work through, as this topic requires a multi-level perspective. Remember to showcase the output of nested loops; it will be much easier for students to grasp the concept when they can visualize the result.

* Some students may wonder about the benefits of using functions; it's because it's easier and less redundant to call upon a block of code that defines a specific programmatic action as a command rather than having to copy and paste the same block of code multiple times to achieve the same effect.

* Make sure TAs circulate the classroom to provide help for students who may still be struggling with Python. If class is moving ahead of schedule, use the extra time to revisit concepts to help bring students up to speed. 

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx). 

- - -

### 1. Instructor Do: Welcome and Review (5 min)

**File:** [Slides](https://docs.google.com/presentation/d/1cFrN2LIjmDC2UdVQMYIY-_peQc4mty4R63lvyJbqn1I/edit?usp=sharing)

Welcome students back to class. Open the slideshow and review today’s class objectives/agenda. 

Navigate to the refresher slide and do a quick review of the previous lesson by posing the following questions to the class: 

* What is a terminal?

  **Answer:** A terminal is a command line interface (CLI) that allows a user to execute and automate commands without the need for a graphical user interface (GUI).

* What are variables?

  **Answer:** Variables are reserved memory allocations that are used to store information that can be referenced and manipulated later.

* What are conditionals?

  **Answer:** Conditionals are if-else statements that make true or false comparisons which determine corresponding actions for either scenario.

* What are for loops?

  **Answer:** For loops are blocks of code that allow you to repeat a process a fixed number of times.

* What is pseudocoding?

  **Answer:** Pseudocoding is the process of devising the specific requirements and behaviors of an application in human-readable terms.

Ask if there are any questions before moving on. 

- - -

### 2. Instructor Do: Lists (10 min)

**Files:**

* [Slides](https://docs.google.com/presentation/d/1cFrN2LIjmDC2UdVQMYIY-_peQc4mty4R63lvyJbqn1I/edit?usp=sharing)

* [lists.py](Activities/01-Ins_Lists/Solved/lists.py)

**Note:** Keep discussion informal at the beginning of the lecture. Data structures are a complex topic, especially as students begin to learn the conceptual difference between variables, data types, and data structures.

To introduce the topic of lists, remind students of what they have been doing so far. 

* Students have worked with variables, conditionals, and for loops. 

* They have been able to automate some processes, but each program they've run has required some degree of hard-coding one-dimensional values, which can be boring.

Tell students that in this class, they will begin to store data as collections and process values iteratively. The world of automation is banging at their doors! 

Introduce lists with the following analogy: 

* If Python commands and operations are like workers assigned specific tasks to do, lists are like the conveyor belt in the assembly line. 

* As the conveyor belt iterates, an item on the belt is processed. 

* Just as the Industrial Revolution changed the lives of workers, using lists will streamline data processing and programming and eliminate redundant tasks. 

Use an example from the previous lesson to illustrate the limitations of supplying only one value to a variable. 

* Think back to the activity from the previous lesson where a cheerleading program was created for a company's intranet. In the program, a variable `cheer` was declared, and a word was provided for the program to cheer (i.e., Python).

* The program would have been even better if it allowed for a series of words to be cheered; this would have made the cheers more dynamic and interesting. 

Review the definition of lists: 

* A **list** is a Python data structure that allows multiple values to be stored inside of it. 

* List values can be retrieved, appended, removed, and iterated.

Open the cheerleading program in JupyterLab. Run the code to show students how using a list changes the output of the program. 

    ```python
    # Create a variable named cheer
    cheer = ["Python", "FinTech","Trilogy","Money"]

    # Below strings can be used to add fun
    cheer_symbol = "*\O/*"
    cheer_symbol_2 = "ヘ( ^o^)ノ＼(^_^ )"

    # Loop through string
    for i in range(len(cheer)):
        for x in cheer[i]:
            #Print each letter with a cheer
            print("Give me a " + x + "!")
            print(x + "!")

        # Print excitement to screen
        print("\nWhat does that spell?!")
        print(cheer[i] + "!\nWoohoo! Go " + cheer[i] + "!")
        print(cheer_symbol * 3)
        print(cheer_symbol_2)
        print()
    ```

Open the slideshow and use slides 5-7 to discuss basic concepts related to lists. Be sure to highlight the following:

* A list in Python is a collection of ordered elements or values, separated by commas, with an index of "zero" for the first element.

  ```python
  color_hats = ["green", "blue", "red", "purple"]
  ```

* Lists commonly hold values of the same data type.

  ```python
  my_favorite_things = ["Chocolate", "beach", "mountains", "breakfast_tacos"]
  ```

* Lists can contain values with different data types.

  ```python
  my_favorite_things = ["Chocolate", 9, "beach", 10, "breakfast_tacos"]
  ```

* Lists can even hold other lists!

  ```python
  my_favorite_things = ["Chocolate", 9, ["beach", "mountains"], "breakfast_tacos"]
  ```

Open the `lists.py` file and explain the following:

* Create a list object `employees` by using a syntax combination of comma-separated values contained in a single set of square brackets. 

  ```python
  # Create a list of Pokemon
  print("Creating a list of Pokemon...")
  pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Garydos", "Dragonite", "Onyx"]
  print(pokemon)
  print()
  ```

  ```
  Creating a list of Pokemon...
  ['Pikachu', 'Charizard', 'Bulbasaur', 'Garydos', 'Dragonite', 'Onyx']
  ```

* Use an index number to specify a particular element of a list.

  ```python
  # Print element at index 2
  print("Printing the third Pokemon...")
  print(pokemon[2])
  print()
  ```

  ```
  Printing the third Pokemon...
  Bulbasaur
  ```

* Use `[start:end]` slice notation to specify elements from the starting index to the ending index. 

  ```python
  # Print elements from index 2 to index 5
  print("Printing 3rd Pokemon to the 5th Pokemon...")
  print(pokemon[2:5])
  print()
  ```

  ```
  Printing 3rd Pokemon to the 5th Pokemon...
  ['Bulbasaur', 'Garydos', 'Dragonite']
  ```

* Use `[start:]` slice notation to specify elements from the starting index to the end of the list. 

  ```python
  # Print elements from index 3 to the end of the list
  print("Printing every Pokemon after the first three...")
  print(pokemon[3:])
  print()
  ```

  ```
  Printing every Pokemon after the first three...
  ['Garydos', 'Dragonite', 'Onyx']
  ```

* Use `[:end]` slice notation to specify elements from the beginning of the list to the ending index. 

  ```python
  # Print elements from beginning of list to index 3
  print("Printing every Pokemon up to the first three...")
  print(pokemon[:3])
  print()
  ```

  ```
  Printing every Pokemon up to the first three...
  ['Pikachu', 'Charizard', 'Bulbasaur']
  ```

* Use `[start:end:step]` slice notation to specify the optional step parameter that defines the increment sizes. 

  ```python
  # Print every other element
  print("Printing every other Pokemon")
  print(pokemon[::2])
  print()
  ```

  ```
  Printing every other Pokemon
  ['Pikachu', 'Bulbasaur', 'Dragonite']
  ```

* The index `-1` can be used to target the last element of a list. 

  ```python
  # Print the last element of the list
  print("Printing the last Pokemon on the list...")
  last_pokemon = pokemon[-1]
  print(last_pokemon)
  print()
  ```

  ```
  Printing the last Pokemon on the list...
  Onyx
  ```

* Modifying a particular element in the list can be done by targeting the element at its specified index and reassigning the value. 

  ```python
  # Change a specified element within the list at the given index
  print("Changing Pokemon name 'Pikachu' to 'Raichu'...")
  pokemon[0] = "Raichu"
  print(pokemon)
  print()
  ```

  ```
  Changing Pokemon name 'Pikachu' to 'Raichu'...
  ['Raichu', 'Charizard', 'Bulbasaur', 'Garydos', 'Dragonite', 'Onyx']
  ```

* The `append()` function adds elements to the end of a list. 

  ```python
  # Add an element to the end of the list
  print("Adding a new Pokemon to the end of the list...")
  pokemon.append("Magikarp")
  print(pokemon)
  print()
  ```

  ```
  Adding a new Pokemon to the end of the list...
  ['Raichu', 'Charizard', 'Bulbasaur', 'Garydos', 'Dragonite', 'Onyx', 'Magikarp']
  ```

* The `len()` function determines how many elements are in the list. 

  ```python
  # Calculate the number of elements within the list
  print("Calculating the number of Pokemon...")
  print(len(pokemon))
  print()
  ```

  ```
  Calculating the number of Pokemon...
  5
  ```

If time permits, cover these additional topics:

* The `index()` function finds the index of a particular element name. 

  ```python
  # Find the index of the particular element name
  print("Determining the order of Pokemon 'Garydos'...")
  print(pokemon)
  print(pokemon.index("Garydos"))
  print()
  ```

  ```
  Determining the order of Pokemon 'Garydos'...
  ['Pikachu', 'Charizard', 'Bulbasaur', 'Garydos', 'Dragonite', 'Onyx']
  3
  ```

* The `remove()` function deletes a particular element by name. 

  ```python
  # Remove an element from the list based on the given element name
  print("Removing employee 'Magikarp'...")
  pokemon.remove("Magikarp")
  print(pokemon)
  print()
  ```

  ```
  Removing employee 'Magikarp'...
  ['Raichu', 'Charizard', 'Bulbasaur', 'Garydos', 'Dragonite', 'Onyx']
  ```

* The `pop()` function deletes a particular element by index. 

  ```python
  # Remove an element from the list based on the given index
  print("Removing employee 'Bulbasaur' based off of its index")
  bulbasaur_index = pokemon.index("Bulbasaur")
  pokemon.pop(bulbasaur_index)
  print(pokemon)
  print()
  ```

  ```
  Removing employee 'Bulbasaur' based off of its index
  ['Raichu', 'Charizard', 'Garydos', 'Dragonite', 'Onyx']
  ```

Reiterate that lists are a powerful data container in Python that can do so much more than just store data. 

Send out a link to the [Python documentation]((https://docs.python.org/3/tutorial/datastructures.html)) that students can use to reference more list functions. 

- - -

### 3. Student Do: Sugar, Flour, Butter! (15 min)

In this activity, students will work with lists to maintain a grocery list. They will create lists, append to lists, retrieve `n` items from a list, and retrieve values by indexes. The goal of this activity is to get students comfortable with using lists to store and track data so that they can later apply this knowledge to financial information. 

**File:** [starter-code](Activities/02-Stu_Lists/Unsolved/Core/grocery_list_core.py)

**Instructions:** [README.md](Activities/02-Stu_Lists/README.md)

### 4. Instructor Do: Review Sugar, Flour, Butter! (5 min)

**File:** [solution](Activities/02-Stu_Lists/Solved/Core/grocery_list_core.py)

Open the solution file and explain the following:

* The `[start:end:step]` slice notation targets elements of defined slices from the grocery list. 

  ```python
  # Find the first two items on the list
  print("What are my first two items on the list?")
  print(groceries[:2])
  print()

  # Find the last four items on the list
  print("What are all my items except for the first two on the list?")
  print(groceries[2:])
  print()

  # Find every other item on the list, starting from the second item
  print("What is every other item on the list, starting from the second item?")
  print(groceries[1::2])
  print()
  ```

  ```
  What are my first two items on the list?
  ['water', 'butter']

  What are all my items except for the first two on the list?
  ['eggs', 'apples', 'cinnamon', 'sugar', 'milk']

  What are is every other item on the list, starting from the second item?
  ['butter', 'apples', 'sugar']
  ```

* The `append()` function adds more items to the end of the grocery list. 

  ```python
  # Add an element to the end of the list
  print("Oops, forgot to add flour...")
  groceries.append("flour")
  print(groceries)
  ```

  ```
  Oops, forgot to add flour...
  ['water', 'butter', 'eggs', 'apples', 'cinnamon', 'sugar', 'milk', 'flour']
  ```

* The `index()` function finds the index of a particular item on the grocery list. 

  ```python
  # Find the index of the particular element name
  print("Where is 'apples' in the list index?")
  print(groceries)
  print(groceries.index("apples"))
  ```

  ```
  Where is 'apples' in the list index?
  ['water', 'butter', 'eggs', 'apples', 'cinnamon', 'sugar', 'milk', 'flour']
  3
  ```

* The `len()` function determines how many items are on the grocery list. 

  ```python
  # Calculate how many items you have in the list
  print("How many items do I have on my shopping list?")
  print(len(groceries))
  print()
  ```

  ```
  How many items do I have on my shopping list?
  8
  ```

* The `remove()` function removes an item from the grocery list by a specified name. 

  ```python
  # Remove an element from the list based on the given element name
  print("Picked up some sugar!")
  groceries.remove("sugar")
  print(groceries)
  ```

  ```
  Picked up some sugar!
  ['water', 'butter', 'eggs', 'gala apples', 'cinnamon', 'milk', 'flour']
  ```

* The `pop()` function removes an item from the grocery list by a specified index. 

  ```python
  # Remove an element from the list based on the given index
  print("Actually, I don't need water. I have some at home...")
  water_index = groceries.index("water")
  groceries.pop(water_index)
  print(groceries)
  ```

  ```
  Actually, I don't need water. I have some at home...
  ['butter', 'eggs', 'gala apples', 'cinnamon', 'milk', 'flour']
  ```

* The index `-1` targets the last item on the grocery list. 

  ```python
  # Remove the last element of the list
  print("I'm going to pick up the last item on the list...")
  groceries.pop(-1)
  print(groceries)
  ```

  ```
  I'm going to pick up the last item on the list...
  ['butter', 'eggs', 'gala apples', 'cinnamon', 'milk']
  ```

Ask if there are any questions before moving on.

- - -

### 5. Instructor Do: Iterate Lists (5 min)

**File:** [iterate_lists.py](Activities/03-Ins_Iterate_Lists/Solved/iterate_lists.py)

Introduce the concept of iterating through a list in Python: 

* Iterating through lists is a powerful programming tool that will allow you to automate financial analysis and pipelines that assess collections of data points. 

* Learning how to iterate lists and execute operations against each element in a list puts you one step closer to creating programs that are completely automated.

Open `iterate_lists.py` and cover the following points:

* In Python, certain objects are considered **iterators**, or iterable objects. Iterators are objects that can be iterated on, meaning that you can loop through each value. Lists are iterators because you can loop through every element in the list.

* In this example, each value of the `tips` list can be accessed using the `tip` variable. 

    * During each loop, the next value in the list is assigned to `tip` and can be used within the loop. 
    
    * When there are no more values, the loop ends.

* The `+=` operator is used to cumulatively sum up numerical values when looping through a list. The following code snippets are operationally equivalent.

  ```python
  # Cumulatively sum up the total and count of tips
  total += tip
  ```

  ```python
  # Cumulatively sum up the total and count of tips
  total = total + tip
  ```

* Conditionals can simulate common functions, such as calculating the `minimum` and `maximum` metrics within a list of values.

  ```python
  # Logic to determine minimum and maximum values
  if minimum == 0:
      minimum = tip
  elif tip < minimum:
      minimum = tip
  elif tip > maximum:
      maximum = tip
  ```

Ask if there are any questions before moving on. 

- - -

### 6. Student Do: Trading Log (15 min)

In this activity, students will use lists to create a trading log that tracks profits and losses for each market day of the month. They will iterate over the list to calculate the highest and lowest profit and loss days. The goal of this activity is to use for loops and lists in order to track multiple data points. 

**File:** [trading_log.py](Activities/04-Stu_Iterate_Lists/Unsolved/trading_log.py)

**Instructions:** [README.md](Activities/04-Stu_Iterate_Lists/README.md)

### 7. Instructor Do: Review Trading Log (5 min)

**File:** [trading_log.py](Activities/04-Stu_Iterate_Lists/Solved/trading_log.py)

Open the solution and explain the following:

* The first step in the PNL calculation is to determine the total profits and losses as well as the count of trading days. 

* Both of these can be calculated by looping through the `trading_pnl` list and updating the `total` and `count` with each new piece of data from the list.

  ```python
  for day_pnl in trading_pnl:

      # Cumulatively sum up the total profits/losses and count of trading days
      total += day_pnl
      count += 1
  ```

* The `total += day_pnl` is equivalent to the operation `total = total + day_pnl`, which cumulatively adds the day's profits and losses to the running total.

* Create additional lists to hold filtered data, allowing us to group data by profitable vs. unprofitable trading days using conditionals.

  ```python
  # Initialize lists to hold profitable and unprofitable day profits/losses
  profitable_days = []
  unprofitable_days = []
  ```

  ```python
  # Logic to determine profitable vs. unprofitable days
  if day_pnl > 0:
      profitable_days.append(day_pnl)
  elif day_pnl < 0:
      unprofitable_days.append(day_pnl)
  ```

* Grouping data allows us to see distributions among the data, in this case, the percentage of profitable days vs. the percentage of unprofitable days. Here it shows that the trader is doing pretty well: 

  ```python
  # Percentage metrics
  percent_profitable = profitable_count / count * 100
  percent_unprofitable = unprofitable_count / count * 100
  print(f"Number of Unprofitable Days: {unprofitable_count}")
  print(f"Percentage of Profitable Days: {percent_profitable}%")
  ```

  ```
  # Output
  Percentage of Profitable Days: 65.0%
  Percentage of Unprofitable Days: 35.0%
  ```

Ask if there are any questions before moving on.

- - -

### 8. Instructor Do: Introduction to Dictionaries (5 min)

**File:** [Slides](https://docs.google.com/presentation/d/1cFrN2LIjmDC2UdVQMYIY-_peQc4mty4R63lvyJbqn1I/edit?usp=sharing)

Open the slideshow and go to the slides on dictionaries. Explain to students: 

* Working with multiple data structures will help you understand the use cases for each type––in other words, when to use them. 

* In certain instances, lists are advantageous; in others, dictionaries may be more useful.

* The goal is to be able to leverage both of these data structures in order to efficiently store, maintain, and look up data. 

Define dictionary. 

* **Dictionaries** are data containers that store values using a special label called a **key**. When you provide a key to a dictionary, you receive the **value** that belongs to that key.
    
* Dictionaries operate just like physical, language dictionaries: if you know the word, you can find the definition. The word is the key, and the value is the definition.

To demonstrate the relationship between key and value, live code a simple example of declaring a dictionary. Explain: 

* The dictionary will contain the top traders for each month in 2019. 
    
* The month will be the key, and the name of the trader will be the value.

  ```python
  # Initialize a dictionary containing top traders for each month in 2019
  top_traders_2019 = {
    "january" : "Karen",
    "february" : "Harold",
    "march" : "Sam"
  }

  print()
  print(f"Dictionary: {top_traders_2019}")
  print()
  ```

Briefly discuss the differences between dictionaries and lists and when one should be used instead of the other.

* While dictionaries and lists are both data containers in Python, they behave quite differently. Lists store items in a specific order, and dictionaries store items in an unordered way using keys.

* Searching for values in dictionaries is significantly faster than looking for values in lists. 

    * It will always take the same amount of time to search for a value in a dictionary, even if the dictionary increases in size. 
    
    * However, size drastically increases performance time when searching a list; if a list doubles in size, search time could also double.

Ask if there are any questions before moving on. 

- - -

### 9. Instructor Do: Dicts (5 min)

**File:** [dicts.py](Activities/05-Ins_Dictionaries/Solved/dicts.py)

Before starting the demonstration, pose the following scenario: 

* Imagine you are prepping for a promotion to Senior Trader. You're 95% confident the promotion is yours, but you want to find one more way to add value to the firm. 

* You come up with the idea to use Python to automate a process that you, your manager, and coworkers spend countless hours doing each day: storing and tracking profits and losses. 

* So far, you have coded a good majority of the logic needed for this program. You've been using lists to store profits and losses every day, but you've heard that dictionaries have better search performance. 

* You don't know much about dictionaries, but you do know that you want your manager to see that you're innovative, and that you know how to create optimized Python programs!

Demonstrate the syntax for creating a dictionary to store daily trading profits and losses:

* Dictionaries are syntactically defined via `{}`, curly braces, with key-value pairs separated by `:`, colons.

* Dictionaries allow for heterogeneous data (varying data types). Here, the `trading_pnl` dictionary holds both strings and integers:

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
  {'title': 'Trading Log', '03-18-2019': -224, '03-19-2019': 352, '03-20-2019': 252, '03-21-2019': 354, '03-22-2019': -544, '03-23-2019': -650, '03-24-2019': 56, '03-25-2019': 123, '03-26-2019': -43, '03-27-2019': 254, '03-28-2019': 325, '03-29-2019': -123, '03-30-2019': 47, '03-31-2019': 321, '04-01-2019': 123, '04-02-2019': 133, '04-03-2019': -151, '04-04-2019': 613, '04-05-2019': 232, '04-06-2019': -311, '04-07-2019': 413}
  ```

* Specific values from a dictionary can be called via the associated key.

  ```python
  # Print out specific value of a key
  print(f"03-31-2019: {trading_pnl['03-31-2019']}")
  print()
  ```

  ```
  03-31-2019: 321
  ```

* Adding a new key-value pair entry to a dictionary is as easy as specifying a new key-value pair combination.

  ```python
  # Add a new key-value pair
  trading_pnl["04-07-2019"] = 413
  print(trading_pnl)
  print()
  ```

  ```
  {'title': 'Trading Log', '03-18-2019': -224, '03-19-2019': 352, '03-20-2019': 252, '03-21-2019': 354, '03-22-2019': -544, '03-23-2019': -650, '03-24-2019': 56, '03-25-2019': 123, '03-26-2019': -43, '03-27-2019': 254, '03-28-2019': 325, '03-29-2019': -123, '03-30-2019': 47, '03-31-2019': 321, '04-01-2019': 123, '04-02-2019': 133, '04-03-2019': -151, '04-04-2019': 613, '04-05-2019': 232, '04-06-2019': -311, '04-07-2019': 413}
  ```

* Modifying an existing key-value pair within a dictionary is as easy as specifying a new value for that particular key.

  ```python
  # Modify a key value
  trading_pnl["04-07-2019"] = 542
  print(trading_pnl)
  print()
  ```

  ```
  {'title': 'Trading Log', '03-18-2019': -224, '03-19-2019': 352, '03-20-2019': 252, '03-21-2019': 354, '03-22-2019': -544, '03-23-2019': -650, '03-24-2019': 56, '03-25-2019': 123, '03-26-2019': -43, '03-27-2019': 254, '03-28-2019': 325, '03-29-2019': -123, '03-30-2019': 47, '03-31-2019': 321, '04-01-2019': 123, '04-02-2019': 133, '04-03-2019': -151, '04-04-2019': 613, '04-05-2019': 232, '04-06-2019': -311, '04-07-2019': 542}
  ```

* Use the `del` keyword to delete a particular key within a dictionary.

  ```python
  # Delete a key-value pair
  del trading_pnl["04-07-2019"]
  print(trading_pnl)
  print()
  ```

  ```
  {'title': 'Trading Log', '03-18-2019': -224, '03-19-2019': 352, '03-20-2019': 252, '03-21-2019': 354, '03-22-2019': -544, '03-23-2019': -650, '03-24-2019': 56, '03-25-2019': 123, '03-26-2019': -43, '03-27-2019': 254, '03-28-2019': 325, '03-29-2019': -123, '03-30-2019': 47, '03-31-2019': 321, '04-01-2019': 123, '04-02-2019': 133, '04-03-2019': -151, '04-04-2019': 613, '04-05-2019': 232, '04-06-2019': -311}
  ```

* If-else statements can be used with dictionaries to check if a key exists.

  ```python
  # Check if key exists
  if "04-03-2019" in trading_pnl:
      print("Yes, '04-03-2019' is one of the keys in the trading_pnl dictionary")
  print()
  ```

  ```
  Yes, '04-03-2019' is one of the keys in the trading_pnl dictionary
  ```

* For loops can be used with dictionaries to iterate over every key in the dictionary.

  ```python
  # Print out dict keys via a for loop
  for key in trading_pnl:
      print(f"Key: {key}")
  ```

  ```
  Key: title
  Key: 03-18-2019
  Key: 03-19-2019
  Key: 03-20-2019
  Key: 03-21-2019
  Key: 03-22-2019
  Key: 03-23-2019
  Key: 03-24-2019
  Key: 03-25-2019
  Key: 03-26-2019
  Key: 03-27-2019
  Key: 03-28-2019
  Key: 03-29-2019
  Key: 03-30-2019
  Key: 03-31-2019
  Key: 04-01-2019
  Key: 04-02-2019
  Key: 04-03-2019
  Key: 04-04-2019
  Key: 04-05-2019
  Key: 04-06-2019
  ```

* For loops can be used in conjunction with operationally returning a value by a specific key to return all values in the dictionary.

  ```python
  # Print out dict values
  for key in trading_pnl:
      print(f"Value: {trading_pnl[key]}")
      print()
  ```

* For loops can be used in conjunction with calling the `items()` dictionary function to return all key-value pairs in the dictionary.

  ```python
  # Print out dict key-value pairs
  for key, value in trading_pnl.items():
      print(f"Key: {key} Value: {value}")
      print()
  ```

  ```
  Key: title Value: Trading Log
  Key: 03-18-2019 Value: -224
  Key: 03-19-2019 Value: 352
  Key: 03-20-2019 Value: 252
  Key: 03-21-2019 Value: 354
  Key: 03-22-2019 Value: -544
  Key: 03-23-2019 Value: -650
  Key: 03-24-2019 Value: 56
  Key: 03-25-2019 Value: 123
  Key: 03-26-2019 Value: -43
  Key: 03-27-2019 Value: 254
  Key: 03-28-2019 Value: 325
  Key: 03-29-2019 Value: -123
  Key: 03-30-2019 Value: 47
  Key: 03-31-2019 Value: 321
  Key: 04-01-2019 Value: 123
  Key: 04-02-2019 Value: 133
  Key: 04-03-2019 Value: -151
  Key: 04-04-2019 Value: 613
  Key: 04-05-2019 Value: 232
  Key: 04-06-2019 Value: -311
  ```

Ask if there are any questions before moving on.
- - -

### 10. Student Do: Market Capitalization (15 min)

In this activity, students will practice creating a dictionary, as well as updating, removing, and extracting values in/from the dictionary. The goal is to get students to better understand the advantages of using dictionaries to store, retrieve, and manipulate data.

**File:** [market_cap.py](Activities/06-Stu_Dictionaries/Unsolved/Core/market_cap_core.py)

**Instructions:** [README.md](Activities/06-Stu_Dictionaries/README.md)

### 11. Instructor Do: Review Market Capitalization (5 min)

**File:** [market_cap.py](Activities/06-Stu_Dictionaries/Solved/Core/market_cap_core.py)

Open the solution file, `market_cap.py`, and explain the following:

* The `banks` dictionary is heterogeneous, containing both int and float data types.

  ```python
  # Initialize a dictionary of banks and market caps (in billions)
    banks = {
    "JP Morgan Chase": 327,
    "Bank of America": 302,
    "Citigroup": 173,
    "Wells Fargo": 273,
    "Goldman Sachs": 87,
    "Morgan Stanley": 72,
    "U.S. Bancorp": 83,
    "TD Bank": 108,
    "PNC Financial Services": 67,
    "Capital One": 47,
    "FNB Corporation": 4,
    "First Hawaiian Bank": 3,
    "Ally Financial": 12,
    "Wachovia": 145,
    "Republic Bancorp": .97
    } 
    ```

* When grouping data in separate categorical buckets, it's best to create additional objects to hold those values.

  ```python
  # Initialize market cap lists
    mega_caps = []
    large_caps = []
    mid_caps = []
    small_caps = []
  ```

* Comparing against dictionary values allows us to pull the associated key for the corresponding action. 

* Here, `market_cap` is compared to the running `minimum_value` and `maximum_value` variables to pull the corresponding key associated with those calculated values.

  ```python
  # Iterate over key-value pairs of the dictionary
  print()
  for bank_name, market_cap in banks.items():
      print(f"Name: {bank_name} | Market Cap: {market_cap}")

      # Calculate sum of market caps and number of banks in the dictionary
      total_market_cap += int(market_cap)
      bank_count += 1

      # Logic to determine min and max values and associated keys
      if minimum_value == 0:
          minimum_value = market_cap
          minimum_key = bank_name
      elif market_cap < minimum_value:
          minimum_value = market_cap
          minimum_key = bank_name

      # Logic to determine max value and associated key
      if market_cap < maximum_value:
          maximum_value = market_cap
          maximum_key = bank_name
  ```

  ```
  Largest Bank: JP Morgan Chase
  Smallest Bank: Republic Bancorp
  ```

* Similar to the determination of the banks associated with the minimum and maximum market cap values, it is possible to group banks by their associated market cap values.

  ```python
  # Group banks by categories of market caps
  if market_cap >= 300:
      mega_caps.append(bank_name)
  elif market_cap >= 10 and market_cap < 300:
      large_caps.append(bank_name)
  elif market_cap >= 2 and market_cap < 10:
      mid_caps.append(bank_name)
  elif market_cap < 2:
      small_caps.append(bank_name)
  ```

  ```
  Mega Cap Banks: ['JP Morgan Chase', 'Bank of America']
  Large Cap Banks: ['Citigroup', 'Wells Fargo', 'Goldman Sachs', 'Morgan Stanley', 'U.S. Bancorp', 'TD Bank', 'PNC Financial Services', 'Capital One', 'Ally Financial', 'American Express']
  Mid Cap Banks: ['FNB Corporation', 'First Hawaiian Bank']
  Small Cap Banks: ['Republic Bancorp']
  ```

Ask if there are any questions before moving on.

- - -

### 12. BREAK (15 min)

- - -

### 13. Instructor Do: Nesting (10 min)

**Files:**

* [nesting_list_of_lists.py](Activities/07-Ins_Nesting/Solved/nesting_list_of_lists.py)

* [nesting_list_of_dicts.py](Activities/07-Ins_Nesting/Solved/nesting_list_of_dicts.py)

* [nesting_dict_of_lists.py](Activities/07-Ins_Nesting/Solved/nesting_dict_of_lists.py)

* [nesting_dict_of_dicts.py](Activities/07-Ins_Nesting/Solved/nesting_dict_of_dicts.py)

Introduce nesting by explaining that lists and dicts are really just data containers.

* The values in a list or dict can actually be other lists and dicts. This means that you can have a list of dictionaries or a dictionary where each value is a list. You can also have lists of lists and dicts of dicts! 

* This concept is called **nesting**, which is a powerful feature of the Python language because it provides a lot of flexibility for how data is stored.

Walk through the solution and highlight the following:

* Lists of lists contain multiple list elements. 

    * Each list element can have two or more values. 
    
    * Each element within the nested list must be separated by a comma.

  ```python
  # List
  ceo_list = ["Warren", "Jack", "Harry"]

  # List of Lists
  ceo_nested_list = [
      ["Warren Buffet", 88, "CEO of Berkshire Hathaway"],
      ["Jack Bogle", 90, "CEO of Vanguard"],
      ["Harry Markowitz", 91, "Professor of Finance"]
  ]
  ```

* When a nested list object has been created, data needs to be retrieved. Accessing elements in a nested list works similar to a one-dimensional list: 

    * To access elements, call the list object and then specify the index for the desired value. 
    
    * Because these lists are nested, two indexes will need to be provided: one index for the top level item, and one for the embedded element that needs to be retrieved.

  ```python
  #List of lists
  ceo_nested_list = [
      ["Warren Buffet", 88, "CEO of Berkshire Hathaway"],
      ["Jeff Bezos", 55, "CEO of Amazon"],
      ["Harry Markowitz", 91, "Professor of Finance"]
  ]

  # Retrieve first entry of ceo_nested_list
  first_entry = ceo_nested_list[0]

  # Retrieve name of first entry
  first_entry_name = ceo_nested_list[0][0]

  # Retrieve age of first entry
  first_entry_age = ceo_nested_list[0][1]

  # Retrieve occupation of first entry
  first_entry_occupation = ceo_nested_list[0][2]

  # Print results to screen
  print("The first entry in employees_nested_list is:", first_entry)
  print(f"{first_entry_name} is {first_entry_age} years old, serving as {first_entry_occupation}.")
  ```

* Lists of dicts are similar to lists of lists; however, the nested level is comprised of dicts rather than lists.

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
  ```

* Access and manipulate nested dict objects in the same way as dictionaries. 

    * To retrieve data from a list with nested dict objects, call the list with the index of the dict element that is desired. This will return the entire dictionary. 
    
    * If a specific dict value is desired, call the list with the index of the dict element and the corresponding dict key.

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

  # Retrieve second entry
  second_entry = ceo_nested_dict[1]

  # Retrieve name, age, and occupation of the second dict entry
  second_entry_name = ceo_nested_dict[1]["name"]
  second_entry_age = ceo_nested_dict[1]["age"]
  second_entry_occupation = ceo_nested_dict[1]["occupation"]

  print(f"The second entry in ceo_nested_dict is {second_entry_name}, a {second_entry_age} year old {second_entry_occupation}.")
  ```

Review how to declare and traverse nested dictionaries.

* Dictionaries of lists are objects based on key-value pairs. Unlike regular dicts, dicts of lists have more than one entry for the value.

  ```python
  # Dict
  stocks_dict = {
      "APPL": 101.32,
      "MU": 43.4,
      "AMD": 23.12,
      "TWTR": 25
  }

  # Dictionary of Lists
  stocks_nested_list = {
      "APPL": ["Apple", 101.32, "NASDAQ", 937.7],
      "MU": ["Micron Technology", 32.12, "NASDAQ", 48.03],
      "AMD": ["Advanced Micro Devices", 23.12, "NASDAQ", 29.94],
      "TWTR": ["Twitter", 34.40, "NASDAQ", 26.42]
  }
  ```

* Data can be accessed from dicts of lists by calling the dictionary and specifying the key for the desired entry. A specific value from the list object can be retrieved by providing the index.

  ```python
  # Dictionary of Lists
  stocks_nested_list = {
      "APPL": ["Apple", 101.32, "NASDAQ", 937.7],
      "MU": ["Micron Technology", 32.12, "NASDAQ", 48.03],
      "AMD": ["Advanced Micro Devices", 23.12, "NASDAQ", 29.94],
      "TWTR": ["Twitter", 34.40, "NASDAQ", 26.42]
  }

  # Retrieve entry for APPL
  appl_entry = stocks_nested_list["APPL"]

  # Retrieve name, stock_price, and exchange for APPL entry
  appl_name = stocks_nested_list["APPL"][0]
  appl_stock_price = stocks_nested_list["APPL"][1]
  appl_exchange = stocks_nested_list["APPL"][2]

  print(f"APPL ticker stands for {appl_name}. APPL stock price is currently {appl_stock_price}, and it is available on {appl_exchange}.")
  ```

* Dictionaries of dicts are objects based on nested key-value pairs. Unlike dicts of lists, dicts of dicts will have a dictionary as the value.

  ```python
  # Dictionary of Dicts
  stocks_nested_dict = {
    "APPL": {
        "name": "Apple",
        "exchange": "NASDAQ",
        "market_cap": 937.7
    },
    "MU": {
        "name": "Micron Technology",
        "exchange": "NASDAQ",
        "market_cap": 48.03
    },
    "AMD": {
        "name": "Advanced Micro Devices",
        "exchange": "NASDAQ",
        "market_cap": 29.94
    },
    "TWTR": {
        "name": "Twitter",
        "exchange": "NASDAQ",
        "market_cap": 26.42
    }
  }
  ```

* The top-level dictionary item can be accessed by calling the dictionary and specifying the key. Individual elements in the value collection can be accessed by specifying the key of the nested dict.

  ```python
  # Dictionary of Dicts
  stocks_nested_dict = {
    "APPL": {
        "name": "Apple",
        "exchange": "NASDAQ",
        "market_cap": 937.7
    },
    "MU": {
        "name": "Micron Technology",
        "exchange": "NASDAQ",
        "market_cap": 48.03
    },
    "AMD": {
        "name": "Advanced Micro Devices",
        "exchange": "NASDAQ",
        "market_cap": 29.94
    },
    "TWTR": {
        "name": "Twitter",
        "exchange": "NASDAQ",
        "market_cap": 26.42
    }
  }

  # Retrieve Twitter entry
  twitter_entry = stocks_nested_dict["TWTR"]

  # Retrieve TWTR name, exchange, and market_cap
  twitter_name = stocks_nested_dict["TWTR"]["name"]
  twitter_exchange = stocks_nested_dict["TWTR"]["exchange"]
  twitter_market_cap = stocks_nested_dict["TWTR"]["market_cap"]

  print(f"Name of TWTR ticker is {twitter_name}. TWTR is available on {twitter_exchange}, and it currently has a market capitalization of {twitter_market_cap}.")
  ```

Ask if there are any questions before moving on.
- - -

### 14. Student Do: Weekly Gains (20 min)

In this activity, students will work with nested data structures in a Python file. Students will store daily stock data in a list and then store that list in a dictionary. The key of the dictionary will be the stock tickers. They will then retrieve stock data from the dictionary for specific days.

Encourage students to work with a partner on this activity.

**File:** [weekly_gains.py](Activities/08-Stu_Nesting/Unsolved/Core/weekly_gains_core.py)

**Instructions:** [README.md](Activities/08-Stu_Nesting/README.md)

### 15. Instructor Do: Review Weekly Gains (5 min)

**File:** [weekly_gains.py](Activities/08-Stu_Nesting/Solved/Core/weekly_gains_core.py)

Open the solution file, `weekly_gains.py`, and explain the following:

* Nested objects allow us to contain and structure more information in one place. Although this may be convenient, this also makes accessing data more complicated as the number of nested levels increases.

* The `historical_stock_data` dictionary holds a stock ticker key and a list of daily price records as the value. Each daily price record consists of a `date` and `open`, `high,` `low`, and `close` prices.

  ```python
  # Dictionary of List of Lists
  # Key: Stock Ticker | Value: List of Records
  # Record: Date, Open, High, Low, Close
  historical_stock_data = {
      "AAPL": [
          ["04-17-2019", 199.54, 203.38, 198.61, 203.13],
          ["04-18-2019", 199.46, 201.37, 198.56, 199.25],
          ["04-19-2019", 198.58, 199.85, 198.01, 199.23],
          ["04-20-2019", 199.20, 200.14, 196.21, 198.87],

      ],
      "MU": [
          ["04-17-2019", 43.20, 43.53, 42.79, 43.40],
          ["04-18-2019", 43.36, 44.05, 42.76, 43.15],
          ["04-19-2019", 42.26, 42.93, 42.08, 42.76],
          ["04-20-2019", 42.17, 42.23, 41.20, 41.82],

      ],
      "AMD": [
          ["04-17-2019", 27.60, 27.88, 27.34, 27.68],
          ["04-18-2019", 28.21, 28.27, 27.22, 27.49],
          ["04-19-2019", 27.72, 28.18, 27.49, 27.93],
          ["04-20-2019", 27.80, 27.84, 26.96, 27.33],

      ],
      "TWTR": [
          ["04-17-2019", 34.67, 34.86, 34.32, 34.40],
          ["04-18-2019", 34.73, 34.90, 34.20, 34.48],
          ["04-19-2019", 34.84, 34.99, 34.23, 34.46],
          ["04-20-2019", 34.38, 35.03, 34.34, 34.71],
      ]
  }
  ```

* The `new_records` dictionary holds a stock ticker key and a dictionary of a single daily price record as the value.

  ```python
  # Dictionary of Dictionary
  # Key: Stock Ticker | Value: Dictionary
  new_records = {
      "AAPL": {
          "date": "04-21-2019",
          "open": 200.85,
          "high": 201.00,
          "low": 198.44,
          "close": 198.95
      },
      "MU": {
          "date": "04-21-2019",
          "open": 42.85,
          "high": 43.20,
          "low": 41.81,
          "close": 42.01
      },
      "AMD": {
          "date": "04-21-2019",
          "open": 28.21,
          "high": 28.38,
          "low": 27.66,
          "close": 27.85
      },
      "TWTR": {
          "date": "04-21-2019",
          "open": 34.67,
          "high": 34.83,
          "low": 34.11,
          "close": 34.37
      }
  }
  ```

* Use a for loop to iterate over every key-value pair in the `new_records` dictionary, and assign each daily price record to the corresponding stock ticker list of daily prices in the `historical_stock_data` dictionary. This is more effective than doing it manually. 

  ```python
  # Set each ticker's new record: date, open, high, low, close
  new_aapl_record = [new_records['AAPL']['date'], new_records['AAPL']['open'], new_records['AAPL']['high'], new_records['AAPL']['low'], new_records['AAPL']['close']]
  new_mu_record = [new_records['MU']['date'], new_records['MU']['open'], new_records['MU']['high'], new_records['MU']['low'], new_records['MU']['close']]
  new_amd_record = [new_records['AMD']['date'], new_records['AMD']['open'], new_records['AMD']['high'], new_records['AMD']['low'], new_records['AMD']['close']]
  new_twtr_record = [new_records['TWTR']['date'], new_records['TWTR']['open'], new_records['TWTR']['high'], new_records['TWTR']['low'], new_records['TWTR']['close']]

  # Choice 1: Add a new round of entries to the 'historical_stock_data' dictionary
  historical_stock_data['AAPL'].append([new_aapl_record])
  historical_stock_data['MU'].append([new_mu_record])
  historical_stock_data['AMD'].append([new_amd_record])
  historical_stock_data['TWTR'].append([new_twtr_record])
  #print(historical_stock_data)

  # Choice 2: Add a new round of entries via for loop to the 'historical_stock_data' dictionary
  for ticker, ticker_data in new_records.items():
      # Set the new record to be added in list format
      record = [ticker_data['date'], ticker_data['open'], ticker_data['high'], ticker_data['low'], ticker_data['close']]
      # Append the new record to the historical_stock_data dictionary
      historical_stock_data[ticker].append(record)

  # Print out the modified 'historical_stock_data' dictionary
  print(historical_stock_data)
  ```

* To calculate the weekly gains, take the closing prices of the first and last record of the list of daily prices for each stock ticker. The list index notations `list[0]` and `list[-1]` target the first and last elements of a list, respectively.

  ```python
  # Initialize 'results' dictionary to hold weekly change of each ticker
  results = {}

  # Calculate the weekly change of each stock ticker
  for ticker, ticker_data in historical_stock_data.items():

      # Set closing prices of first and last records of each stock ticker
      ending_week_close = ticker_data[-1][4]
      beginning_week_close = ticker_data[0][4]

      # Calculate weekly change per stock ticker
      ticker_weekly_change = round((ending_week_close - beginning_week_close) / beginning_week_close * 100, 2)
      print(ticker_weekly_change)

      # Set the weekly change for every stock ticker in the 'results' dictionary
      results[ticker] = ticker_weekly_change

  # Print out 'results' dictionary
  print(results)
  ```

Ask if there are any questions before moving on.

- - -

## 16. Instructor Do: Introduction to Functions (5 min)

**File:** [Slides](https://docs.google.com/presentation/d/1cFrN2LIjmDC2UdVQMYIY-_peQc4mty4R63lvyJbqn1I/edit?usp=sharing)

Open the slideshow and go to the slides on functions. Explain the following:

* This section on functions is meant to help write programs with modularity. **Modularity** is the degree to which components or parts can be separated or decoupled from a whole.

* **Modularity** greatly improves code readability and ensures that reusable lines of code are reused in an efficient, effective way.

* This introduction to functions will put you on the path to creating analytical functions for finance. 

Define functions. 

* **Functions** offer a methodology for splitting up blocks of code that are redundant or need to be reused. 

* Functions are valuable because they make programs more modular and reusable. 

* Functions can be created by a developer or imported from a library. 

  ```python
  import math
  ```

Explain what "reinventing the wheel" means and the drawbacks of not leveraging reusable/repeatable assets.

Engage students by asking if they can remember any of the functions used in class so far. For example: 

* `print()`

* `range()`

* `round()`

* `append()`

* `index()`

* `pop()`

Ask if there are any questions before moving on. 

- - -

## 17. Instructor Do: Functions (5 min)

**File:** [functions.py](Activities/09-Ins_Functions/Solved/functions.py)

Open `functions.py` and facilitate a discussion focused on the following points: 

* Functions allow you to define a reusable block of code. This code block (function) can be used whenever or wherever you need it within a program. 

* Reusing code means that there is less redundant code. It also means that you can build up your own libraries of useful, reusable code blocks (aka functions).

* Functions are easy to create. Use the `def` keyword to define your function, give the function a name, and then indent whatever code you want to become part of the function.

Live code and define the following function. Do not call it. Then, run the Python script and ask students what happens. 

Explain that a function won't be executed if it is not called. Add a line of code that shows the function call.

```python
"""
Create a main function that prints Greetings!
"""

def main():
    print("Greetings!")
```

```python
# Call main function
main()
```

Review the mechanics of function inputs and outputs while showing the code:

* Functions can have inputs. 

    * **Inputs** are called arguments, and arguments are passed to functions. 
    
    * Arguments can be variables, data structures, or other functions. 
    
    * Inputs are not required.

  ```python
  """
  Using a function, concatenate a string input with a message
  """

  def main(stock_ticker):
      print(stock_ticker + " is booming right now!")
  ```

* Functions can produce output. 

    * Output can range from a print statement to a value from a computation to auto-generated code. 
    
    * If outputting a value from a computation, the `return` keyword must be used. 
    
    * `return` can only be used once per function.

  ```python
  """
  Using a function, implement Market Cap calculation
  """

  def calculate_market_cap(market_price, number_of_shares):
      cap = market_price * number_of_shares

      # Output market_cap value
      return cap
  ```

* Each function call will need to include the required input arguments. 

* By passing in an argument as input, a program can run the same code against two different types of input.

  ```python
  """
  Initialize market_price and number_of_shares variables
  """

  stock_ticker = "SBUX"
  market_price = 76.06
  number_of_shares = 1243600000

  # Call calculate_market_cap() function
  market_cap = calculate_market_cap(market_price, number_of_shares)
  print(f"{stock_ticker} Market Capitalization: {market_cap}")
  ```

* The output of a function can be captured and saved as a variable. 

* The variable to which you assign the output of the function will inherit the data type and value of the function output.

  ```python
  """
  Capture function output as variable
  """

  market_price = 76.06
  number_of_shares = 1243600000

  # Call calculate_market_cap() function and capture output as market_cap
  market_cap = calculate_market_cap(market_price, number_of_shares)
  print(f"Market Capitalization: {market_cap}")
  print(f"Data type of market_cap variable is: {type(market_cap)}")
  ```

* Variable scope is imperative to understand when working with functions. Variables can be understood as either global or local. 

    * Global variables are defined outside of functions. 
    
    * Local variables are defined within functions. 
    
* Functions only have access to read and write to variables that are passed as arguments, global, or defined within the function itself. Variables that are defined locally to a function cannot be accessed outside of that function. 

* To work around this, return a function's local variable and capture the results in a different variable.

  ![LP_Ins_Functions_Variable_Scope.png](Activities/09-Ins_Functions/Images/LP_Ins_Functions_Variable_Scope.png)

* Function names should follow the `camel_case` naming convention.

  ```python
  def calculate_market_cap()
  ```

* Function bodies should not include more than 40–50 lines of code. Code longer than 40–50 lines should be decoupled and split into different functions.

Ask if there are any questions before moving on. 

- - -

### 18. Student Do: Functions (20 min)

In this activity, students will define a function to calculate compound annual growth rate (CAGR) for an investment portfolio. The goal of this activity is for students to use functions to modularize code and reduce redundancy.

Encourage students to work with a partner on this activity.

**File:** [finally_functioning.py](Activities/10-Stu_Functions/Unsolved/finally_functioning.py)

**Instructions:** [README.md](Activities/10-Stu_Functions/README.md)

### 19. Instructor Do: Review Functions (10 min)

**File:** [finally_functioning.py](Activities/10-Stu_Functions/Solved/finally_functioning.py)

Open the solution file, `finally_functioning.py`. Review the activity solution, covering the following points: 

* `calculate_compound_growth_rate` accepts three arguments, all of which are needed to calculate growth rate.

* These variables are set up as global variables so that they can be accessed in the function code block, as well as in other places.

  ```python
  def calculate_compound_growth_rate(beginning_balance, ending_balance, years):
      growth_rate = (ending_balance / beginning_balance)**(1/years) - 1
      return growth_rate
  ```

* The function was called three times, with three different sets of arguments. By passing these as arguments, we can dynamically calculate growth rate. 

* This is what makes functions so dynamic! When used with variables, you can write code knowing that your logic can be dynamically leveraged in multiple use cases.

  ```python
  calculate_compound_growth_rate(beginning_balance, ending_balance, years)
  calculate_compound_growth_rate(beginning_balance, ending_balance, years)
  calculate_compound_growth_rate(beginning_balance, ending_balance, years)
  ```

* `calculate_compound_growth_rate` was called three times for three different years, and the output was captured in three different variables. 

* Having each year's growth rate in distinct variables allows the values to be manipulated down the road, adding more flexibility to the code.

  ```python
  year_one_growth = calculate_compound_growth_rate(beginning_balance, ending_balance, years)
  year_two_growth = calculate_compound_growth_rate(beginning_balance, ending_balance, years)
  year_three_growth = calculate_compound_growth_rate(beginning_balance, ending_balance, years)
  ```

* The `round` function is used to present the most precise dollar amount. The number of digits to round to is configurable. In this example, dollar amounts are rounded to two decimal places.

  ```python
  year_one_growth_rnd = round(year_one_growth,2)
  year_two_growth_rnd = round(year_two_growth,2)
  year_three_growth_rnd = round(year_three_growth,2)
  ```

Ask students what can be added to this program to make it more powerful and valuable. 

To get them thinking, provide an example: _Add a decision structure that identifies which years had the highest and lowest growth rates._

Engage students with the following review questions:

* What are functions?

    **Answer:** Functions are callable objects.

* What are the attributes of a function?

    **Answer:** The attributes of a function are name, input, and return output.

* What are function inputs called?

    **Answer:** Function inputs are called arguments/parameters.

* How do you program a function to provide output?

    **Answer:** The `return` keyword instructs a function to provide output.

* How many `return` values can a function have?

    **Answer:** A function can have only `return` one value.

* What are the advantages of using functions?

    **Answer:** Functions make code modular, reusable, and more readable.

* How do you use a function?

    **Answer:** To use a function, the function must be called. Arguments must be provided when calling a function.

* What is the naming convention used for functions?

    **Answer:** Functions subscribe to the `camel_case` naming convention.

* How many lines of code should be in the `body` of a function?

    **Answer:** The `body` of a function should contain between 40-50 lines of code in order to improve readability.

To guide students, you may want to follow up with questions such as:

* Can functions accept other functions as arguments?

* What would happen if you called a function within a `for` loop?

* What has been your experience working with functions so far?

Ask if there are any questions before moving on.

- - -

### 20. Instructor Do: Reflection and End Class 

Use the last few minutes of class to give the students encouraging and positive feedback. Remind them that they're one step closer to conquering Python and becoming FinTech visionaries!

Then give students an opportunity to share any thoughts they have about this lesson and the course so far. Ask questions such as the following: 

* What activity was the most enjoyable to complete? What was the most fulfilling activity?

* What do you find to be the most stressful aspect of programming?

* What concepts or topics gave you the most difficulty? 

* Did you figure out any shortcuts or unique ways to complete the steps of the activities? 

Emphasize that students are making great progress so far, and learning financial and technical concepts is not easy. It takes practice, abstract thinking, and perseverance. 

Remind students that they have come a long way in just two classes. They are now creating iterative programs that leverage variables, conditional statements, loops, lists, dictionaries, nested data structures, and functions. This is exciting and mind-blowing! 

Let students know that office hours are available for anyone who would like to ask questions or review topics, or would just like to talk Python, programming, and/or FinTech!

### End Class

- - -

© 2019 Trilogy Education Services 
