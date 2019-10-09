## 12.3 Lesson Plan - Text Extraction

---

### Overview

This lesson introduces the concepts of **p**art-**o**f-**s**peech (POS) tagging and **n**amed **e**ntity **r**ecognition (NER). Students will practice both techniques using [spaCy](https://spacy.io/), a model-based tool for natural language processing in Python.

### Class Objectives

By the end of the class, students will be able to:

* Understand spaCy capabilities and where to find documentation.

* Be able to use POS tagged text to extract specific words.

* Use dependency parsed text to extract descriptors.

* Extract specific types of entities from text.

* Correlate text features to real-world series like stock prices.

* Create a dashboard from NLP sentiment features.

### Instructor Notes

* Slack out the [Create and Activate an AWS Account Guide](../../13-AWS-Cloud/Supplemental/1-Create-and-Activate-an-AWS-Account.md). Tell students to complete the AWS account creation and verify it with a TA before the end of Today's class. This should help catch account creation issues outside of the class time.

* It may not be immediately obvious to students why POS tagging and named entity extraction are important techniques in natural language processing. While their outputs will not always be directly used for analysis, these processes are critical for sifting through text to its most important or pertinent aspects.

* Be sure to emphasize the use of correct preprocessing, which is different for every use case - in this class, hardly any preprocessing will be needed.

* The activities today may be challenging for students as they introduce unfamiliar concepts and are very open-ended. Be sure to provider support along with your TA's, and spend some time in review to ask why students made certain choices in their projects.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 12.3 Slides](#).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 mins)

Welcome students back to class. Today's class will introduce a few new concepts, but will also help put everything together that we've learned in this unit. We'll work with spaCy, another useful tool for general-purpose NLP, and go through a few activities that make use of this tool and others from this unit. The activities today should be rewarding and fun, and students are encouraged to think about out of the box approaches to meet the requirements. Pause for questions about either the homework or previous lessons, then open the slides and continue to the introduction on spaCy.

---

### 2. Instructor Do: Intro to spaCy (5 mins)

**Files**

* [Lesson 12.3 Slides](#)

Comment students that to implement POS tagging and named entity recognition (more on these later), we will be using spaCy.

* spaCy is different from NLTK in that it is mainly statistical-based instead of rule-based, meaning that spaCy's core functions depend on language models learned from tagged text instead of programmed rules. This makes spaCy more flexible and in many cases more accurate than some of the NLTK tools.

* We will be using spaCy for part of speech tagging, named entity recognition, and dependency parsing. These tasks are more suitable for model-based solutions because they are complex and depend highly on context.

* In addition, spaCy also provides tools for tasks like tokenization and lemmatization, which we've already learned with NLTK, and creating word vectors, which is beyond the scope of this unit but is a foundation for deep learning for NLP.

* In comparison to NLTK, spaCy's language models trades off accuracy for speed, so if the corpus is large then students may prefer a simpler, rule-based solution.

Ask students to check out spaCy's documentation at https://spacy.io/usage

---

### 3. Instructor Do: POS Tagging and Dependency Parsing (10 mins)

This activity introduces students to two important concepts that add grammatical features to text. Part-of-speech tagging is intuitive - each word in a sentence is designated a grammatical part of speech, such as noun, verb, or adjective. Dependency parsing follows this step. Adjectives describe nouns, adverbs describe verbs, nouns can be the subject or object of verbs, and so forth. Each sentence is made of not just the words that it contains but also the relationships that are implicit between them, and a dependency parser is an NLP tool that tries to make these relationships explicit.

**Files:**

* Solved: [pos_tagging.ipynb](Activities/01-Ins_POS_Tagging/Solved/pos_tagging.ipynb)

Go through the demo line by line, pausing for questions and highlighting these points.

* Notice that we need to load the language model before using spacy's various NLP tools. If the text we wanted to analyze was in a foreign language, we'd need to load a different model.

* spacy tokenizes each word and stores the POS and dependency data inside each token. To access them, we need to iterate through each token and access its pos_ attribute.

* Filtering words by their part of speech is simple - we can use a loop, or even more easily, a list comprehension with a conditional like below.

```python
[token.text for token in sent if token.pos_ == 'NOUN']
```

* Similar to POS, we can print the dependencies of each word. However, because dependencies are relationships, this view will not tell us much. Instead, we can use `displacy`, a module that visualizes attributes generated by spacy, to view the relationships of words in a sentence.

* If we want to check what word a token is describing or otherwise related to, we can use the .head attribute. Using conditionals in a list comprehension, we can filter for adjectives that describe a particular word, as we do in the final cell of the notebook.

```python
[token.text for token in sent if (token.head.text == 'cow' and token.pos_ == 'ADJ')]
```

---

### 4. Students Do: Describing America (15 mins)

In this activity students will use the inaugural address corpus from NLTK and spacy's parsing and tagging modules to analyze the text that presidents have used to describe America.

**Instructions:**

* [README.md](Activities/02-Stu_Describing_America/README.md)

**Files:**

* [describing_america.ipynb](Activities/02-Stu_Describing_America/Unsolved/describing_america.ipynb)

---

### 5. Instructor Do: Review Describing America (10 mins)

**Files:**

* [describing_america.ipynb](Activities/02-Stu_Describing_America/Solved/describing_america.ipynb)

Open the solved notebook and go over each section of the activity and each code block in turn.

* For the first part of this activity, we want to create a function that returns the most common adjective from each inaugural address. We can make use of the Counter function for this:

```python
def most_freq_adj(text):
    doc = nlp(text)
    adjs = [token.text.lower() for token in doc if token.pos_ == 'ADJ']
    return Counter(adjs).most_common(1)
```

* In the second part of this activity, we want to first discover the most-used adjectives in the whole corpus. We make a small change to the function above so that it returns all adjectives in each text instead of just the most common. Then, we simply make use of the Counter function over all the adjectives.

* Next, we want to track the usage of these frequent adjectives in speeches over time. To do this, we first need to count the occurrence of each word in each speech, which we can do with a function like this:

```python
def get_counts(text, word):
    tok = word_tokenize(text)
    tok = [word.lower() for word in tok]
    return tok.count(word)
```

* Once we get the counts for each word, we can put the three lists in a DataFrame. In order to create a chart over time, though, we need a x-axis with dates. Luckily, the years of the speeches are part of each fileid - we can extract those years and turn it into a DateTime index with two lines of code:

```python
dates = [i.split('-')[0] for i in ids]
adj_df.index = pd.to_datetime(dates)
```

* The chart of word occurrences should look something like this:

![describe](Images/describe1.png)

* For the third part of this activity, we need to make use of the spacy's dependency parsing. The function that we define to extract words that describe "America" is below. Notice that we extract any adjectives that have a "head" (in this case, the word is describing) the word America.

```python
def describe_america(text):
    doc = nlp(text)
    adjs = [token.text.lower() for token in doc if (token.pos_ == 'ADJ' and token.head.text == 'America')]
    return adjs
```

---

### 6. Instructor Do: Named Entity Recognition (10 mins)

This activity introduces students to named entity recognition (NER), a process that extracts specific types of nouns ("named entities") from text. Named entities are often proper nouns, but NER tools often can also extract things like currency, dates, and times. Like POS tagging and dependency parsing, NER gives us a way of being more precise with our text analysis, only extracting the words that meet a specific grammatical or semantic criteria.

**Files:**

* Solved: [ner.ipynb](Activities/03-Ins_NER/Solved/ner.ipynb)

Open the notebook and walk through the code.

* Similar to the tokens that we used to get POS and dependencies, we can access the tagged entities through the .ents attribute and its child attributes, .text and .label_

```python
for ent in doc.ents:
    print(ent.text, ent.label_)
```

* We can also use displacy here to visually examine an article, which makes seeing the named entities a lot easier.

![ner_2](Images/ner_2.PNG)

* Again, like with with POS or dependencies, we can filter for particular types of entities with a list comprehension.

```python
print([ent.text for ent in doc.ents if ent.label_ == 'GPE'])
```

Before moving on to the next student activity, ask the class to search for spacy documentation (https://spacy.io/api/annotation#named-entities) to find out what entity types exist and what each label means.

---

### 7. Students Do: NER Clouds (15 mins)

In this activity students will extract named entities of their own choosing from the Reuters corpus and build a wordcloud from these entities.

**Instructions:**

* [README.md](Activities/04-Stu_NER_Clouds/README.md)

**Files:**

* [ner_clouds.ipynb](Activities/04-Stu_NER_Clouds/Unsolved/ner_clouds.ipynb)

---

### 8. Instructor Do: Review NER Clouds (10 mins)

**Files:**

* [ner_clouds.ipynb](Activities/04-Stu_NER_Clouds/Solved/ner_clouds.ipynb)

Open the solved notebook and walk through the activity code.

* As with most NLP tasks, it's advantageous to manually inspect a few of the documents in a corpus if you're unfamiliar with the corpus in order to understand it better. Here, we can use the displacy tool to make this easier for us.

* Having decided to extract organizations and geopolitcal entities, we can use the following code to extract them from the corpus.

```python
doc = nlp(articles)
entities = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'ORG']]
```

* Before creating the wordcloud, remember that we need to do a little preprocessing. First, the wordcloud only takes in a single string, so we need to join all the entities together. Before doing this, though, we should make all entities lowercase and replace spaces with underscores so that multi-word entities are not split apart.

```python
entities = [i.lower().replace(' ', '_') for i in entities]
```

![ner](Images/ner1.PNG)

Ask students to talk about their own strategies for selecting entity types and whether their selections resulted in informative wordclouds.

---

### 9. BREAK (40 mins)

---

### 10. Instructor Do: Text as Feature (10 mins)

In this activity we'll ask students to remind themselves of the tools and techniques they've learned in this unit and talk about how we can use them to create numerical features (structured data) from text (unstructured data).

Ask the class to recall the lessons of this unit. Call on volunteers to list some of the tools and techniques that we've learned in this unit.

* Techniques include preprocessing, tokenizing, and lemmatizing text; aggregating word counts; creating n-grams; normalizing to tf-idf weights; sentiment analysis; parsing and pos-tagging text; and named entity recognition. Tools include the libraries NLTK, wordcloud, and spacy.

We've learned a lot! Tell the class that it's often not enough to transform text data in the ways that we've done. In order to use this data for classification or prediction, we need to make them features - numerical representations of unstructured text. Ask the class for examples of features that can be created from text documents.

* Some examples of features include: length of document; count of a key word; count of named entities; sentiment scores; percent of words that are adjectives; and total tf-idf score. These features can then be used to, for example, classify a document to a category or predict the effect of a earnings call on stock price.

Let the class know that the remainder of the class will be spent on practicing ways to engineer features from text and then correlating those features to variables of interest in the real world: stock prices, earning results, or investment decisions, for example.

---

### 11. Students Do: Correlating Returns (15 mins)

In this activity students will create a sentiment index from newsapi headlines and correlated it to S&P 500 daily returns, looking for text topic that generates the highest correlation.

**Instructions:**

* [README.md](Activities/06-Stu_Correlating_Returns/README.md)

**Files:**

* [correlating_returns.ipynb](Activities/06-Stu_Correlating_Returns/Unsolved/correlating_returns.ipynb)

---

### 12. Instructor Do: Review Correlating Returns (10 mins)

**Files:**

* [correlating_returns.ipynb](Activities/06-Stu_Correlating_Returns/Solved/correlating_returns.ipynb)

Open the solved notebook. First, ask a volunteer to walk through the code in the headline download function below, explaining the input and output.

* The newsapi allows only a limited number of articles to be accessed for each day, which is why we only use the 20 most relevant articles. It also truncates the full text of the article.

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

Walk through the next few blocks of code, which contain the keywords we chose to look for. Ask the class what other keywords they used, and why they thought those topics might be correlated with Apple stock.

* The function below calculates an average sentiment score for each day for each topic. We chose to take the average of the compound sentiment score as implemented by vader.

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

* After calculating the sentiment scores and merging it with the stock return that we get from the IEX API, we generate the correlation coefficients between each variable in the DataFrame. One useful trick when looking for strong correlations, especially when there are many variables of interest, is to use pandas' style module to visualize the DataFrame as a heatmap.

```python
topic_sentiments.corr().style.background_gradient()
```

  ![corr1](Images/corr1.PNG)

Ask students whether they found topic sentiments that are more closely correlated with AAPL returns. Ask volunteers whether they might expect correlations between sentiment and returns to remain stable over time for a given topic/stock pairing.

---

### 13. Student Do: Crisis Analysis Dashboard (40 mins)

In this mini-project activity, students will use their new sentiment analysis skills in combination to some of the skills they already master such as: Pandas, Pyviz, Plotly Expres and PyViz Panel to create a data visualization dashboard.

Students will analyze sentiment and tone about the news related to the financial crisis of 2008 that where published along the last month fetching articles from the News API. By default, the developer account gives access to news articles up to a month old.

Present the solution demo to students before starting the activity and join TAs to assist students along this activity.

* This activity can be done on teams up to three students.

**Instructions:**

* [README.md](Activities/14-Stu_Sentiment_Dashboard/README.md)

**Files:**

* [sentiment_analysis.ipynb](Activities/14-Stu_Sentiment_Dashboard/Unsolved/sentiment_analysis.ipynb)

* [sentiment_dashboard.ipynb](Activities/14-Stu_Sentiment_Dashboard/Unsolved/sentiment_dashboard.ipynb)

---

### 14. Instructor Do: Review Crisis Analysis Dashboard (10 mins)

**Files:**

* [sentiment_analysis.ipynb](Activities/14-Stu_Sentiment_Dashboard/Solved/sentiment_analysis.ipynb)

* [sentiment_dashboard.ipynb](Activities/14-Stu_Sentiment_Dashboard/Solved/sentiment_dashboard.ipynb)

Start by opening the `sentiment_analysis.ipynb` solution, walk through the solution and highlight the following:

* In this activity, students will use their new sentiment analysis skills, in combination to some of the skills they already master such as: Pandas, Pyviz, Plotly Express and PyViz Panel, that why the _initial imports_ section is quite large.

```python
# Initial imports
import os
from path import Path
import pandas as pd
import numpy as np
import hvplot.pandas
import nltk
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from newsapi import NewsApiClient
from ibm_watson import ToneAnalyzerV3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib as mpl
import panel as pn

plt.style.use("seaborn-whitegrid")
pn.extension('plotly')
```

* It's important to define the `page_size=100` on the News API instance to have more interesting number of news articles to analyze.

  ```python
  crisis_news_en = newsapi.get_everything(
      q="financial AND crisis AND 2008",
      language="en",
      page_size=100
  )
  ```

* When the news articles' sentiments DataFrame is created, a `try-except` block is used to pass any `AttributeError` that could occurs. This is important to have to avoid problems when launching the dashboard web application.

  ```python
  for article in crisis_news_en["articles"]:
      try:
          # Get sentiment scoring using the get_sentiment_score() function
          sentiments_data.append(
              get_sentiment_scores(
              article["content"],
              article["publishedAt"][:10],
              article["source"]["name"],
              article["url"]
              )
          )
      except AttributeError:
          pass
  ```

* The `hvplot.table()` only supports one signature: either all columns are plotted, or a subset of columns can be selected by defining the `columns` parameter explicitly.

  ```python
  pos_news_table = pos_news.hvplot.table(
    columns=["date", "source", "text", "url"],
    width=500
  )
  ```
* On the **Challenge** section, take into account that the `for-loop` to create the DateFrame structure containing the news articles and their tone scoring results will take up to five minutes to complete, so a kind of progress bar is created by printing asterisks on each iteration.

  ![DataFrame creation sample with news articles and tone analysis results](Images/tone_analysis_progress_bar.png)

Explain to students that it's important to create the CSV files on this section to reduce the processing time on the dashboard creation by only reading the final results from the files.

Continue the review activity by opening the `sentiment_dashboard.ipynb` Jupyter notebook, walk through the solution and highlight the following:

* As students did on the PyViz unit homework, on this notebook they have to compile all the plots into functions to be used on a PyViz Panel Dashboard.

* Instead of doing all the sentiment and tone scoring, these functions will load the data from the CSV files previously created.

  * The `news_vader.csv` file with all the news articles and the VADER sentiment scores.

  * The `tone_data.csv` file with the IBM Watson Tone Analyzer results.

  * The `top_words_data.cvs` file with the top 20 words for creating the word cloud based on the bag-of-words method.

  * The `top_words_tfidf_data.cvs` file with the top 20 words for creating the word cloud based on TF-IDF.

On the **Plots Functions** section comments to students the following:

* It's important to include any DataFrame transformation/manipulation code required along with the plotting code.

* Each function should return a Panel pane object that will be used to build the dashboard.

* Any `.show()` methods should be removed from the code.

* The final dashboard could be like the one shown bellow.

  ![Sample dashboard](Images/sentiment_analysis_dashboard.gif)

---

### 15. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35 minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings.

### END CLASS

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
