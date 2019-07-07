### 6. Instructor Demo: Stopwords (0:10 mins)

This activity introduces the concept and implementation of stopwords. In English, there are many words that are important to grammar and expression but have no topical significance - these include some of the most common words in the language, such as "is," "him," "for," etc. In NLP, these words are called stopwords. For many use cases in which we hope to summarize the contents of a corpus - such as frequency analysis or topic modeling, for example - we want to take these words out in preprocessing so that they don't distract from the topically important words and phrases. We will also take a look at a way of stripping out non-alphabetic characters, which we might want to do for a similar reason. 

**Files:**

Solved: [stopwords.ipynb](C:\Users\Mike\Documents\fintech\FinTech-Lesson-Plans\01-Lesson-Plans\13-NLP\1\Activities\03-Ins_Stopwords\Solved\stopwords.ipynb)

Walk through the notebook, taking care to allow time for students to look at the output of each step. 

* For simplicity's sake, we're only going to use one sentence from the article in order to demonstrate stopwording. Note that these techniques can be applied to entire documents or corpuses as well. 

* Ask students to familiarize themselves with NLTK's list of stopwords. What others can they think of that might be added? Could stopwords for one domain be ill-suited for another (for example, might you want to ignore certain words in finance documents that you wouldn't want to ignore in documents about history)?

* We can strip a word_tokenized list of stopwords with the following list comprehension:

```python
sw = set(stopwords.words('english'))
first_result = [word.lower() for word in words if word.lower() not in sw]
```

* Two important notes here: first, we choose to instantiate the list of stopwords as a set because a set is more efficient computationally compared to a list when we want to determine whether or not a word exists in it. This is not a big difference when we only want to do this once, but if you have large numbers of documents and words the time efficicency can become significant. Second, we want to use the .lower() string function to make all words in the list lowercase when we evaluate them because stopwords are only in lowercase. We can output the words either in their regular case or in all lowercase - usually, the latter is preferred because this is one more way of normalizing words. This becomes important if we're doing something like frequency analysis because words like "orange" and "Orange," in most cases, mean the same thing regardless of capitalization. 

![stopwords1](Images/stopwords1.PNG)

* Have students take a look at the result after the sentence has been "stopworded." Are there other words in there that are not informative? If so, we can define our own list of custom stopwords and join these to the NLTK list when we perform this step of preprocessing:

```python
sw_addon = {'said', 'mln', 'kilolitres','kl'}
second_result = [word.lower() for word in words if word.lower() not in sw.union(sw_addon)]
```

Note that the union function here combines the unique elements of the two sets. 

![stopwords2](Images/stopwords2.PNG)

* Once again, have students take a look at the result. We've gotten rid of the words that are uninformative, but what about the numbers and punctuation at the end? For most use cases, these characters are also of little use. It's possible to get rid of them using the stopwords methodology - but this would involve entering every combination of numbers and punctuation that exists in the corpus, and that's unrealistic. 

* Instead, we're going to make use of regular expressions. Direct students to this resource for learning more about regular expressions and how they're implemented in Python: https://docs.python.org/3/library/re.html For now, though, go through the following code:

```python
regex = re.compile("[^a-zA-Z ]")
re_clean = regex.sub('', sentence)
```

* Regex substitution here takes two steps. In the first, we compile a pattern to match for. In this case, we want to match all characters that is not a letter or a space (denoted by the carrot followed by lower and uppercase letters). In the second, we use the .sub() function to substitute out whatever matches that pattern in the string we want to "clean." Important: stress to students that this step should occur BEFORE the text is word tokenized. 

* Finally, have students take a look at the results of regex cleaning, followed by the stopwording that we did before. 

![stopwords3](Images/stopwords3.PNG)
