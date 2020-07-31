# Describing America

Somehow, the speech delivered by country leaders when they start duties on their charge could shape the line they will follow during their term. In this activity, you will use NLTK and spaCy to analyze the inaugural addresses delivered by the Presidents from the United States since 1798.

You will use [the inaugural address corpus](https://www.nltk.org/book/ch02.html#inaugural-address-corpus) from the NLTK library to identify what were the most common adjectives used by U.S. Presidents and how these adjectives describe America.

## Initial considerations

In the `Initial imports` cell from the starter Jupyter notebook, we import two modules that are worth highlighting.

* The `Counter` module from the `collections` library will allow you to track how many times equivalent values are into a list.

* The `inaugural` module from the `nltk.corpus` library provides some methods to extract information from [the inaugural address corpus](https://www.nltk.org/book/ch02.html#inaugural-address-corpus).

## Instructions

Open the starter Jupyter notebook and complete the following tasks.

### 1. Retrieve the documents IDs and text of the U.S. presidential inaugural addresses

In the `inaugural` module, the `fileids()` function retrieves each document's name, where the year of the inaugural address and the President's last name can be identified. This document name represents a unique identifier (ID) for each text in the corpus.

The `raw()` function receives as argument the ID for any given inaugural address and returns the text of the speech delivered by the President.

Use the `fileids()` and `raw()` functions to retrieve the following data from the `inaugural` corpus.

* Retrieve the IDs of the inaugural addresses using the `fileids()` function and store them in a variable named `ids`.

* Use the `raw()` function to retrieve the text of every inaugural address and store all the text documents as elements of a Python list called `texts`.

* For testing purposes, print the first document ID and the first inaugural address in the corpus.

### 2. Retrieve the most frequent adjective from each inaugural address

In this section, you will retrieve the most frequent adjective used in every inaugural address. A function called `most_freq_adj()` is provided to help you to complete this task.

* Analyze the code of the `most_freq_adj` function and make some tests to figure out how it works. This function uses the `Counter` module. You can learn more about it in [this page of the Python documentation](https://docs.python.org/3.7/library/collections.html#collections.Counter).

* Use the `most_freq_adj` to create a Python list containing the most common adjective from each inaugural address. Remember that you store all the inaugural addresses in the `texts` Python list.

* Create a DataFrame `df_adjs` with the most common adjective for each inaugural address. Define two columns, `doc_id` with all the document IDs you store in the `ids` Python list, and `adjective` containing the most common adjective from each inaugural address.

### 3. Analyze adjectives over time

In this section, you will analyze how many times U.S. Presidents used the most common adjectives in their inaugural addresses over time.

Two helper functions are provided to aid you in this task.

1. `all_adj()`: This function retrieves all the adjectives on the given text.

2. `get_word_counts()`: This function counts the occurrences of a word in a text.

Use these functions to analyze the usage of the adjective over time as follows.

* Use the `all_adj()` function provided to create a Python list `all_adjectives` containing all the adjectives into all the inaugural addresses.

* Use the `most_common()` function from the `Counter` module to fetch the three most frequent adjectives used in the U.S. Presidential inaugural address. The `most_common()` function returns a Python list that you should store in a variable called `most_freq_adjectives`.

* Use the `get_word_counts()` function provided to compute the counts of each of the three most frequent adjectives in the U.S. presidential inaugural addresses. Store the adjective counts in three different Python lists called `great_counts`, `other_counts`, and `own_counts`.

* Create a Python list `dates` to store the year when every inaugural address was delivered. You can retrieve the year of each inaugural address from the document IDs you store as string values in the `ids` list and using [the `split()` function](https://docs.python.org/3.7/library/stdtypes.html#str.split).

* Create a Python list `presidents` to store the last name of each U.S. President whose inaugural address is in the `inaugural` corpus. You can retrieve the Presidents last name from the document IDs you store as string values in the `ids` list and using [the `split()` function](https://docs.python.org/3.7/library/stdtypes.html#str.split).

* Create a DataFrame `df_adjectives` with the Presidents' last names and the adjectives counts as columns, and set the `dates` list as the index.

* Create a line plot using the `df_adjectives` DataFrame to visualize the usage of the most common adjective over time in the U.S. presidential inaugural addresses.

### 4. Adjectives describing America

In this section, you will use spaCy to analyze all the documents in the inaugural corpus to identify the adjectives that describe the head word `America`.

* Use spaCy to create a function `describe_america()` that returns the adjectives in all the inaugural addresses that describe de head word `America`

* Use the `describe_america()` function you defined to create a Python list containing all the adjectives describing the word `America` into all the inaugural addresses in the corpus.

## Hints

* To create the Python list, we encourage you to use list comprehensions. You can recall [how list comprehensions work in the Python documentation](https://docs.python.org/3.7/tutorial/datastructures.html#list-comprehensions).

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
