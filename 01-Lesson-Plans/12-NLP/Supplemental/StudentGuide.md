# Unit 12: Natural Language Processing

### Helpful Links

* This online version of the NLTK book, [*Natural Language Processing with Python – Analyzing Text with the Natural Language Toolkit*](https://www.nltk.org/book/), is a great reference for all things NLTK.

* An excellent starter resource on spaCy: [*spaCy 101: Everything you need to know*](https://spacy.io/usage/spacy-101).

* The [Word Cloud](https://amueller.github.io/word_cloud/) documentation has everything from command-line interface tools to gallery examples of how to make your own, unique word cloud.
---

### Additional Course Resources

* [NLP installation guide](nlp-env-install-guide.md)

---

### FAQs

<details>
<summary>What is Natural Language Processing?</summary><br>

Natural language processing is a field focused on the goal of having computers interact with (understand and generate) natural (human) language.

Examples include:
* A spell Checker.

* Talking to digital assistants such as Alexa, Siri or Google Assistant.

* Voice-to-text on mobile devices.

Computer language is very specific; its unambiguous, literal, methodical, and mathematical. Human language is quite the opposite. Words can share multiple meanings when used in different contexts, despite being spelled the same or sounding the same.

When translating words between languages, the direct word-for-word translation will often sound nonsensical because the order of the words and cultural idioms vary. Even different dialects of the same language can have words or sayings that mean different things depending on your geography.

NLP allows us to process human language and text so that it can be used in machine learning and software applications.

</details>
<details>
<summary>What is Tokenization and why do I need it?</summary><br>

Tokenization is the process of breaking apart language into smaller pieces. A document of text could be tokenized into sentences, the sentences could be tokenized into words or phrases, or a word could be tokenized into characters. Tokens can then be counted, grouped, sorted, and further processed to help us better understand the content of the text. A simple example of tokenization is using Python's `.split()` function to split a sentence into a list of words using the whitespace as a delimiter.

<blockquote>
<details><summary>Word Tokenization</summary><Br>

In the following example we'll use `.split()` and the space delimiter to tokenize our sentence:

![sentence](Images/sentence_split.PNG)

This method works ok, but NLP can become much trickier than breaking down a sentence by a single delimiter. You might need to write code that breaks down an entire text into whole phrases on multiple delimiters. Because of this, we can use the Natural Language ToolKit (NLTK) platform to perform our tokenizing. NLTK provides libraries and tools that help with NLP tasks such as text processing. Let's tokenize the same sentence using NLTK's tokenizer, `word_tokenizer()`:

![sentence1](Images/sentence_tokens.PNG)

This method allows us to handle complex situations such as punctuation. We can also use regular expressions to customize our tokenizer further. This gives us much more flexibility to concisely deliver the intended outcome regardless of how complex the text might be.
</details>
<details><summary>Sentence Tokenization</summary><br>

Sentences can also be tokenized.  In the following example, we'll tokenize a short text into sentences.  First we use `.split()` and the period delimiter:


![sentence3](Images/sentence_sent_split.PNG)

This works ok, but what if we have a more complex text? What if our text has exclamation points or question marks? Or, even trickier, what if our text contains periods that do not denote the end of a sentence, but rather some other punctuation, like the period after *Mr.* or *Mrs.*? To work with this type of text, NLTK offers the `sent_tokenizer()`.  It works much like the `word_tokenizer`, but breaks apart text as sentence chunks, and is smart enough to know where the sentence breaks should be.  An example of using `sent_tokenzier` is as follows:

![sentence4](Images/sentence_sent_tokens.PNG)

</details>
</blockquote><br>
</details>

<details>
<summary>What are Stopwords?</summary><br>

Stopwords are considered words that hold no relevance to the outcome. In the English language, words like, _is_, _the_, and  _it_ are considered extraneous. They are words that are used in proper grammar, but they hold no bearing on the meaning of the sentence. As part of preprocessing or cleaning data for NLP, it's important to remove these words so that unnecessary bias doesn't weigh our model down. NLTK has built-in lists of stopwords in multiple languages and provides methods for extracting these words simply.
<blockquote>
<details><summary>Examples of Stopwords:</summary><br>

We can view the built-in list of English stopwords like this:

![stopwords_english](Images/stopwords_english.PNG)

Similarly, you can invoke other languages. For example, here we look at French stopwords:

![stopwords_french](Images/stopwords_french.PNG)
</details>
<details><summary>Usage:</summary><br>

Once we have our stopwords, we can remove them using a for loop. First, we store our stopwords as a set in a variable. The `set` data structure creates an unordered list with duplicates removed. Sets make it easy to compare the contents of lists to find their differences:

```python
sw = set(stopwords.words('english'))
```
We can then run a for loop with this list to remove the stopwords:

![sentence_stopwords](Images/sentence_sw.PNG)

</details>
<details><summary>Custom Stopwords:</summary><br>

In certain cases, we may have additional words we need to remove. Let's suppose the words `Dylan` and `Eli` are not necessary for our NLP work, and we wish to add them to our stopwords. We can add these words to our stopwords list as follows:

```python
sw = set(stopwords.words('english'))
updated_sw = sw.union({'Dylan', 'Eli'})
```
We can then run a for loop with this new list to remove the stopwords, which now include `Dylan` and `Eli`. As you can see in our output, this was successful:

![sentence_stopwords](Images/sentence_new_sw.PNG)
</details>
</blockquote><br>
</details>

<details>
<summary>What is Regex and how is it used?</summary><br>

<blockquote>
<details>
<summary>What it is:</summary><br>

Regex stands for *regular expression*, and it allows us to search for text using very specific patterns. It can be intimidating at first glance, but it's well worth the little study and persistence required to conquer it, especially in cases of NLP usage. Consider using the find and replace option in your Word processor - it works great for finding specific text, but what if your query is more complex?  Perhaps you are looking for someone's name, and you can only remember that the last name ends with *b*. Regex lets you find that!

</details>

<details>
<summary>How it's used:</summary><br>

Before we tokenize, we use regex to get clean token data. Let's apply regex to the following sentence: *"Dylan and Eli love playing video games. They have lots of favorites."*

First, we import the `re` python module, and compile with the pattern we are searching for. In this case, we are searching for any character that is not a letter. The `^` symbol indicates *not*. `A-Z` and `a-z` indicate any upper or lower case letter, and the empty `space` at the end indicates a `space`. When we compile using `^A-Za-Z `, we are looking for any character that is not an upper or lower case letter, or a space. We then use `.sub` to substitute something new in the place of any matches. In the example below, we are substituting `''` (which is essentially nothing) for any matches, which results in the deletion of that character:

<img src='Images/sentence_regex1.PNG' width=700>

Then we can tokenize our sentence, leaving us with clean token data that has no non-alphanumeric characters:

<img src='Images/sentence_regex2.PNG' width=600>

</details>

<details>
<summary>How to learn more:</summary><br>

Here are some great resources to get you started:

* For a gentle introduction from Python click [here.](https://docs.python.org/3/howto/regex.html#regex-howto)

* For an intro with practice prompts, try [this *Google for Education* module.](https://developers.google.com/edu/python/regular-expressions)

* For a quick glance cheat sheet click [here.](https://www.debuggex.com/cheatsheet/regex/python)

* For hands-on practice click [here](http://play.inginf.units.it/#/) or [here.](https://www.hackerrank.com/domains/regex)

</details>
</blockquote><br>

</details>

<details>
<summary>What is Lemmatization and why do I need it?</summary><br>

Lemmatization is the process of decomposing a word to its root; for example, the lemmatized word *busiest* would have a root of *busy*. NLTK provides in-built functionality for this process. The default for this function is to convert plural nouns to singular, but verbs and adjectives can also be converted. To use the function, we import the module and instantiate the object as follows:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
```

We can then call on the function by using the method `.lemmatize()`. In the following example we will lemmatize the sentence:  *"Dylan and Eli love playing video games. They have lots of favorites."*. The tokenized form of this sentence is as follows:
```python
['dylan',
 'eli',
 'love',
 'playing',
 'video',
 'games',
 '.',
 'lots',
 'favorites',
 '.']
```
To properly lemmatize the `sentence_tokenized` object:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

result = []
for word in sentence_tokenized:
    word = lemmatizer.lemmatize(word)
    result.append(word)
```
You can see in the following image, that compared to the original output, the new output has converted all plural words to singular:

<img src = 'Images/lemmatize_sentence.png' width = 400>

A more concise way to generate this new list is with a list comprehension. The results are the same:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

result = [lemmatizer.lemmatize(word) for word in sentence_tokenized]
```
</details>

<details>
<summary>What are N-grams and why do I need them?</summary><br>

<blockquote>
<details>
<summary>What they are:</summary><br>

Ngrams are word groupings that are grouped by **N** number of words. For example, let's use part of our original sentence object: *Dylan and Eli love playing video games.* If we grouped this sentence into bigrams (groups of 2 words), the division would be:

*Dylan and*,<br>
*and Eli*,<br>
*Eli love*,<br>
*love playing*,<br>
*playing video*,<br>
*video games.*<br>

</details>
<details>
<summary>How to find them programmatically:</summary><br>

To get the ngram count of a text using NLTK, we must first tokenize our text using `word_tokenizer`:

Input:
```python
from nltk.tokenize import word_tokenize

sentence = 'Dylan and Eli love playing video games.'
sentence = word_tokenize(sentence)
print(sentence)
```

Output:
```python
['Dylan',
 'and',
 'Eli',
 'love',
 'playing',
 'video',
 'games',
 '.']
```

We can then use NLTK to work with ngrams as follows:

Input:
```python
from nltk.util import ngrams
from collections import Counter

Counter(ngrams(sentence, n=2))
```
Output:
```python
Counter({('Dylan', 'and'): 1,
         ('and', 'Eli'): 1,
         ('Eli', 'love'): 1,
         ('love', 'playing'): 1,
         ('playing', 'video'): 1,
         ('video', 'games'): 1,
         ('games', '.'): 1,
```

The output is a dictionary of values that hold our two word combinations and the number of times those two words appear together.
</details>
<details>
<summary>Why they're important:</summary><br>

Ngrams give NLP models more predictive power by revealing the context of words through analysis of their patterns. Humans innately understand the context of language by processing a sentence as we hear it.  We can tell by tone and inflection if the statement is a question or exclamation, and we can tell by word placement if a statement is positive or negative.  Ngrams give computers a similar ability by looking at groups of words. For example, let's use the following sentence: *Let's hammer out the details.*. The bigrams for the sentence are:

*Let's hammer*,<br>
*hammer out*,<br>
*out the*,<br>
*the details*<br>

Ngrams give context to this statement by looking at how the meaning changes when words are grouped in certain ways. The word *hammer* in this instance has bigrams of *Let's hammer* and *hammer out*.  The words *Let's* and *out* gives context that *hammer* in this instance is being used as a verb. The bigrams *hammer out* and *the details* might also tell our model that the word *hammer* is not being used literally, but rather in a context of clarification.

If instead, our sentence was *I need the hammer*, then having the word *the* preceding the word *hammer* will give the context that hammer in this case is a noun.  Were the sentence *Let's hammer out the details...not!*, then the word *not* would negate the sentence and also hint at sarcasm.  Both examples show how a slight change in pattern and word order can alter the entire context of a sentence.  Ngrams help models pick up on these cues.





</details>
</blockquote><br>

</details>

<details>
<summary>What is a corpus?</summary><br>

In linguistics and NLP, _corpus_ refers to a collection of texts that may be formed of a single language of texts or can span multiple languages. It can be thought of as a dataset that is specific to NLP tasks. Corpora are vital for NLP, as they are used for benchmarking a model's performance, NLP testing, and because effective NLP requires large quantities of text-based data that include as many words as possible. The larger the corpus (dataset), the more likely low-frequency words are to be included in the text.

There are numerous well-known corpora used in NLP, some are general for language-based applications, and some are more specialized for task-specific applications. For example, when working on sentiment analysis projects, you could use the IMDB Reviews or Yelp Reviews corpora.

For more info on corpora, how they work in NLP and where you can find corpora to use in your own projects click [here.](https://devopedia.org/text-corpus-for-nlp)

</details>

<details>
<summary>What is TF-IDF?</summary><br>

Term Frequency * Inverse Document Frequency, or TF-IDF for short, is a weighting factor intended to measure how important a word is to a document in a corpus. It is calculated by combining the Term Frequency (TF) and the Inverse Document Frequency (IDF) to get a weighted value.

Term frequency (TF) is the count of the word in a document of the corpus. Inverse document frequency (IDF) is the number of documents the word appears in throughout the corpus. An increase in TF will make the TF-IDF score go higher, because the more often a word is counted, it can be considered to be more relevant. An increase in IDF will make the TF-IDF score go lower, because the more often a word appears throughout all the documents, it is considered more common and irrelevant.

The higher the TF-IDF score, the more common the word, the lower the TF-IDF score, the more unique (relevant) the word.
<blockquote>

For example:

If the word ***play*** appears **500** times in my **10,000** word document then the TF is high:  **`500 / 10,000 = 0.05`**.

If I have **10,000** documents and ***video*** only appears in **10** of them, then IDF is low: **`LOG(10,000 / 10) = 3`**

In this example, the TF-IDF is: **`0.05 * 3 = 0.15`**.

In the following list of words with TF-IDF values, the word *games* has the highest score, meaning it is a more relevant word than *play* or *video*.

|Word|TF-IDF|
| :----: | :----: |
|*play*|0.15|
|*video*|0.32|
|*games*|0.47|

</blockquote><br>
</details>

<details>
<summary>What is the difference between NLTK and spaCy?</summary><br>

The primary difference between NLTK and spaCy is that NLTK uses a rule-based approach, and spaCy uses a statistical-based approach.

With a rule-based approach, the model deterministically draws conclusions from the text using the rules of the selected language. With NLTK, the word *sick* is negative based on rules that dictate that relationship. With a statistical approach, machine learning can be used to make decisions using the context of the text. SpaCy might notice that the word *sick* is used in a context that implies a positive relationship; for example, *That steak was grilled to perfection! It was sick!*

Additionally, NLTK was built with research and education in mind. It's a great resource for exploring your text data and conducting analyses; however, all data is represented as strings, which can make it more difficult to work with on a larger scale. SpaCy was built with production performance in mind and tends to be faster than NLTK. All data with SpaCy are represented as objects, and more task-based functionality is provided.

</details>
<details>
<summary>What is the difference between POS Tagging and Dependency Parsing?</summary><br>

Part of speech tagging (POS tagging) is the process of labeling each word or token in a sentence as its part of speech (noun, verb, adjective), while dependency parsing takes those words and determines the relationships between each. Dependency parsing is the step that comes after POS tagging.

If we were to POS tag and dependency parse the following sentence:
`'Dylan and Eli love video games.'`, the results would look like this:
<img src='Images/sentence_dependencies.PNG' width = 900>

</details>


© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
