## 12.3 Lesson Plan—Text Extraction

---

### Overview

This lesson introduces the concepts of part-of-speech (POS) tagging and named entity recognition (NER). Students will practice both techniques using [spaCy](https://spacy.io/), a model-based tool for natural language processing in Python.

### Class Objectives

By the end of the class, students will be able to:

* Understand spaCy capabilities and where to find documentation.

* Be able to use POS-tagged text to extract specific words.

* Use dependency-parsed text to extract descriptors.

* Extract specific types of entities from text.

* Correlate text features to real-world series like stock prices.

* Create a dashboard from NLP sentiment features.

### Instructor Notes

* Slack out the [Create and Activate an AWS Account Guide](../../13-AWS-Cloud/Supplemental/1-Create-and-Activate-an-AWS-Account.md). Tell students to complete the AWS account creation and verify it with a TA before the end of today's class. This should help catch account creation issues outside of class time.

* It may not be immediately obvious to students why POS tagging and named entity extraction are important techniques in natural language processing. While their outputs will not always be directly used for analysis, these processes are critical for sifting through text to its most important or pertinent aspects.

* Be sure to emphasize the use of correct preprocessing, which is different for every use case—in this class, hardly any preprocessing will be needed.

* The activities today may be challenging for students, as they introduce unfamiliar concepts and are very open-ended. Be sure to provide support along with your TAs, and spend some time in review to ask why students made certain choices in their projects.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx).

### Sample Class Video (Highly Recommended)
* To watch an example class lecture, go here: [12.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7400a964-c443-4056-8722-aae900471381) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1x3Wxnv1piynJy3GnoZHBfoyGneRayibAgZhHCRBzs6s/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

Welcome students back to class. Today's class will introduce a few new concepts but will also help put everything together that we have learned in this unit. We will work with spaCy, another useful tool for general-purpose natural language processing (NLP), and go through a few activities that make use of this tool and others from this unit. The activities today should be rewarding and fun, and students are encouraged to think about out-of-the-box approaches to meet the requirements. Pause for questions about either the homework or previous lessons, then open the slides and continue to the introduction on spaCy.

---

### 2. Instructor Do: Intro to spaCy (5 min)

Tell students that to implement POS tagging and named entity recognition (more on these later), we will be using spaCy.

* SpaCy is different from NLTK in that it is mainly statistical-based instead of rule-based, meaning that spaCy's core functions depend on language models learned from tagged text instead of programmed rules. This makes spaCy more flexible and in many cases, more accurate than some of the NLTK tools.

* We will be using spaCy for part-of-speech tagging, named entity recognition, and dependency parsing. These tasks are more suitable for model-based solutions because they are complex and depend highly on context.

* SpaCy also provides tools for tasks like tokenization and lemmatization, which we've already learned with NLTK, and creating word vectors, which is beyond the scope of this unit but is a foundation for deep learning for NLP.

* In comparison to NLTK, spaCy's language models trade off accuracy for speed, so if the corpus is large, then students may prefer a simpler, rule-based solution.

Ask students to check out spaCy's documentation at https://spacy.io/usage

---

### 3. Instructor Do: POS Tagging and Dependency Parsing (10 min)

This activity introduces students to two essential concepts that add grammatical features to text, Part-of-Speech (POS) tagging, and dependency parsing.

**Files:**

* Solved: [pos_tagging.ipynb](Activities/01-Ins_POS_Tagging/Solved/pos_tagging.ipynb)

Open the lesson slides, move to the "POS Tagging and Dependency Parsing" section, and highlight the following.

* Part-of-Speech (POS) tagging is intuitive. Each word in a sentence is designated a grammatical part of speech, such as noun, verb, or adjective. POS tagging categorizes each word in a sentence by its grammatical role in the sentence.

* For example, in the following slide, we have the sentence `Jose made a book collector happy the other day`. POS tagging will tokenize the sentence and add a `label` next to each token, such as `noun`, `verb`, or `adverb` in this example.

  ![pos-tagging-slides-example](Images/pos-tagging-slides-example.png)

* Dependency parsing follows POS tagging. In grammar, a dependency is a notion that words are connected to each other by directed links. For example, adjectives describe nouns, and adverbs describe verbs, nouns can be the subject or object of verbs, and so forth.

* Each sentence is made of not just the words that it contains but also the relationships that are implicit between them. A dependency parser is an NLP tool that tries to make these relationships explicit.

* For example, in the slide, you can note that in the sentence's fragment `a book collector`, the noun `book` has a relationship with `collector` and modifies its meaning and semantics.

  ![dependency-parsing-slides-example](Images/dependency-parsing-slides-example.png)

* Today, you will learn how to use spaCy to conduct this kind of text analysis.

Open the Jupyter notebook, and go through the demo line by line, pausing for questions and highlighting these points.

* We start by importing the `spcacy` library and loading the language model before using spaCy's various NLP tools. If the text we wanted to analyze were in a different language, we would need to load a different model.

  ```python
  # Import spaCy library
  import spacy

  # Load the English language model for spaCy
  nlp = spacy.load("en_core_web_sm")
  ```

* Next, we set a sample sentence to analyze using spaCy.

  ```python
  # Set a sentence to be analyzed using spaCy
  sentence = "The brown cow jumped over the round moon."
  ```

* We use the spaCy language model object `nlp` to tokenize each word and store the POS-tags and dependency data inside each token.

  ```python
  # Tokenize text and parse each token
  tokens = nlp(sentence)
  ```

* To access the POS-tags, we need to iterate through each token and access its `pos_` attribute. Note that each token was parsed using the language model to determine the corresponding tag (presented in uppercase).

  ```python
  # Print POS-Tags for each token
  for token in tokens:
      print(token.text, token.pos_)
  ```

  ```text
  The DET
  brown ADJ
  cow NOUN
  jumped VERB
  over ADP
  the DET
  round ADJ
  moon NOUN
  . PUNCT
  ```

Slack out this link to the class: https://spacy.io/api/annotation#pos-tagging. Explain to students that they can find a complete list that describes all the POS tags in this page.

* Using the POS-tags, we can filter the words using a list comprehension with a conditional, for example, to identify all the nouns in a sentence or text.

  ```python
  # Retrieve all the nouns in the sentence using a list comprehension
  nouns = [token.text for token in tokens if token.pos_ == "NOUN"]

  # Print the nouns in the sentence
  print(nouns)
  ```

  ```text
  ['cow', 'moon']
  ```

* Similar to POS-tags, we can print the grammar dependencies of each word. using the `dep_` attribute.

  ```python
  # Print grammar dependencies
  for token in tokens:
      print(token.text, token.dep_)
  ```

  ```text
  The det
  brown amod
  cow nsubj
  jumped ROOT
  over prep
  the det
  round amod
  moon pobj
  . punct
  ```

* However, because dependencies are relationships, the list view will not tell us much. Instead, we can use `displacy`, a module that visualizes attributes generated by spaCy, to view the relationships of words in a sentence.

  ```python
  # Import the displacy module from spaCy
  from spacy import displacy

  # Show the dependency tree
  displacy.render(tokens, style="dep")
  ```

  ![dependencies-graph](Images/dependencies-graph.png)

* Dependency parsing extracts a dependency parse of a sentence representing its grammatical structure and defines the relationships between “head” words and words, which modify those heads. We can retrieve the head word of each token using the `head` attribute.

  ```python
  # Print the POS-tag and head word of each token
  for token in tokens:
      print(token.text, token.pos_, token.head.text)
  ```

  ```text
  The DET cow
  brown ADJ cow
  cow NOUN jumped
  jumped VERB jumped
  over ADP jumped
  the DET moon
  round ADJ moon
  moon NOUN over
  . PUNCT jumped
  ```

* If we want to check what word a token is describing or otherwise related to, we can also use the .`head` attribute. For example, using conditionals in a list comprehension, we can filter for adjectives that describe a particular word like `cow`.

  ```python
  # Retrieve the adjectives that describe the word "cow"
  cow_describers = [token.text for token in tokens if (token.head.text == "cow" and token.pos_ == "ADJ")]

  # Print describers
  print(cow_describers)
  ```

  ```text
  ['brown']
  ```

Explain to students that this type of text analysis has different applications in the FinTech industry, such as analyzing financial news, investing memorandums, financial analysis reports, and even social media feeds.

Answer any questions before moving on.

---

### 4. Student Do: Describing America (20 min)

In this activity, students will use the inaugural address corpus from NLTK and spaCy's parsing and POS-tagging modules to analyze the words that U.S. Presidents have delivered in their inaugural addresses.

**Instructions:**

* [README.md](Activities/02-Stu_Describing_America/README.md)

**Files:**

* [describing_america.ipynb](Activities/02-Stu_Describing_America/Unsolved/describing_america.ipynb)

---

### 5. Instructor Do: Review Describing America (10 min)

**Files:**

* [describing_america.ipynb](Activities/02-Stu_Describing_America/Solved/describing_america.ipynb)

Open the solved notebook and go over each section of the activity and each code block in turn.

* In the first part of this activity, we use the functions provided by the `inaugural` module to retrieve the document IDs and the text of each inaugural address from the inaugural address corpus.

  ```python
  # Retrieve the IDs of inaugural addresses
  ids = inaugural.fileids()

  # Retrieve the text of inaugural addresses
  texts = [inaugural.raw(id) for id in ids]
  ```

* Note that we use a list comprehension to create the list containing the text of each inaugural address.

* In the second part of the activity, it's worth highlighting that we use POS-tagging to identify the adjectives in the text passed as an argument. All the adjectives are stored in a list created using list comprehension.

  ```python
  # Creates a list with all the adjectives in the text
  adjs = [token.text.lower() for token in doc if token.pos_ == 'ADJ']
  ```

* In the same function, the `Counter` module from the `collections` library is used to pick the most frequent adjective in each text using the `most_common()` function passing `1` as an argument.

  ```python
  # Retrieves the most frequent adjective in the `adjs` list using the Counter module
  most_common_adj = Counter(adjs).most_common(1)
  ```

* To create a list with the most common adjective on each inaugural address, we use the `most_freq_adj()` function into a list comprehension.

  ```python
  adjs = [most_freq_adj(text) for text in texts]
  ```

* This second part of the activity concludes by creating a DataFrame to store the most common adjective per inaugural address.

  ```python
  # Create a DataFrame `df_adjs` with the most common adjective for each inaugural address.
  df_adjs = pd.DataFrame(
      {
          'doc_id':ids,
          'adjective':adjs
      }
  )
  ```

  ![most-common-adjs](Images/most-common-adjs.png)

* In the third part of the activity, our goal is to analyze the most frequent adjectives over time. First, we use the `all_adj()` function to create a Python list `all_adjectives` containing all the adjectives into all the inaugural addresses.

  ```python
  # Create an empty list to store all the adjectives
  all_adjectives = []

  # Use a for-loop to retrieve all the adjectives on each inaugural address and concatenate the adjectives fetched to `all_adjectives`
  for text in texts:
      all_adjectives = all_adjectives + all_adj(text)
  ```

* Note that we use a `for-loop` to create the `all_adjectives` Python list. Inside the loop, we use the plus (`+`) operator to concatenate all the adjectives found in a text using the `all_adj()` function provided. We use the plus operator instead of the `append()` list method to create a list of concatenated single values instead of a list or lists.

* Next, we use the `most_common()` function from the `Counter` module to fetch the three most frequent adjectives used in the U.S. Presidential inaugural address. The `most_common()` function returns a Python list that you should store in a variable called `most_freq_adjectives`.

  ```python
  # Retrieve the three most frequent adjectives
  most_freq_adjectives = Counter(all_adjectives).most_common(3)
  ```

* In order to create the lists having the counts of the three most frequent adjectives, we use the `get_word_counts()` function into list comprehensions. 

  ```python
  # Use list comprehensions to create a list with the counts of each top adjective in the inaugural addresses
  great_counts = [get_word_counts(text,'great') for text in texts]
  other_counts = [get_word_counts(text,'other') for text in texts]
  own_counts = [get_word_counts(text,'own') for text in texts]
  ```

* Fetching the years and the Presidents' last names from the document IDs may be tricky, but this task is easy to face using list comprehensions and the `slipt()` string's method.

  ```python
  # Create a list `dates` with the year for each inaugural address using the file IDs
  dates = [id.split('-')[0] for id in ids]

  # Create a list `presidents` with the last name of each president
  presidents = [id.split('-')[1].split('.')[0] for id in ids]
  ```

* Now that we have all the data about the most used adjectives in the inaugural addresses over time, we create a DataFrame and plot a line chart to analyze how U.S. presidents used them their speech visually.

  ```python
  # Set DataFrame data
  adjectives_data = {
      'president': presidents,
      'great':great_counts,
      'other':other_counts,
      'own': own_counts
  }

  # Create the DataFrame
  df_adjectives = pd.DataFrame(adjectives_data, index=pd.to_datetime(dates).year)
  ```

  ![adjectives-df](Images/adjectives-df.png)

  ```python
  # Use the `df_adjectives` DataFrame to plot frequencies of each adjective over time
  df_adjectives.plot(
      title = "Most Common Adjectives Used in the U.S. Presidential Inaugural Addresses",
      figsize = (10, 5)
  )
  ```

  ![adjectives-plot](Images/adjectives-plot.png)

* Finally, in the fourth part of this activity, you are asked to create a function `describe_america()` to retrieve all the adjectives in a given text. This can be done using the same logic from the helper functions by using a comprehension list.

  ```python
  def describe_america(text):
      """
      This function retrieves the adjectives in the text that describe the head word 'America'.

      Args:
          text (string): The text to analyze.

      Returns:
          adjs (list): A list of the adjectives that describe the head word 'America' in the text.
      """

      # Use the spaCy English language model to tokenize the text and parse each token
      doc = nlp(text)

      # Create a list with all the adjectives in the text that describe the head word 'America'
      adjs = [token.text.lower() for token in doc if (token.pos_ == 'ADJ' and token.head.text == 'America')]

      return adjs
  ```

* The activity ends by using the `describe_america()` function you defined to create a list with all the adjectives used in the inaugural address to describe the word `America``.

  ```python
  # Create an empty list to store de adjectives
  america_adjectives = []

  # Use a for-loop to retrieve all the adjectives that describe the word 'America' on each inaugural address and concatenate the adjectives fetched to `america_adjectives`
  for text in texts:
      america_adjectives = america_adjectives + describe_america(text)

  # Print the list of the adjectives describing the word 'America'
  print(america_adjectives)
  ```

  ```text
  ['productive', 'strong', 'stronger', 'rich']
  ````

Explain to students that this kind of textual analysis could have different applications in the FinTech industry, such as analyzing social media feeds to listen to customers or benchmarking competitors.

Answer any questions before moving on.

---

### 6. Instructor Do: Named Entity Recognition (10 min)

**Corresponding Activity:** [03-Ins_NER](Activities/03-Ins_NER)

This activity introduces students to named entity recognition (NER), a process that extracts specific types of nouns ("named entities") from the text. Named entities are often proper nouns, but NER tools can also extract things like currency, dates, and times. Like POS tagging and dependency parsing, NER gives us a way of being more precise with our text analysis, only extracting the words that meet a specific grammatical or semantic criteria.

**Files:**

* Solved: [ner.ipynb](Activities/03-Ins_NER/Solved/ner.ipynb)

Open the notebook and walk through the code.

* Similar to the tokens that we used to get POS and dependencies, we can access the tagged entities through the .ents attribute and its child attributes, .text and .label_

```python
for ent in doc.ents:
    print(ent.text, ent.label_)
```

* We can also use displaCy here to visually examine an article, which makes seeing the named entities a lot easier.

![ner_2](Images/ner_2.png)

* As with POS or dependencies, we can filter for particular types of entities with a list comprehension.

```python
print([ent.text for ent in doc.ents if ent.label_ == 'GPE'])
```

Before moving on to the next student activity, ask the class to search for spaCy documentation (https://spacy.io/api/annotation#named-entities) to find out what entity types exist and what each label means.

---

### 7. Student Do: NER Clouds (15 min)

**Corresponding Activity:** [04-Stu_NER_Clouds](Activities/04-Stu_NER_Clouds)

In this activity, students will extract named entities of their own choosing from the Reuters Corpus and build a word cloud from these entities.

**Instructions:**

* [README.md](Activities/04-Stu_NER_Clouds/README.md)

**Files:**

* [ner_clouds.ipynb](Activities/04-Stu_NER_Clouds/Unsolved/ner_clouds.ipynb)

---

### 8. Instructor Do: Review NER Clouds (10 min)

**Files:**

* [ner_clouds.ipynb](Activities/04-Stu_NER_Clouds/Solved/ner_clouds.ipynb)

Open the solved notebook and walk through the activity code.

* As with most NLP tasks, it is advantageous to manually inspect a few of the documents in a corpus if you are unfamiliar with the corpus to understand it better. Here, we can use the displaCy tool to make this easier for us.

* Having decided to extract organizations and geopolitical entities, we can use the following code to extract them from the corpus.

```python
doc = nlp(articles)
entities = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'ORG']]
```

* Before creating the word cloud, remember that we need to do a little preprocessing. First, the word cloud only takes in a single string, so we need to join all the entities together. Before doing this, though, we should make all entities lowercase and replace spaces with underscores so that multi-word entities are not split apart.

```python
entities = [i.lower().replace(' ', '_') for i in entities]
```

![ner](Images/ner1.png)

Ask students to talk about their own strategies for selecting entity types and whether their selections resulted in informative word clouds.

---

### 9. BREAK (40 min)

---

### 10. Instructor Do: Text as Feature (10 min)

In this activity, we'll ask students to remind themselves of the tools and techniques they've learned in this unit and talk about how we can use them to create numerical features (structured data) from the text (unstructured data).

Ask the class to recall the lessons of this unit. Call on volunteers to list some of the tools and techniques that we have learned in this unit.

* Techniques include preprocessing, tokenizing, and lemmatizing text; aggregating word counts; creating ngrams; normalizing to TF-IDF weights; sentiment analysis; parsing and pos-tagging text; and named entity recognition. Tools include the libraries NLTK, word cloud, and spaCy.

We have learned a lot! Tell the class that it is often not enough to transform text data in the ways that we have done. In order to use this data for classification or prediction, we need to make them features—numerical representations of unstructured text. Ask the class for examples of features that can be created from text documents.

* Some examples of features include: length of document, count of a key word; count of named entities, sentiment scores, percent of words that are adjectives, and total TF-IDF score. These features can then be used, for example, to classify a document to a category or predict the effect of an earnings call on a stock price.

Let the class know that the remainder of the class will be spent on practicing ways to engineer features from text and then correlating those features to variables of interest in the real world: stock prices, earning results, or investment decisions, for example.

---

### 11. Student Do: Correlating Returns (15 min)

**Corresponding Activity:** [05-Stu_Correlating_Returns](Activities/05-Stu_Correlating_Returns)

In this activity, students will create a sentiment index from News API headlines and correlate it to S&P 500 daily returns, looking for a text topic that generates the highest correlation.

**Instructions:**

* [README.md](Activities/05-Stu_Correlating_Returns/README.md)

**Files:**

* [correlating_returns.ipynb](Activities/05-Stu_Correlating_Returns/Unsolved/correlating_returns.ipynb)

---

### 12. Instructor Do: Review Correlating Returns (10 min)

**Files:**

* [correlating_returns.ipynb](Activities/05-Stu_Correlating_Returns/Solved/correlating_returns.ipynb)

Open the solved notebook. First, ask a volunteer to walk through the code in the headline download function below, explaining the input and output.

* The News API allows only a limited number of articles to be accessed each day, which is why we only use the 20 most relevant articles. It also truncates the full text of the article.

```python
def get_headlines(keyword):
    all_headlines = []
    all_dates = []
    date = '2019-07-24'
    while date > '2019-06-25':
        articles = (newsapi.get_everything(q=keyword,
                                              from_param=date,
                                              to=date,
                                              language='en',
                                              sort_by='relevancy',
                                              page=1))
        headlines = []
        for i in range(0, len(articles['articles'])):
            headlines.append(articles['articles'][i]['title'])
        all_headlines.append(headlines)
        all_dates.append(date)
        date = datetime.strftime(datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1), '%Y-%m-%d')
    return all_headlines, all_dates
```

Walkthrough the next few blocks of code, which contain the keywords we chose to look for. Ask the class what other keywords they used and why they thought those topics might be correlated with Apple stock.

* The function below calculates an average sentiment score for each day for each topic. We chose to take the average of the compound sentiment score as implemented by VADER.

```python
def headline_sentiment_summarizer_avg(headlines):
    sentiment = []
    for day in headlines:
        day_score = []
        for h in day:
            if h == None:
                continue
            else:
                day_score.append(sid.polarity_scores(h)['compound'])
        sentiment.append(sum(day_score) / len(day_score))
    return sentiment
```

* After calculating the sentiment scores and merging it with the stock return that we get from the Alpaca API, we generate the correlation coefficients between each variable in the DataFrame. One useful trick when looking for strong correlations, especially when there are many variables of interest, is to use the Pandas style module to visualize the DataFrame as a heat map.

```python
topic_sentiments.corr().style.background_gradient()
```

  ![corr1](Images/corr1.png)

Ask students whether they found topic sentiments that are more closely correlated with AAPL returns. Ask volunteers whether they might expect correlations between sentiment and returns to remain stable over time for a given topic or stock pairing.

---

### 13. Instructor Do: Machine Learning Review (50 min)

The remainder of today's class is intended to review any topics, activities, or concepts covered in any of the previous machine learning units.

---

### 14. Instructor Do: Structured Review (35 min)

Note: If you are teaching this lesson on a weeknight, save this 35 minute review for the next Saturday class.

Use the entire time to review questions with the students before ending class.

Suggested format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### END CLASS

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
