## FAQs

## Unit 02: Python
[What's the relevance of Python?](#what's-the-relevance-of-python)<br>
[What's up with this crazy indentation?](#what's-up-with-this-crazy-indentation)<br>
[How do list comprehensions work?](#how-do-list-comprehensions-work)<br>
[How are variables assigned with a For Loop?](#how-are-variables-assigned-with-a-For-Loop)<br>
[How does slicing work?](#how-does-slicing-work)<br>
[How do you access values in a nested dictionary?](#how-do-you-access-values-in-a-nested-dictionary)<br>

#### What's the relevance of Python?
Python is the primary language that we will be using in this course. It's a semantic language which makes it easier to read and understand, and the reliance on indentation makes the organized structure quicker to grasp. With this language, we'll be able to dive into a slew of libraries that will make solving complex data problems more simple.

#### What's up with this crazy indentation?
With Python, indentation is more than just organization and readability. Python's functionality actually depends on proper indentation!

In this snippet, we're using indentation to tell our code where our for loops begin and end. In Python, indenting creates blocks of code that work together. Similarly, indenting backwards tells the program when to end a loop.

```python
for x in range(10):
    print(x)

for x in range(20, 30):
    print(x)
```

The code you will write in Python will eventually be seen by someone else. Focusing on organization and readability is important because you want colleagues to be able to read your code. If your code is poorly organized it will be difficult to read later on.



#### How do list comprehensions work?
In a list comprehension, you are writing a for loop in a concise format that outputs a list object.  It can be confusing because the variable is repeated twice.  What the code is saying is: for each item in my old list, add that item to my new list.

For example:

Input:
```Python
old_list = range(10)
new_list = [item for item in old_list]
    print(new_list)
```
Output:
```Python

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### How are variables assigned with a For Loop?
Typically a for loop is iterating over an object and extracting each of the next smallest objects.  The variable is established after the word `For`. If your variable is `letter` and your object is `name` then Python finds the next smallest item in the `name` object you are iterating over and assigns `letter` to each of them.


Input:
```Python
name = 'Elliot'
for letter in name:
  print(letter)
```
Ouput:
```Python
E
l
l
i
o
t
```

In the example of a list of strings, the next smallest items are the individual strings:


Input:
```Python
name_list = ['Elliot' ,'Darlene', 'Angela', 'Shayla']
for name in name_list:
  print(name)
```
Output:
```Python
Elliot
Darlene
Angela
Shayla
```


#### How does slicing work?
Slice notation allows you to extract certain information from a list.  The syntax is `a[start:stop:step]`, with `step` being an optional component.  If a start number is ommited, it is assumed to be zero.  If a stop number is ommitted, it is assumed to be one more than the index number of the last item in the data.  In the following examples ommitting the stop number is the equavilient of using the number 4, because there are only 4 items (0, 1, 2, 3) in the list.

Given the following list:
`name_list = ['Elliot' ,'Darlene', 'Angela', 'Shayla']`

Input: `name_list[:]` OR `name_list[0:4]`

Both have the same output:
```Python
['Elliot' ,'Darlene', 'Angela', 'Shayla']
```

Input: `name_list[0:2]`

Output is first two names:
```Python
['Elliot' ,'Darlene']
```

Input: `name_list[2:4]`

Output is last two names:
```Python
['Angela', 'Shayla']
```

Input: `name_list[0:4:2]` OR `name_list[:4:2]` OR `name_list[::2]`


All three have the same output - every other name, starting with the first name:
```Python
['Elliot', 'Angela']
```

For more information check out this [Stack Overflow post](https://stackoverflow.com/questions/509211/understanding-slice-notation)

#### How do you access values in a nested dictionary?

Think of a dictionary like an assembled puzzle.  To get one of the pieces out of the puzzle, you have to deconstruct the puzzle by breaking apart the larger chunks and then the smaller chunks.  If you have a list of two dictionaries, you must first extract the dictionary you want, then you can extract the value you want.

In the following list of dictionaries lets access the 2nd pilot of the Galactica:
```Python
battlestars =
[{'Ship': 'Pegasus',
  'Commander': 'Admiral Helena Cain',
  'Pilots': ['Whiplash', 'Thumper']},
 {'Ship': 'Galactica',
  'Commander': 'Admiral William Adama',
  'Pilots': ['Starbuck', 'Apollo', 'Helo', 'Athena']}]
```
Our list contains two dictionaries, with the Galactica being in the 2nd one.
![Alt Text](Resources/battlestar_dictionary.gif)

So we first call our list object (`battlestars`), then the index position of our 2nd dictionary - `1`.

```Python
battlestars[1]
```
Which gives us:
```Python
{'Ship': 'Galactica',
  'Commander': 'Admiral William Adama',
  'Pilots': ['Starbuck', 'Apollo', 'Helo', 'Athena']}
```

Now that we have the dictionary we want, we can call the key we want.
![Alt Text](Resources/galactica_dictionary.gif)


We need to get information on pilots, so we call the 'Pilots' key:
```Python
battlestars[1]['Pilots']
```
Which gives us:
```Python
['Starbuck', 'Apollo', 'Helo', 'Athena']
```

Now we have extracted a list of pilots.  We just need to use the index position of the Pilot we want to finish up.  We want the 2nd pilot in the list, so we call position 1:

```Python
battlestars[1]['Pilots'][1]
```

Which gives us:
```Python
'Apollo'
```
