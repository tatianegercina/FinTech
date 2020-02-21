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
- Talk to Alexa, Siri or Googl Assistant.
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


</details>
</details>

<details>
<summary>What is Lemmatization and Why do I Need It?</summary>


</details>

<details>
<summary>What is a corpus?</summary>
</details>


<details>
<summary>What are N-grams and why do I Need them?</summary>
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
