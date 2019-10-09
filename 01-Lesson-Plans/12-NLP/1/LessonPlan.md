## 12.1 Lesson Plan—Intro to Natural Language Processing (NLP)

---

### Please take the Mid-Course Instructional Staff Survey if You Haven't Yet

Trilogy, as a company, values transparency and data-driven change quite highly. As we grow, we know there will be areas that need improvement. It’s hard for us to know what these areas are unless we’re asking questions. Your candid input truly matters to us, as you are key members of the Trilogy team. In addition to the individual feedback at the end of lesson plans, we would appreciate your feedback at the following link if you have not already taken the mid-course survey:

[Instructional Staff Survey](https://docs.google.com/forms/d/e/1FAIpQLSfYVe6jUQwDoXferzGqfd3LZ1k0i_RWzgwccd1f5arSXg2pzA/viewform)

### Overview

Welcome to the natural language processing unit! NLP is an exciting area of machine learning research and is used in a variety of contexts, from algorithmic trading to chatbots. Today's class will explore what NLP is and give students a solid foundation on preprocessing documents for NLP, as well as introduce them to some simple analytical methods.

### Class Objectives

By the end of the class, students will be able to:

* Understand what NLP is, why we use it.

* Understand and be able to implement the NLP workflow.

* Demonstrate an ability to tokenize texts into sentences and words, including handling punctuations and non-alphabetic characters gracefully.

* Implement lemmatization and stopwording with the understanding of pros and cons of various choices.

* Experiment with a few ways of counting tokens and displaying the most frequent ones.

* Define the concept of ngrams and implement with Scikit-learn.

* Create a word cloud to show most frequent terms in a text.

### Instructor Notes

* There is plenty of jargon in NLP. While we try to explain things in plain English as often as possible, some terms of art such as **token** or **corpus** are inescapable. One option for helping keep all the new terms straight is writing down unfamiliar terms on a slide or whiteboard so that students can refer to it as needed.

* Each step in this lesson ties into the next, and every section is critical to learn for students to be able to implement the NLP workflow. Pause and ask for questions often.

* Students may expect to start off doing cool things like text modeling or sentiment analysis, and that's OK—these are coming in the next couple of lessons! However, it's good to remind them that preprocessing text, like any other kind of data, is critical to prevent the garbage in, garbage out phenomenon.

* Have your TAs keep track of time with the [Time Tracker.](TimeTracker.xlsx)

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 12.1 Slides](#).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

**Files**

* [Lesson 12.1 Slides](#)

Welcome students back to class and explain that today is the start of the NLP unit. We'll talk about what NLP is and how it's used in finance in just a little bit, but first pose the following question.

* When was the last time that a student made a decision—could be financial, career, or purchase—based on what they read in a news story? What about the story made them want to make that decision?

    **Sample answer**: I bought 10 shares of TSLA because of a news article about sales of the Model 3. The tone of the story—optimistic—as well as the specific numbers they cited made me bullish about the company.

Take a few answers from volunteers (or call on a couple of students).

* Common answers might include statistics cited in a story, something novel that was described, or the tone in which the author wrote about something.

* Scaling this process with computers—reading and understanding the text of documents—is a key task in NLP and is a central use case in financial applications.

* Computers don't understand the stories in the way that we do, but they can identify key features—like the ones given by students—and make decisions based off those features.

Hopefully, your students are excited and ready to dive into the content at this point! Open the slides for this lesson and begin the next section.

---

### 2. Instructor Do: Intro to NLP (10 min)

**Files**

* [Lesson 12.1 Slides](#)

Open the slides and be sure to hit on the following talking points. Pause after each slide for questions.

* Our objectives today are focused on preprocessing—the stage of the NLP workflow when written documents are transformed into units of data that are more easily processed by a computer.

* NLP spans a wide field of research that intersects computer science, statistics, linguistics, and other disciplines. Understanding and generating human language are two large tasks that encompass many smaller tasks—voice recognition, optical character recognition, summarization, topic representation, etc, etc.

* Finance-specific use cases have mostly been centered around using NLP for quantitative trading. Other settings include fraud detection and chatbots for client interaction (which we will introduce in the next unit).

* The NLP workflow is characterized by four steps: preprocessing, extraction, analysis, and representation. It's not unlike a typical machine learning workflow for any type of data. However, unstructured text data can take much more work to get into usable form than structured, numerical data.

Ask students if they have any questions about NLP in general or the direction of today's class. If not, it's time to move on to the first topic: tokenization.

---

### 3. Instructor Do: Tokenization (10 min)

This activity introduces students to tokenization, the process with which we break down documents into smaller units of analysis. Tokenizing is crucial because many of the NLP techniques we'll learn about, including frequency analysis and sentiment analysis, use word-, phrase-, or sentence-level chunks instead of the entire document. Students will use NLTK (Natural Language Toolkit) functions to split documents into sentences and words. Students will also be introduced to the corpora made available by NLTK, specifically the Reuters Corpus, a collection of financial news stories.

**Files:**

* Solved: [tokenization.ipynb](Activities/01-Ins_Tokenization/Solved/tokenization.ipynb)

* Unsolved: [tokenization.ipynb](Activities/01-Ins_Tokenization/Unsolved/tokenization.ipynb)

Depending on your comfort level, either walk through the solved version or live-code with the unsolved template. Point out that NLTK includes several collections of documents that can be accessed through the corpus module (students may have to download these collections if they did not download all the NLTK data as indicated at the start of this lesson plan). One of these is the Reuters news corpus, which includes financial news stories and is grouped by topic, or "category."

Highlight how we can find articles by topic and then use a single article for practicing tokenization by using the corpus object:

```python
reuters.fileids(categories='crude')
article = reuters.raw('test/14829')
```

Point out that the idea of tokenization is very simple. First, we decide the unit of text we want to work with, whether that's a sentence or word (other units are possible, but harder to define consistently). Next, we look for strings that signal a boundary, or a break between one unit and the next. For words, this might be spaces. For sentences, it might be periods. Ask students how they might proceed to then do the actual split.

We can use Python's native string split function to break apart text into smaller units, or tokens.


```python
## simple sentence tokenize
article.split('.')
## simple word tokenize
sent.split(' ')
```

However, these simple methods aren't very good at covering many potential types of boundaries. For example, sentences don't just end with periods—sometimes they have exclamation marks, question marks, or no punctuation at all. It's possible, but annoying, to account for all these cases. Luckily, NLTK provides us with tokenization methods that do this for us. Walk through the sent_tokenize and word_tokenize methods.

Note that even with NLTK's functions, we won't get perfect results all the time. For example, while NLTK's word_tokenizer is pretty good at separating words and punctuation that are not separated by spaces, it does not separate words with forward slashes like "supply/demand" below.

![string_split_tokenization](Images/string_split_tokenization.PNG)

![nltk_tokenization](Images/nltk_tokenization.PNG)

Ask students to give an example of one type of analysis that they can do with the tokenized sentences and words. Prompt students to think about what else they might need to make the tokens cleaner for the analysis they have in mind.

---

### 4. Student Do: Tokenizing Reuters (15 min)

In this activity, students will practice sentence and word tokenization on some articles from the Reuters Corpus and place the results in a Pandas DataFrame.


**Instructions:**

* [README.md](Activities/02-Stu_Tokenizing_Reuters/README.md)

**Files:**

* [tokenizing_reuters.ipynb](Activities/02-Stu_Tokenizing_Reuters/Unsolved/tokenizing_reuters.ipynb)

---

### 5. Instructor Do: Review Tokenizing Reuters (5 min)

**Files:**

* [tokenizing_reuters.ipynb](Activities/02-Stu_Tokenizing_Reuters/Solved/tokenizing_reuters.ipynb)

Begin by explaining that when we perform NLP tasks, we're often doing it on many documents at once. This is one reason why keeping everything in a DataFrame is a good idea: it allowed us to keep track of the various versions of any given document, and it allows us to add metadata—such as the file ID of the article in this case—to each document in a corpus.

Open the [solved file](Activities/02-Stu_Tokenizing_Reuters/Solved/tokenizing_reuters.ipynb), and discuss the following points:

* Unlike in the demo, we want to tokenize multiple articles. Since we know how to get one article in a given category, we should be able to get all of the articles under category CPI and store them in a list with a simple for loop.

```python
raw_stories = []
ids = []
for id in cpi_ids:
    raw_stories.append(reuters.raw(id))
    ids.append(id)
```

* Just as with the raw articles, we can store sentences in a list. Note that once we apply sent_tokenize to each article, we get a list of sentences back. So, the sentence tokenized list we create is actually a list of lists.

![sentences_list_of_lists](Images/sentences_list_of_lists.PNG)

* The word tokenized list is a little trickier to create. Recall that the sentences are stored in a list of lists. If we apply word_tokenize to each of these lists and try to store the results in another list, we'll get three layers of lists: the first of which are articles, the second of which are sentences, and the third of which are words. The activity asks for a list of tokenized words for each article, which we create with two loops.

```python
# word tokenize all sentences
word_tokenized = []

for story in sentence_tokenized:
    # get all for each article, which is already sentence tokenized
    words = []
    for sent in story:
        words = words + word_tokenize(sent)
    # append all words for each article to the word_tokenized list
    word_tokenized.append(words)
```

---

### 6. Instructor Do: Stopwords (10 min)

This activity introduces the concept and implementation of stopwords. In English, there are many words that are important to grammar and expression but have no topical significance—these include some of the most common words in the language, such as "is," "her," "for," etc. In NLP, these words are called stopwords. For many use cases in which we hope to summarize the contents of a corpus—such as frequency analysis or topic modeling, for example—we want to take these words out in preprocessing so they don't distract from the topically important words and phrases. We will also take a look at a way of stripping out non-alphabetic characters, which we might want to do for a similar reason.

**Files:**

Solved: [stopwords.ipynb](Activities/03-Ins_Stopwords/Solved/stopwords.ipynb)

Walk through the notebook, taking care to allow time for students to look at the output of each step.

For simplicity's sake, we're only going to use one sentence from the article to demonstrate stopwording. Note that these techniques can be applied to entire documents or corpora as well.

Ask students to familiarize themselves with NLTK's list of stopwords. What others can they think of that might be added? Could stopwords for one domain be ill-suited for another (for example, might you want to ignore certain words in finance documents that you wouldn't want to ignore in documents about history)?

We can strip a word_tokenized list of stopwords with the following list comprehension:

```python
sw = set(stopwords.words('english'))
first_result = [word.lower() for word in words if word.lower() not in sw]
```

Two important notes here: First, we choose to instantiate the list of stopwords as a set because a set is more efficient computationally than a list when we want to determine whether or not a word exists in it. This is not a big difference when we only want to do this once, but if you have large numbers of documents and words, the time efficiency can become significant. Second, we want to use the .lower() string function to make all words in the list lowercase when we evaluate them because stopwords are only in lowercase. We can output the words either in their regular case or in all lowercase—usually, the latter is preferred because this is one more way of normalizing words. This becomes important if we're doing something like frequency analysis because words like "orange" and "Orange," in most cases, mean the same thing regardless of capitalization.

![stopwords1](Images/stopwords1.PNG)

Have students take a look at the result after the sentence has been "stopworded." Are there other words in there that are not informative? If so, we can define our own list of custom stopwords and join these to the NLTK list when we perform this step of preprocessing:

```python
sw_addon = {'said', 'mln', 'kilolitres','kl'}
second_result = [word.lower() for word in words if word.lower() not in sw.union(sw_addon)]
```

Note that the union function here combines the unique elements of the two sets.

![stopwords2](Images/stopwords2.PNG)

Once again, have students take a look at the result. We've gotten rid of the words that are uninformative, but what about the numbers and punctuation at the end? For most use cases, these characters are also of little use. It's possible to get rid of them using the stopwords methodology, but this would involve entering every combination of numbers and punctuation that exists in the corpus, and that's unrealistic.

Instead, we're going to make use of regular expressions. Direct students to this resource for learning more about regular expressions and how they're implemented in Python: https://docs.python.org/3/library/re.html. For now, though, go through the following code:

```python
regex = re.compile("[^a-zA-Z ]")
re_clean = regex.sub('', sentence)
```

Regex substitution here takes two steps. In the first, we compile a pattern to match for. In this case, we want to match all characters that are not a letter or a space (denoted by the caret followed by lower and uppercase letters). In the second, we use the .sub() function to substitute out whatever matches that pattern in the string we want to clean. Important: stress to students that this step should occur **before** the text is word tokenized.

Finally, have students take a look at the results of regex cleaning followed by the stopwording that we did before.

![stopwords3](Images/stopwords3.PNG)

---

### 7. Student Do: Crude Stopwords (15 min)

In this activity, students will practice creating a function that strips non-letter characters from a document and then applies stopwording.

**Instructions:**

* [README.md](Activities/04-Stu_Crude_Stopwords/README.md)

**Files:**

* [crude_stopwords.ipynb](Activities/04-Stu_Crude_Stopwords/Unsolved/crude_stopwords.ipynb)

---

### 8. Instructor Do: Review Crude Stopwords (10 min)

**Files:**

* [crude_stopwords.ipynb](Activities/04-Stu_Crude_Stopwords/Solved/crude_stopwords.ipynb)

Reiterate that stopwording is very domain and circumstance specific. Using the same set of stopwords for every corpus is rarely a good idea. The NLTK set is a good start, but chances are that you'll want to augment it with your own set after inspecting the results.

Note the order in which we apply the regex cleaning, word tokenizing, and stopwording.

```python
def clean_text(article):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")

    re_clean = regex.sub('', article)
    words = word_tokenize(re_clean)
    output = [word.lower() for word in words if word.lower() not in sw]
    return output
```

Read the list of additional words that we decided to drop in the second solved implementation. Ask students if they agree with these and which words they might add or drop from this list.

![crude_stopwords](Images/crude_stopwords.PNG)

Tell students that the extent to which we want to add stopwords is a trade-off. The more stopwords, the fewer words we have to look through in a final analysis. However, this also raises the chances that we delete informative words.

---

### 9. BREAK (15 min)

---

### 10. Instructor Do: Lemmatization (5 min)

Lemmatization is a technique that transforms various morphologies of a word into its base form. This may sound fancy, but it's pretty intuitive. If we're looking to summarize a document with the most frequent words in it, words like "stock" and "stocks" should, for the most part,  mean the same. This is also true for words like "run" and "ran." NLTK's lemmatizer takes words in different forms (past tense, plural, etc.) and transforms them to the base form (present tense, singular).

**Files:**

Solved: [lemmatization.ipynb](Activities/05-Ins_Lemmatization/Solved/lemmatization.ipynb)

Note that the lemmatizer is smart enough to not only transform those words that have simple plural forms, but also those words like "goose" that have complex plurals.

![lemma1](Images/lemma1.PNG)

The lemmatizer does not automatically lemmatize any part of speech; the default is noun, which means that plural forms will be transformed to singular. If you want to lemmatize verbs or adjectives, you can use the **pos** argument to change the default part of speech. So, changing pos to **a** for adjective allows us to lemmatize words like "greater" to their root, "great."

![lemma2](Images/lemma2.PNG)

Note that it's possible to lemmatize every part of speech for any given word—all we need to do is apply the lemmatize function to the word with a different pos argument on each pass. In practice, however, noun lemmatizations are usually enough, since the most informative words for most NLP analyses are nouns. It's also important to note that lemmatization is not a step one would want to apply for any kind of analysis—measures of sentiment would be biased if the words were adjective-lemmatized beforehand, for example.

---

### 11. Student Do: Lemmatize (15 min)

In this activity, create a function that performs stopwording, regex cleaning of non-letter characters, word tokenizing, and lemmatization on each word in the article

**Instructions:**

* [README.md](Activities/06-Stu_Lemmatize/README.md)

**Files:**

* [lemmatize.ipynb](Activities/06-Stu_Lemmatize/Unsolved/lemmatize.ipynb)

---

### 12. Instructor Do: Review Lemmatize (5 min)

**Files:**

[lemmatize.ipynb](Activities/06-Stu_Lemmatize/Solved/lemmatize.ipynb)

For this exercise, the key fact to note is the order in which we apply the various processing steps. Explain to students that it's usually appropriate to lemmatize before stopwording so that the different forms of stopwords are more likely to be caught.

```python
def process_text(article):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    re_clean = regex.sub('', article)
    words = word_tokenize(re_clean)
    lem = [lemmatizer.lemmatize(word) for word in words]
    output = [word.lower() for word in lem if word.lower() not in sw]
    return output
```

---

### 13. Instructor Do: Ngram Counter (10 min)

In this section, we introduce the idea of frequency analysis and ngrams. Like the terms we've thrown about earlier, these are fancy names for pretty basic concepts. Frequency analysis, at its simplest, is simply counting words and phrases. At the most basic level, the words that occur most often in a document (assuming they are not stopwords), will probably give you a good idea of what the document is about. This applies at the corpus level as well. Ngrams are multiple word sequences—the n stands for the number of consecutive words (or tokens) that are included. So a bigram, for example, is two consecutive tokens strung together. We can think of creating ngrams as another way of tokenizing a document.

**Files:**

Solved: [ngram_count.ipynb](Activities/07-Ins_Ngram_Count/Solved/ngram_count.ipynb)

Open the solved notebook and explain the following:

* We use the same preprocessing function that was defined in the previous activity to get a list of processed words.

* We want to count the frequency of individual words in this article. We can use the imported Counter function to create a dictionary-like object that has words as its keys and counts as values (the Counter function can be used to count any elements of an iterable, but in this case we want it to count tokens.) As we can see in the snippet of code below, we can convert the Counter object to a dictionary, a more familiar data type.

```python
word_counts = Counter(processed)
print(dict(word_counts))
```

* The Counter object created by the function of the same name can be used to generate the top *x* words by count in the article using the most_common() function. The argument that we input is the number of most frequent words we want to include.

![counter1](Images/counter1.PNG)

* Although counts of words can sometimes be very informative, they rarely have context. Informative terms often contain two or more words, so being able to look at frequent multi-word terms is also useful.

* Ngrams are multiple word sequences—the n stands for the number of consecutive words (or tokens) that are included. So a bigram, for example, is two consecutive tokens strung together.

* We will be using the ngram function from NLTK (Natural Language Toolkit) to break up the list of words into ngrams.

* The ngram function takes two arguments. The first is the list of tokenized words, and the second is the number of words we want in each token—the "n" in ngram. We can use the same Counter function as before on the results to produce the counts of each ngram and get the most common ngrams.

```python
bigram_counts = Counter(ngrams(processed, n=2))
```

Ask students to notice that the counts of the most common ngrams are much smaller than those of the most common words.

* This should be intuitive—most words are used in very different contexts, so two-word combinations should be less frequent, on average, than the words that make them up. This is one reason that higher-n ngrams are rarely used in practice. Unless the corpus is very large or very repetitive, there are few three-, four-, or five-word sequences that are used frequently.

---

### 14. Student Do: Counter (15 min)

In this activity, students will create a function that preprocesses and outputs a list of the most common words in a corpus.

**Instructions:**

* [README.md](Activities/08-Stu_Counter/README.md)

**Files:**

* [counter.ipynb](Activities/08-Stu_Counter/Unsolved/counter.ipynb)

---

### 15. Instructor Do: Review Counter (5 min)

**Files:**

[counter.ipynb](Activities/08-Stu_Counter/Solved/counter.ipynb)

Open the solved notebook and explain the following:

* We can quickly copy and paste from the previous activity in order to get a preprocessing function that can output lemmatized, stopworded, and tokenized words. We'll use this function as a helper in our main Counter functions.

Go over the first word counter function below line by line, highlighting the following points:

* Given a list of articles as a corpus, we have two options. We can either treat each article separately and clean and count words for each in turn, or we can combine all the articles into one big string and preprocess and count that string all at once. Since the latter is more efficient, both computationally and in terms of lines of code written, we choose that method, which is implemented in the function below.

```python
def word_counter(corpus):
    # Combine all articles in corpus into one large string
    big_string = ' '.join(corpus)
    processed = process_text(big_string)
    top_10 = dict(Counter(processed).most_common(10))
    return pd.DataFrame(list(top_10.items()), columns=['word', 'count'])
```

* The join() method can be used to combine multiple strings into one longer string.

* We next run the defined process_text function over this string to get the list of words needed for the Counter function. Once the most frequent words are selected with most_common, all we need to do is to put them into a DataFrame.

* One way of transforming the dictionary is to turn it into a list of tuples first with the .items() method.

* The bigram Counter function, shown below, is very similar. The difference is that nstead of going right to the Counter function after we preprocess the text, we apply the ngram function first, with 2 as the n argument.

```python
def bigram_counter(corpus):
    # Combine all articles in corpus into one large string
    big_string = ' '.join(corpus)
    processed = process_text(big_string)
    bigrams = ngrams(processed, n=2)
    top_10 = dict(Counter(bigrams).most_common(10))
    return pd.DataFrame(list(top_10.items()), columns=['bigram', 'count'])
```

---

### 16. Instructor Do: Word Cloud (10 min)

Frequency analysis is a useful technique, but counts of words or ngrams are difficult and boring to read through for an audience. If only there was a visualization that can achieve the same purpose, but with some color and flair. Enter word clouds! These visualizations are now pretty common and get their share of flack for not being the most rigorous of methods for visualizing text frequency, but there are still few better alternatives for quickly and viscerally summarizing a text.

**Files:**

[wordcloud.ipynb](Activities/09-Ins_Word_Cloud/Solved/wordcloud.ipynb)

First, we need to import the word cloud library, which will do most of the heavy lifting for this activity. Note that we also import matplotlib's pyplot module; although we won't be using pyplot substantively, because the word cloud library is built on top of the matplotlib library, there are some useful matplotlib functions that we can use to create our word cloud.

We can copy over most of the preprocessing code from previous activities. Alert students to one small but important change—whereas before we were returning a list of words, this time we want to return one string instead. So, as a last step, we use a join to create that string. We still want to lemmatize and stopword, so word tokenizing is necessary as an intermediate step. But, since the word cloud function takes only a single string as an argument, we must join these words back together in the preprocessing function.

```python
def process_text(doc):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    re_clean = regex.sub('', doc)
    words = word_tokenize(re_clean)
    lem = [lemmatizer.lemmatize(word) for word in words]
    output = [word.lower() for word in lem if word.lower() not in sw]
    return ' '.join(output)
```

Creating the word cloud itself is easy—two lines will do it. Tell students that the word cloud function does a lot of things in the background that we've done explicitly, like tokenizing and counting words, and then sizes each word that is displayed based on the frequency with which it appears in the text. Do the words that show up largest here make sense for the topic, "gold"? (It's possible that you'd want to add some additional stopwords here, since some of the largest words don't seem informative in this context.)

![cloud1](Images/cloud1.PNG)

There are many ways to customize your word cloud. Some of the most basic include changing the size and the maximum number of words that appear in it. If we think the cloud above was too crowded, for example, we can reduce the maximum words argument and make it a little bigger.

![cloud2](Images/cloud2.PNG)

---

### 17. Student Do: Gas Cloud (15 min)

In this activity, students will  practice creating a word cloud from a subset of the Reuters Corpus.

**Instructions:**

* [README.md](Activities/10-Stu_Gas_Cloud/README.md)

**Files:**

* [gas_cloud.ipynb](Activities/10-Stu_Gas_Cloud/Unsolved/gas_cloud.ipynb)

---

### 18. Instructor Do: Review Gas Cloud (5 min)

**Files:**

[gas_cloud.ipynb](Activities/10-Stu_Gas_Cloud/Solved/gas_cloud.ipynb)

Review the solved notebook cell by cell, pausing to ask students about their implementations when necessary.

* To create a word cloud, students essentially need only to copy and paste code from the previous demo. Reiterate that sometimes we need to make small changes to our preprocess function depending on what the output is going to be used for. In this case, we need to join the output because the word cloud takes one string as input.

Go over the challenge section next; ask students how they implemented it before reviewing the code.

* We need to create bigrams in order to show them in a word cloud, but how can we do this if the word cloud module automatically word tokenizes any string we give it? One work-around is to use a character to join the two words of each bigram, essentially fooling the word cloud tokenizer to think that they are one word. Here, we use the underscore as the join character.

```python
def process_text_bg(doc):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    re_clean = regex.sub('', doc)
    words = word_tokenize(re_clean)
    lem = [lemmatizer.lemmatize(word) for word in words]
    sw_words = [word.lower() for word in lem if word.lower() not in sw]
    bigrams = ngrams(sw_words, 2)
    output = ['_'.join(i) for i in bigrams]
    return ' '.join(output)
```

* Note that there are many "nonsense" bigrams prominent in this word cloud. Is this a case where adding stopwords can help?

![wordcloud](Images/wordcloud.PNG)

### END CLASS

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
