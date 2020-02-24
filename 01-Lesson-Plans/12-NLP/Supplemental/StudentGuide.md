# Unit 20: Natural Language Processing

## FAQs

<details>
<summary>What is Natural Language Processing?</summary>


<blockquote>
<details>
<summary>In a nutshell:</summary>

Natural Language Processing (NLP) is the development of technology that works with translating human language components into something a computer can work with.   NLP is at work anytime you interact with technology that responds to your language inputs.  It can be thought of processing human language into computer inputs.

Examples include:
- Spell Checker
- Talk to Alexa, Siri or Google Assistant.
- Voice to text on mobile devices
</details>
<details>
<summary>But why?</summary>

Computer speak is very specific; its unambigous, literal, methodical and mathematical.  Human language is quite the opposite - Words can share multiple meanings when used in different contexts, despite being spelled the same or sounding the same.  When translating words between languages, direct word for word translation will often sound nonsensical because the order of the words and cultural sayings vary.  Even different dialects of the same language can have words or sayings that mean different things depending on your geography.
</details>
</blockquote>
</details>
<details>
<summary>What is Tokenization and Why do I Need It?</summary>

Probably the most basic level of NLP is breaking apart language into smaller chunks.  This could be breaking apart a sentence into words, an article into sentences or book into phrases. The process is called tokenization and it can be thought of as simply stripping down a string using a delimiter as you would in Python using `.split()`.

<blockquote>
<details><summary>Word Tokenization</summary>
In the following example we'll use `.split()` and the a space delimiter to tokenize our sentence:

![Mando](Images/Mando_split.PNG)

This method can work fine in some instances, but NLP can become much trickier than breaking down a sentence on a single delimiter.  You might need to write code that breaks down an entire text into whole phrases on multiple multiple delimiters.  Because of this, we use the Natural Language ToolKit (NLTK) platform to perform our tokenizing.  NLTK provides libraries and tools that help with NLP tasks such as text processing.  Let's tokenize the same sentence using NLTK's tokenizer, `word_tokenizer()`:

![Mando1](Images/Mando_tokens.PNG)

This method allows us to separate the words also, but even includes the period at the end.  It is a more concise delivery of the intended outcome.
</details>
<details><summary>Sentence Tokenization</summary>
In NLP words are not the only items tokenized.  In the following example we'll tokenize a short text into sentences.  First we use `.split()` and the a period delimiter:

![Mando3](Images/Mando_sent_split.PNG)

This works ok, but we can get more concise results using NLTK's `sent_tokenizer()`:

![Mando4](Images/Mando_sent_tokens.PNG)

</details>
</details>


<details>
<summary>What are Stopwords?</summary>

Stopwords are considered words that hold no relevance to the outcome.  In the English langugae words such like, _is_, _the_, and  _it_ are considered extraneous.  They are words that are used in proper grammar but they hold no bearing on the meaning of the sentence.  As part of preprocessing or cleaning data for NLP, its important to remove these words so that unnecessary bias doesn't weigh our model down.  NLTK has built in lists of stopwords in multiple language and provides methods for extracting these words simply.
<blockquote>
<details><summary>Examples of Stopwords:</summary>
We can view the built in list of English stopwords like this:

![stopwords_english](Images/stopwords_english.PNG)

Similarly you can call other languages.  For example, here we look at French stopwords:

![stopwords_french](Images/stopwords_french.PNG)
</details>
<details><summary>Usage:</summary>

Once we have our stopwords we can remove them from our list of important using a for loop.  First we store our stopwords in a variable:

```python
sw = set(stopwords.words('english'))
```
We can then run a for loop with this list to remove the stopwords:

![mando_stopwords](Images/Mando_sw.PNG)


</details>
<details><summary>Custom Stopwords:</summary>

In certain cases we may have additional words we need to remove.  Let's suppose that the words `yoda` and `mandalorian` are not necessary for our NLP work and we wish to add them to our stopwords.  We can add these words to our stopwords list as follows:

```python
sw = set(stopwords.words('english'))
updated_sw = sw.union({'yoda', 'mandalorian'})
```
We can then run a for loop with this new list to remove the stopwords which now include `yoda` and `mandalorian`.  As you can see in our output, this was successful:

![mando_stopwords](Images/Mando_new_sw.PNG)




</details>
</details>

<details>
<summary>Is there a place I can find a simple guide to Regex?</summary>


</details>

<details>
<summary>What is Lemmatization and Why do I Need It?</summary>
Lemmatization is the process of removing the added elements of a word to bring it to its root.  NLTK provides in built functionality for this process. The default for this function is to convert plural nouns to singular, but verbs and adjectives can also be converted.  To use the function, we import the module and instantiate the object as follows:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
```

We can then call on the function.  `.lemmatize()` must be used on text that has already been tokenized, otherwise it will break apart your text into a list of single letters.  In the following example we will lemmatize the sentence:  *'Of all babies in the many worlds in all the galaxies that make our universe, baby yoda rules all hearts as cutest'*.  The tokenized form of this sentence is stored in the object `baby_Yoda` and is a list of words as follows:
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

A more concise way to generate this new list is with a list comprehension.  The results are the same:

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

result = [lemmatizer.lemmatize(word) for word in new_babyYoda]
```
</details>


<details>
<summary>What are N-grams and why do I Need them?</summary>

<blockquote>
<details>
<summary>What they are:</summary>
Ngrams are word groupings that are grouped by **N** number of words.  For example, let's use our original mando sentence: *The mandalorian has rescued baby Yoda.* If we grouped this sentence into bigrams (groups of 2 words), the division would be:

*The mandalorian*,
*mandalorian has*,
*has rescued*,
*rescued baby*,
*baby Yoda.*
</details>
<details>
<summary>How to find them programmatically:</summary>
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



</details>


<details>
<summary>What is a corpus?</summary>

A corpus is a collection of writings, whether on a particular subject or by an author.  The corpus of J.K. Rowling's work would include the Harry Potter series, spin-offs like *Fantastic Beasts and Where to Find Them*, and those books written under a pen name such as *Cuckoo's Calling*.

In NLP a corpus can be thought of as a dataset that is specific to NLP tasks.  Corpora are vital for NLP, because effective NLP requires large quantities of text based data that include as many words as possible.  The larger the corpus (dataset), the more likely low frequency words are to be included in the text.

There are numerous well known corpora used in NLP, some are general for language based applications, and some are more specialized for task specific applications.  For example, when working on sentiment analysis projects, you could use the IMDB Reviews or Yelp Reviews corpora.

For more info on corpora, how they work in NLP and where you can find corpora to use in your own projects click [here](https://devopedia.org/text-corpus-for-nlp)

</details>


<details>
<summary>What is Sentiment?</summary>
</details>



<details>
<summary>What is TF-IDF?</summary>
</details>



<details>
<summary>What are Stop Words and How do I use them?</summary>
</details>



<details>
<summary>What is the differency between spaCy and NLTK?</summary>
</details>



<details>
<summary>What are N-grams and why do I Need them?</summary>
</details>


<details>
<summary>What is the difference between POS Tagging and Dependency Parsing?</summary>
</details>
