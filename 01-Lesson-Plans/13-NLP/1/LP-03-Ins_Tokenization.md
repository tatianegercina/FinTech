### 3. Instructor Demo: Tokenization (0:10 mins)

This activity introduces students to tokenization, the process with which we break down documents into smaller units of analysis. Tokenizing is crucial because many of the NLP techniques we'll learn about, including frequency analysis and sentiment analysis, use word, phrase, or sentence level "chunks" instead of the entire document. Students will use NLTK functions to split documents into sentences and words. Students will also be introduced to the corpuses made available by NLTK, specifically the Reuters corpus, a collection of financial news stories. 

**Files:**

* Solved: [tokenization.ipynb](C:\Users\Mike\Documents\fintech\FinTech-Lesson-Plans\01-Lesson-Plans\13-NLP\1\Activities\01-Ins_Tokenization\Solved\tokenization.ipynb)

* Unsolved: [tokenization.ipynb](C:\Users\Mike\Documents\fintech\FinTech-Lesson-Plans\01-Lesson-Plans\13-NLP\1\Activities\01-Ins_Tokenization\Unsolved\tokenization.ipynb)

Depending on your comfort level, either walk through the solved version or live-code with the unsolved template. Highlight the following:

* NLTK includes several collections of documents that can be accessed through the corpus module (students may have to download these collections if they did not download all the NLTK data as indicated at the start of this lesson plan). One of these is the Reuters new corpus, which includes financial news stories and is grouped by topic, or "category."

* Highlight how we can find articles by topic and then use a single article for practicing tokenization by using the corpus object:

```python
reuters.fileids(categories='crude')
article = reuters.raw('test/14829')
```

* The idea of tokenization is very simple. First, we decide the unit of text we want to work with, whether that's a sentence or word (other units are possible, but harder to define consistently). Next, we look for strings that signal a boundary, or a break between one unit and the next. For words, this might be spaces. For sentences, it might be periods. Ask students how they might proceed to then do the actual split.

* We can use Python's native string split function to break apart text into smaller units, or tokens. 


```python
## simple sentence tokenize
article.split('.')
## simple word tokenize
sent.split(' ')
```

* However, these simple methods aren't very good at covering many potential types of boundaries. For example, sentences don't just end with periods- sometimes they have exclamation marks, question marks, or no punctuation at all. It's possible, but annoying, to account for all these cases. Luckily, NLTK provides us with tokenization methods that do this for us. Walk through the sent_tokenize and word_tokenize methods. 

* Note that even with NLTK's functions we won't get perfect results all the time. For example, while nltk's word_tokenizer is pretty good at separating words and punctuation that are not separated by spaces, it does not separate words with forward slashes like "supply/demand" below.

![string_split_tokenization](Images/string_split_tokenization.PNG)

![nltk_tokenization](Images/nltk_tokenization.PNG)

* Ask students to give an example of one type of analysis that they can do with the tokenized sentences and words. Prompt students to think about what else they might need to make the tokens cleaner for the analysis they have in mind.