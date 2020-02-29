# Unit 12: Natural Language Processing

### Helpful Links

* [Natural Language Processing with Python – Analyzing Text with the Natural Language Toolkit](https://www.nltk.org/book/) This online version of the NLTK book is a great reference for all things NLTK.

* [spaCy 101: Everything you need to know](https://spacy.io/usage/spacy-101) This direct link to the spaCy documention is an excellent place to find out all there is to know about spaCy.

* [Word Cloud](https://amueller.github.io/word_cloud/) The wordcloud documentation has everything from command line interface tools to gallery examples of how to make your own, unique word cloud.

---

### Additional Course Resources

* [NLP installation guide](nlp-env-install-guide.md)

---

### FAQs

<details>
<summary>What is Natural Language Processing?</summary><br>

Natural Language Processing (NLP) is the development of technology that works with translating human language components into something a computer can work with. NLP is at work anytime you interact with technology that responds to your language inputs. It can be thought of as processing human language into computer inputs.

Examples include:
* Spell Checker.

* Talking to Alexa, Siri or Google Assistant.

* Voice to text on mobile devices.

Computer speak is very specific; its unambigous, literal, methodical and mathematical. Human language is quite the opposite * Words can share multiple meanings when used in different contexts, despite being spelled the same or sounding the same.

When translating words between languages, direct word for word translation will often sound nonsensical because the order of the words and cultural sayings vary. Even different dialects of the same language can have words or sayings that mean different things depending on your geography.

NLP allows a joining of computer speak with human speak to develop intricate tech that can understand language.

</details>
<details>
<summary>What is Tokenization and why do I need it?</summary><br>

Probably the most basic level of NLP is breaking apart language into smaller chunks. This could be breaking apart a sentence into words, an article into sentences or a book into phrases. This process is called tokenization and it can be thought of as simply stripping down a string using a delimiter as you would in Python using `.split()`.

<blockquote>
<details><summary>Word Tokenization</summary><Br>

In the following example we'll use `.split()` and the a space delimiter to tokenize our sentence:

![Mando](Images/Mando_split.PNG)

This method works ok, but NLP can become much trickier than breaking down a sentence on a single delimiter. You might need to write code that breaks down an entire text into whole phrases on multiple delimiters. Because of this, we can use the Natural Language ToolKit (NLTK) platform to perform our tokenizing. NLTK provides libraries and tools that help with NLP tasks such as text processing. Let's tokenize the same sentence using NLTK's tokenizer, `word_tokenizer()`:

![Mando1](Images/Mando_tokens.PNG)

This method allows us to separate out the puncuation in addition to the words and can be combined with regex to be even more detailed. It is a more concise delivery of the intended outcome.
</details>
<details><summary>Sentence Tokenization</summary><br>

In NLP words are not the only items tokenized. In the following example we'll tokenize a short text into sentences. First we use `.split()` and the period delimiter:

![Mando3](Images/Mando_sent_split.PNG)

This works ok, but we get more concise results using NLTK's `sent_tokenizer()`:

![Mando4](Images/Mando_sent_tokens.PNG)

</details>
</blockquote><br>
</details>

<details>
<summary>What are Stopwords?</summary><br>

Stopwords are considered words that hold no relevance to the outcome. In the English language words like, _is_, _the_, and  _it_ are considered extraneous. They are words that are used in proper grammar but they hold no bearing on the meaning of the sentence. As part of preprocessing or cleaning data for NLP, its important to remove these words so that unnecessary bias doesn't weigh our model down. NLTK has built-in lists of stopwords in multiple languages and provides methods for extracting these words simply.
<blockquote>
<details><summary>Examples of Stopwords:</summary><br>

We can view the built-in list of English stopwords like this:

![stopwords_english](Images/stopwords_english.PNG)

Similarly, you can invoke other languages. For example, here we look at French stopwords:

![stopwords_french](Images/stopwords_french.PNG)
</details>
<details><summary>Usage:</summary><br>

Once we have our stopwords we can remove them using a for loop. First we store our stopwords in a variable:

```python
sw = set(stopwords.words('english'))
```
We can then run a for loop with this list to remove the stopwords:

![mando_stopwords](Images/Mando_sw.PNG)

</details>
<details><summary>Custom Stopwords:</summary><br>

In certain cases we may have additional words we need to remove. Let's suppose that the words `yoda` and `mandalorian` are not necessary for our NLP work and we wish to add them to our stopwords. We can add these words to our stopwords list as follows:

```python
sw = set(stopwords.words('english'))
updated_sw = sw.union({'yoda', 'mandalorian'})
```
We can then run a for loop with this new list to remove the stopwords which now include `yoda` and `mandalorian`. As you can see in our output, this was successful:

![mando_stopwords](Images/Mando_new_sw.PNG)
</details>
</blockquote><br>
</details>

<details>
<summary>What is Regex and how is it used?</summary><br>

<blockquote>
<details>
<summary>What it is:</summary><br>

Regex stands for *regular expression* and it allows us to search for text using very specific patterns. It can be intimidating at first glance, but it's well worth the little study and persistance required to conquer it, especially in cases of NLP usage. Consider using the find and replace option in your Word processor * it works great for finding specific text, but what if your query is more complex?  Perhaps you are looking for someone's name, and you can only remember that the last name ends with *b*. Regex lets you find that!

</details>

<details>
<summary>How it's used:</summary><br>

Before we tokenize, we apply regex. This gives us clean token data. Let's apply regex to our mando sentence: *The Mandalorian has rescued baby Yoda. I do not care if he is not the real Yoda. I am still calling him that.*

First we import the `re` python module, and compile with the pattern we are searching for. In this case we are searching for any character that is not a letter. The `^` symbol indicates *not*. `A-Z` and `a-z` indicate any upper or lower case letter, and the empty `space` at the end indicates a `space`. When we compile using `^A-Za-Z `, we are looking for any character that is not an upper or lower case letter, or a space. We then use `.sub` to substitute something new in the place of any matches. In the example below we are substituting `''` for any matches, which results in the deletion of that character:

<img src='Images/mando_regex1.PNG' width=700>

Then we can tokenize our sentence, leaving us with clean token data that has no non-alphanumeric characters:

<img src='Images/mando_regex2.PNG' width=600>

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

Lemmatization is the process of decomposing a word to its root, for example the lemmatized word *busiest* would be *busy*. NLTK provides in-built functionality for this process. The default for this function is to convert plural nouns to singular, but verbs and adjectives can also be converted. To use the function, we import the module and instantiate the object as follows:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
```

We can then call on the function by using the method `.lemmatize()`. In the following example we will lemmatize the sentence:  *'Of all babies in the many worlds in all the galaxies that make our universe, baby yoda rules all hearts as cutest'*. The tokenized form of this sentence is as follows:
```python
['babies',
 'many',
 'worlds',
 'galaxies',
 'make',
 'universe',
 ',',
 'baby',
 'yoda',
 'rules',
 'hearts',
 'cutest']
```
To properly lemmatize the `baby_Yoda` object:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

result = []
for word in baby_Yoda:
    word = lemmatizer.lemmatize(word)
    result.append(word)
```
You can see in the following image, that compared to the original output, the new output has converted all plural words to singular:

<img src = 'Images/lemmatize_baby_Yoda.png' width = 400>

A more concise way to generate this new list is with a list comprehension. The results are the same:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

result = [lemmatizer.lemmatize(word) for word in new_babyYoda]
```
</details>

<details>
<summary>What are N-grams and why do I need them?</summary><br>

<blockquote>
<details>
<summary>What they are:</summary><br>

Ngrams are word groupings that are grouped by **N** number of words. For example, let's use our original mando sentence: *The mandalorian has rescued baby Yoda.* If we grouped this sentence into bigrams (groups of 2 words), the division would be:

*The mandalorian*,<br>
*mandalorian has*,<br>
*has rescued*,<br>
*rescued baby*,<br>
*baby Yoda.*<br>
</details>
<details>
<summary>How to find them programmatically:</summary><br>

To get the ngram count of a text using NLTK, we must first tokenize our text using `word_tokenizer`:

Input:
```python
from nltk.tokenize import word_tokenize

mando = 'The mandalorian has rescued baby Yoda.'
mando = word_tokenize(mando)
print(mando)
```

Output:
```python
['The', 'mandalorian', 'has', 'rescued', 'baby', 'Yoda', '.']
```

We can then use NLTK to work with ngrams as follows:

Input:
```python
from nltk.util import ngrams
from collections import Counter

Counter(ngrams(mando, n=2))
```
Output:
```python
Counter({('The', 'mandalorian'): 1,
         ('mandalorian', 'has'): 1,
         ('has', 'rescued'): 1,
         ('rescued', 'baby'): 1,
         ('baby', 'Yoda'): 1,
         ('Yoda', '.'): 1})
```

The output is a dictionary of values that hold our two word combinations and the number of times those two words appear together.
</details>
<details>
<summary>Why they're important:</summary><br>

Ngrams help computers to understand the context of language. As humans, we can break apart a sentence quickly to grasp the meaning behind it. For an example, let's use the following sentence: *Let's hammer out the details of our trip*. The bigrams for the sentence are:

*Let's hammer*,<br>
*hammer out*,<br>
*out the*<br>
*the details*,<br>
*details of*,<br>
*of our*<br>
*our trip.*<br>

By using the words before and after other words, the computer gains a better understanding of context. The word *hammer* in this instance has bigrams of *Let's hammer* and *hammer out*. The words *Let's* and *out* gives context that *hammer* in this instance is being used as a verb.

If instead our sentence were *I need the hammer*, then having the word *the* preceding the word *hammer* will give the context that hammer in this case is a noun, thus an entirely different context.

</details>
</blockquote><br>

</details>

<details>
<summary>What is a corpus?</summary><br>

A corpus is a collection of writings, typically involving NLP. It can be thought of as a dataset that is specific to NLP tasks. Corpora are vital for NLP, because effective NLP requires large quantities of text based data that include as many words as possible. The larger the corpus (dataset), the more likely low frequency words are to be included in the text.

There are numerous well known corpora used in NLP, some are general for language based applications, and some are more specialized for task specific applications. For example, when working on sentiment analysis projects, you could use the IMDB Reviews or Yelp Reviews corpora.

For more info on corpora, how they work in NLP and where you can find corpora to use in your own projects click [here.](https://devopedia.org/text-corpus-for-nlp)

</details>

<details>
<summary>What is TF-IDF?</summary><br>

Term Frequency * Inverse Document Frequency, or TF-IDF for short, measures the relevance of a word in the document. It is calculated by combining the Term Frequency (TF) and the Inverse Document Frequency (IDF) to get a weighted value.

Term frequency (TF) is the count of the word in a document of the corpus. Inverse document frequency (IDF) is the number of documents the word appears in throughout the corpus. An increase in TF will make the TF-IDF score go higher, because the more often a word is counted, it can be considered to be more relevant. An increase in IDF will make the TF-IDF score go lower, because the more often a word appears throughout all the documents, it is considered more common and irrevelant.

The calculated value of TF-IDF is a number from 0 to 1. When the score approaches 0, the word is considered more common. When the score approaches 1, the word is considered more unique (relevant).
<blockquote>

For example:

If the word *Yoda* appears 500 times in my 10,000 word document then the TF is high:  `500 / 10,000 = 0.05`.

If I have 10,000 documents and *Yoda* only appears in 10 of them, then IDF is low: `LOG(10,000 / 10) = 3`

In this example, the TF-IDF is: `0.05 / 3 = 0.0167`.

This is most certainly a number approaching 0, and would imply a unique, or relevant word. In this example, because *Yoda* appears frequently throughout the document, but not frequently throughout the set of documents, the TF-IDF is high.

</blockquote><br>
</details>

<details>
<summary>What is the difference between NLTK and spaCy?</summary><br>

The primary difference between NLTK and spaCy is that NLTK uses a rule-based approach and spaCy uses a statistical-based approach.

With a rule-based approach, the model deterministically draws conclusions from the text using the rules of the selected language. With NLTK, the word *sick* is negative based on rules that dictate that relationship. With a statistical approach, machine learning can be used to make decisions using the context of the text. SpaCy might notice that the word *sick* is used in a context that implies a positive relationship, for example *That steak was grilled to perfection! It was sick!*

Additionally, NLTK was built with research and education in mind. It's a great resource for exploring your text data and conducting analyses, however all data is represented as strings which can make it more difficult to work with on a larger scale. SpaCy was built with production performance in mind and tends to be faster thank NLTK. All data with SpaCy is represented as objects and more task based functionality is provided.

</details>
<details>
<summary>What is the difference between POS Tagging and Dependency Parsing?</summary><br>

Part of speech tagging (POS tagging) is the process of labeling each word or token in a sentence as its part of speech (noun, verb, adjective), while dependency parsing takes those words and determines the relationships between each. Dependency parsing is the step that comes after POS tagging.

If we were to POS tag and depedency parse the following sentence:
`'The mandalorian has saved baby Yoda'`, the results would look like:
<img src='Images/mando_dependencies.PNG' width = 900>

</details>
