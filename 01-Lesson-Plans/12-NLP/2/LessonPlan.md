## 12.2 Lesson Plan—How the FinTech Feels

---

### Overview

Today's class will introduce students to **sentiment analysis**, one of the most popular applications of natural language processing (NLP). Normally sentiment analysis is related to marketing, however it's receiving a big attention on FinTech because of its huge spectrum of applications ranging from customer service, competition benchmarking, investment assistance, and news and social media analysis.

In this lesson, students will gain practical experience using the `NLTK` Python library and the **IBM Tone Analyzer** cloud service to analyze sentiments on news feeds.

### Class Objectives

By the end of the class, students will be able to:

* Identify the applications of sentiment analysis for FinTech.

* Retrieve data from news feeds to analyze sentiments and tone.

* Perform data preparation techniques oriented to sentiment analysis.

* Apply natural language processing through `NLTK` and `VADER` to classify news sentiment as positive, negative, or neutral.

* Conduct tone analysis using the **IBM Tone Analyzer** cloud service.

### Instructor Notes

* Slack out the [Create and Activate an AWS Account Guide](../../13-AWS-Cloud/Supplemental/1-Create-and-Activate-an-AWS-Account.md). Tell students to complete the AWS account creation and verify it with a TA before the end of the next class. This should help catch account creation issues outside class time.

* Sentiment analysis is a wide area that has a broad range of tools; this class will cover only a gentle introduction to sentiment analysis fundamentals.

* This lesson includes the use and demonstration of the [News API](https://newsapi.org/), a free API for developers that retrieves metadata for headlines and news. This service requires user registration. The process is quite easy, but have your TAs assist students during the instructor demo activity to be sure students get their API keys.

* Students will use the **IBM Tone Analyzer** cloud service in this class. The registration process could be time-consuming, so be sure to get familiar with the process by your own before class to assist students on the process.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx).

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy."

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Intro to Sentiment Analysis (10 min)

Welcome students to the second day on NLP, this lesson will introduce the fundamentals of **sentiment analysis**, one of the most popular and growing areas of NLP where there are some new tools almost every day. Beyond the buzz, on this initial lecture students will learn what sentiment analysis is as well as how a computer can understand people's feelings.

Follow the _Intro to Sentiment Analysis_ section on lesson slides by highlighting the following points:

* Sentiment analysis is part of NLP. Despite it being quite popular in marketing, it has several applications on FinTech.

* Sentiment analysis is a growing area, so some students could have experience with it or have heard about tools to analyze sentiments from social media and other texts. This lesson will introduce the foundations that will allow students to understand how sentiment analysis works so they will be able to choose the tools that best fit for their analysis purposes.

* Sentiment analysis is not infallible, so take the last three or four minutes of the presentation to discuss with students how sentiment analysis is used in FinTech and the challenges of this NLP area.

---

### 2. Instructor Do: Listen to the FinTech (5 min)

The purpose of this activity is to encourage students to have an open discussion led by the instructor about the applications they envision for sentiment analysis in the FinTech industry.

The introduction to sentiment analysis will offer some context to students about this area of NLP; follow lesson slides and facilitate an open discussion, asking the following questions:

* Can a stock feel sadness if it opens with losses today?

  * **Answer:** A stock can't have feelings, but we can use sentiment analysis to understand the sentiments expressed about a stock in news headlines to support investment decisions.

* Is it possible to your bank account to suggest a travel destinations based on your tweets from last year?

  * **Answer:** If you allow your bank to follow you on Twitter, it's possible it can score the sentiment of your tweets, even the tone you express in your posts. Your bank can give you some travel recommendations to boost your mood for the weekend or to spend some time with your family if it seems you were tweeting to much about how angry your were the last months.

* Can an auction website prevent fraud by analyzing the conversation between a potential buyer and a dealer?

  * **Answer:** Using tone analysis, it's possible to follow the messages between a potential buyer and a dealer and score the emotions they are expressing to prevent a fraud.

* What about your privacy in this sentiment analysis revolution?

  * **Answer:** This is definitely a major concern, you should have consent from people to analyze the sentiment of their written communications and a storage and security infrastructure in compliance with user privacy regulations.

This activity looks to challenge students to think outside of the box and encourages them to dream about future applications of sentiment analysis in FinTech.

---

### 3. Instructor Do: Terms Relevance (Understanding TF–IDF) (15 min)

This activity introduces term relevance from the perspective of TF–IDF (term frequency –inverse document frequency). Also, students will lean how TF–IDF can be implemented using `sklearn`.

Do not invest to much time on the TF–IDF formulas, just explain how they work in general and invest a little more time on the rationale behind these measures and their implementation using `sklearn`.

* [03_Ins_Terms_Relevance.ipynb](Activities/03-Ins_Terms_Relevance/Solved/03_Ins_Terms_Relevance.ipynb)

Open the lesson slides and move to the **Terms Relevance (Understanding TF–IDF)** section, highlighting the following points:

* In a world of words, analyzing text can be confusing because of speech's complexity. That's why measuring term relevance is useful—it offers a way to understand how important a word is to a document in a collection of documents, or a corpus.

* A **corpus** (_corpora_ in plural) is a large, structured and organized collection of text documents that normally focuses on a specific matter; there are monolingual, or single-language corpora, and multilingual or multiple-language corpora.

* **TF–IDF** is a weighting factor intended to measure how important a word is to a document in a corpus.

* **TF** indicates that if a word appears multiple times in a document, it can be concluded that it's relevant and more meaningful than other words in the same text.

* **IDF** comes to action when you're analyzing several documents. If a word also appears many times among a collection of documents, maybe it's just a frequent word and not a relevant one.

* A high weight in TF–IDF is reached by terms with high TF and a low document frequency of the term in the corpus; normally these are more interesting terms to analyze.

* A low weight in TF–IDF is reached by terms with low TF and a high document frequency of the term in the corpus; normally these are quite common terms across the corpus that could be less interesting to analyze.

* The **bag-of-words model** is a technique in NLP to represent the important words or tokens in a document without worrying about sentence structure. A bag-of-words model can then be used to compare documents based on the number of important words that they share.

After finishing the lecture slides, switch to the code demo and show how TF–IDF can be calculated with Python using the `sklearn` library; open the [Jupyter starter file](Activities/03-Ins_Terms_Relevance/Unsolved/03_Ins_Terms_Relevance.ipynb) and highlight the following points:

* `nltk` and `nltk.corpus` are used to retrieve the [Reuters Corpus](https://www.nltk.org/book/ch02.html#reuters-corpus).

* From `sklearn` the [`CountVectorizer` class](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) will be used to implement the bag-of-words model, and the [`TfidfVectorizer` class](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) will be used to calculate the TF–IDF.

Continue the explanation by live coding the solution and highlight the following:

* The Reuters Corpus should have been downloaded for convenience.

  ```python
  nltk.download('reuters')
  ```

* The `reuters.fileids()` method retrieves a list with all a document's unique identifiers in the corpus.

* After selecting a single document from the Reuters Corpus, an instance of the `CountVectorizer()` class is created. The `stop_words='english'` parameter will ignore all English-language stopwords when vectorizing the text.

  ```python
  vectorizer = CountVectorizer(stop_words='english')
  ```

* The [`fit_transform()`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.fit_transform) method retrieves a matrix of the terms counts. In this example, a single document is passed as parameter, but a list of documents can be passed instead.

  ```python
  X = vectorizer.fit_transform([doc_text])
  ```

* The `get_feature_names()` method is used to retrieve the list of unique words found.

  ```python
  words = vectorizer.get_feature_names()
  ```

When the `X` matrix is printed, you will notice that it contains raw data that shows the counting of each term represented by a tuple `(n, t)  c`; `t` is the term's numeric identifier, `n` refers to the _nth_ document where the term `t` was found, and `c` is the term's counting on the document `n`. Since we have only one document in this example, the first term is always `0`.
  ![Raw term-document matrix data](Images/raw_bag_of_words.png)

* A more human-readable version of the bag of words is created with the following DataFrame.
  ![term-document matrix as a DataFrame](Images/df_bag_of_words.png)

To calculate the TF–IDF, a set of 1,000 documents from the Reuters Corpus is used as follows:

* A list of 1,000 documents is created by taking the first 1,000 document IDs from the Reuters Corpus.

  ```python
  all_docs_id = reuters.fileids()
  corpus_id = all_docs_id[0:1000]
  corpus = [reuters.raw(doc) for doc in corpus_id]
  ```

* A `TfidfVectorizer()` instance is created by passing the stopwords in English as parameter.

  ```python
  vectorizer = TfidfVectorizer(stop_words='english')
  ```

* The `fit_transform()` method is called passing the 1,000 documents collection as parameter; a matrix with the TF–IDF value for each term on every single document is retrieved.

  ```python
  X_corpus = vectorizer.fit_transform(corpus)
  ```

* The shape of the matrix gives some interesting information. There is a row per document and a column for each term found in the corpus.
  ![TF-IDF matrix shape rationale](Images/tf_idf_matrix.png)

* Finally, a DataFrame is created for a human-readable TF–IDF matrix. The mean value of the TF–IDF is used to create the DataFrame.
  ![TF-IDF DataFrame](Images/tf_idf_df.png)

Conclude the activity by presenting the highest and lowest ten TF–IDF scores. Explain that highest values normally represent less common and more interesting terms for analysis; they have a high term frequency in some documents and a low document frequency in the collection of documents.

If there is time, ask the class what they think about the numbers identified as terms (tokens) by the algorithm. In fact, the importance of these terms resides in the context of the documents; for example a year or an amount could be relevant if you are talking about a historical fact.

---

### 4. Student Do: Bossy Words (20 min)

On this activity, students will use the knowledge from previous lessons to create a word cloud based on TF–IDF weights. The main objective of this activity is to let students see the differences between term relevance and term occurrence in word clouds.

**Instructions:**

* [README.md](Activities/04-Stu_Bossy_Words/README.md)

**Files:**

* [bossy_words.ipynb](Activities/04-Stu_Bossy_Words/Unsolved/bossy_words.ipynb)

---

### 5. Instructor Do: Review Bossy Words (10 min)

Open the [solution](Activities/04-Stu_Bossy_Words/Solved/bossy_words.ipynb) and review the code by highlighting the following:

* The `reuters.categories()` method retrieves all the categories for a given document as is explained in the [Reuters Corpus documentation](https://www.nltk.org/book/ch02.html#reuters-corpus).

  ```python
  >>> reuters.categories('training/9865')
  ['barley', 'corn', 'grain', 'wheat']
  ```

* A comprehension list is used in combination with the `reuters.categories()` method to retrieve the news articles that are under the `money-fx` and `money-supply` categories.

  ```python
  categories = ["money-fx", "money-supply"]
  all_docs_id = reuters.fileids()
  money_news_ids = [
      doc
      for doc in all_docs_id
      if categories[0] in reuters.categories(doc)
      or categories[1] in reuters.categories(doc)
  ]
  ```

* The working corpus is created using a comprehension list that retrieves the full text of all the articles under the categories of interest. Note that the text is switched to lowercase.

  ```python
  money_news = [reuters.raw(doc).lower() for doc in money_news_ids]
  ```

* When the DataFrame is created, the `sum()` method is used to calculate a measure similar to the word frequency in order to have a parameter to order the terms for creating the word cloud.

  ```python
  money_news_df = pd.DataFrame(
    list(zip(vectorizer.get_feature_names(), np.ravel(X.sum(axis=0)))),
    columns=["Word", "Frequency"],
  )
  ```

* In the challenge section, the most tricky part could be to code the search by any of the terms passed as a parameter. The clue is to use the [`any()` function](https://stackoverflow.com/a/16505590/4325668) in the condition of the `found_terms` comprehension list, as explained on [this article](https://stackoverflow.com/a/25102099/4325668).
  ```python
  def retrieve_docs(terms):
    result_docs = []
    for doc_id in money_news_ids:
        found_terms = [
            word
            for word in reuters.words(doc_id)
            if any(term in word.lower() for term in terms)
        ]
        if len(found_terms) > 0:
            result_docs.append(doc_id)
    return result_docs
  ```

Ask if there are any questions before moving on.

---

### 6. Instructor Do: Getting Data for Sentiment Analysis (15 min)

In this activity, students will learn how to retrieve news articles from the [News API](https://newsapi.org/) and its [Python library](https://newsapi.org/docs/client-libraries/python).

**Files:**

* [sentiment_analysis_data.ipynb](Activities/06-Ins_Sentiment_Analysis_Data/Solved/sentiment_analysis_data.ipynb)
* [keys.sh](Activities/06-Ins_Sentiment_Analysis_Data/Solved/keys.sh)

Explain to students that there are several ways to retrieve data for sentiment analysis, such as web scrapping, manual corpus creation from document digitization, document transformations (e.g., from PDF, word processors, or spreadsheets to raw text) and using APIs. Among these data-retrieval mechanisms APIs is one of the most used, so in this activity students will learn how to retrieve news articles using the [News API](https://newsapi.org/) and its [Python library](https://newsapi.org/docs/client-libraries/python).

Open the [News API](https://newsapi.org/) website and explain that it's an easy-to-use API that returns JSON metadata for headlines and articles that are live all over the web right now, so the results retrieved at this moment could be different from the results retrieved in 20 minutes.

Slack out the News API web address to students (https://newsapi.org/) and ask them to create an account by clicking on the "Get API Key" button on the upper right corner.

![News API homepage](Images/news_api_homepage.png)

Guide students on the account process creation by following these steps:

* On the registration form, the "I am an individual" option should be selected to create a free developer account. It's also important to select the last two check boxes since this is a free service.
  ![News API registration form](Images/news_api_registration_form.png)

* Once the account is created, the API key is shown on [the Account page](https://newsapi.org/account).

  ![News API account page](Images/news_api_account_details.png)

Ask students to create an environment variable called `news_api` by adding their API key to the `keys.sh` script and executing it on the terminal window as they did on the APIs unit.

You are almost ready to code! Before starting the demo, ask students to install the [News API Python library](https://newsapi.org/docs/client-libraries/python) on their virtual environment by executing the following command.

  ```bash
  pip install newsapi-python
  ```

Open [the unsolved Jupyter notebook](Activities/06-Ins_Sentiment_Analysis_Data/Unsolved/sentiment_analysis_data.ipynb) and live code the demo by highlighting the following:

* The `NewsApiClient` class should be imported to interact with the News API service.

  ```python
  from newsapi import NewsApiClient
  ```

* To create a `NewsApiClient` object, the API key should be passed as parameter.

  ```python
  newsapi = NewsApiClient(api_key=api_key)
  ```

Switch to [the News API documentation](https://newsapi.org/docs/endpoints) and explain that there are three different endpoints. Encourage students to review the API documentation to learn more about all the different request parameters they have available:

* Top Headlines: Returns breaking news headlines; the most relevant request parameters are `q` for the search terms, `language` and `country`.
* Everything: Retrieves news and articles from over 30,000 different sources; the most relevant request parameters are `q` for the search terms, `language` and `sort_by`.
* Sources: Returns information about the most important article sources that this service indexes.

Switch back to the Jupyter notebook and mention to students that you will focus on using the Top Headlines and Everything endpoints, slack out the [News API Python Client Library reference page](https://newsapi.org/docs/client-libraries/python) and encourage them to learn more about this library and its options.

Start the live-coding demo by highlighting the following:

* The `get_top_headlines()` method fetches top news articles about the keyword defined on the `q` parameter. This example gets top headlines about oil (`q="oil"`) in English (`language="en"`) from the United States (`country="us"`).

  ```python
  oil_headlines = newsapi.get_top_headlines(
    q="oil",
    language="en",
    country="us"
  )
  ```

* The Python client library transforms the API response to a Python dictionary, so elements of the JSON schema can be accessed by a key.

  ![News API sample reponse](Images/news_api_sample_response.png)

* All the articles can be retrieved from the `totalResults` key and the content of a single article from the `articles` key.

  ![Accessing the News API dictionary](Images/news_api_top_headlines.png)

Show students how they can create a DataFrame using the response Python dictionary for further analysis, data manipulation, or storing the data.

  ![Creating a DataFrame from the response python dictionary](Images/news_api_df.png)

Live code the `newsapi.get_everything()` demo by highlighting that it's also possible to send more than one keyword as search term, as with this example to fetch news about Facebook Libra using `q="facebook libra"` as parameter:

* Separating two keywords by a blank space is equivalent to use `q="facebook AND libra"`.

  ```python
  libra_headlines = newsapi.get_everything(
      q="facebook libra",
      language="en",
      sort_by="relevancy"
  )
  ```

Answer any question that arise and move to the next activity.

---

### 7. Student Do: The Voice of the Crisis (15 min)

In this activity, students will use the News API to retrieve news articles in English and French about the financial crisis of 2008. At the end of the activity, students will create a CSV file that will be used for coming activities.

**Instructions:**

* [README.md](Activities/07-Stu_Crisis_Voice/README.md)

**Files:**

* [voice_crisis.ipynb](Activities/07-Stu_Crisis_Voice/Unsolved/voice_crisis.ipynb)

---

### 8. Instructor Do: Review The Voice of the Crisis (5 min)

Open the [solution](Activities/07-Stu_Crisis_Voice/Solved/voice_crisis.ipynb) and walk through the code, highlight the following:

* As can be read on [the News API documentation for the `Everything` endpoint,](https://newsapi.org/docs/endpoints/everything) it's possible to use logical operators to include or exclude keywords.
  ![Documentation for the q parameter of the News API](Images/new_api_q_param.png)

* All the articles containing the three keywords are retrieved using the `AND` operator, either for English or French news. The queries are sensitive to orthographic signs, so it's important to use the grave accent over the first `è` in `financière`.

  ```python
  # Fetch news about the financial crisis on 2008 in English
  crisis_news_en = newsapi.get_everything(
      q="financial AND crisis AND 2008",
      language="en"
  )

  # Fetch news about the financial crisis on 2008 in French
  crisis_news_fr = newsapi.get_everything(
      q="crise AND financière AND 2008",
      language="fr"
  )
  ```

Review the code for the `create_df()` function highlighting the following:

* A list of dictionaries is used to create the DataFrame structure, so an empty list `articles` is created before starting the iteration across all the news articles.

* A `for-loop` is used to iterate across the `news` list to fetch every article's data and to keep only the fields of interest.

* A new element is appended to the list on every iteration with an additional key for the language.

* A `try-except` block is used to bypass any list-attribute error.

![Important points on the create_df() function](Images/create_df_function.png)

* Once the `create_df()` function is coded, one DataFrame per language is created and both DataFrames are concatenated with the `pd.concat()` function.

```python
# Create a DataFrame with the news in English
crisis_en_df = create_df(crisis_news_en["articles"], "en")

# Create a DataFrame with the news in French
crisis_fr_df = create_df(crisis_news_fr["articles"], "fr")

# Concatenate both DataFrames
crisis_df = pd.concat([crisis_en_df, crisis_fr_df])
```

Get the `head()` an `tail()` of the DataFrame to show the news articles in both languages.

![Sample news in English and French](Images/crisis_news_df.png)

Save the DataFrame as a CSV file for further use in the next activities. Warn students that is important to use the `encoding='utf-8-sig'` parameter when saving the file to preserve special characters, especially in French, in the CSV file.

```python
file_path = Path("Data/crisis_news_en_fr.csv")
crisis_df.to_csv(file_path, index=False, encoding='utf-8-sig')
```

Answer any additional question before moving to the next activity.

---

### 9. Instructor Do: Intro to VADER Sentiment (15 min)

In this activity, students will understand how VADER sentiment works and how to interpret sentiment polarity; also students will learn how to score sentiment using the VADER module of NLTK.

**Files:**

* [vader_sentiment.ipynb](Activities/09-Ins_Vader_Sentiment/Solved/vader_sentiment.ipynb)

Open the lesson slides, move to the Intro to VADER Sentiment section and highlight the following:

* VADER (Valence Aware Dictionary and Sentiment Reasoner) is a tool used to score the sentiment  of human speech as positive, neutral, or negative based on a set of rules and a [lexicon](https://dictionary.cambridge.org/dictionary/english/lexicon) (a list of words).

* VADER calculates the polarity of a sentiment using its built-in rules and a predefined lexicon that was manually tagged as positive or negative according to semantic orientation.

* VADER generates four scores for each analyzed text: positive (`pos`), neutral (`neu`), negative (`neg`) and `compound`.

* The `pos`, `neu` and `neg` scores assess the sentiment from 0 to 1.

* The `compound` score is the most useful metric if a single measure of sentiment for a given text is needed.

* The `compound` score ranges between `-1` (most extreme negative) and `+1` (most extreme positive); the following rules can be followed to interpret this measure:

  * positive sentiment: `compound` score >= 0.05
  * neutral sentiment: (`compound` score > -0.05) and (`compound` score 0.05)
  * negative sentiment: `compound` score <= -0.05

Open the Jupyter notebook, live code the solution and highlight the following:

* The News API is used to fetch news about Facebook Libra and analyze sentiment using the [`NLTK` VADER sentiment module](https://www.nltk.org/api/nltk.sentiment.html#module-nltk.sentiment.vader).

```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer
```

* Prior to use, `nltk vader` the `vader_lexicon` should be downloaded.

```python
nltk.download('vader_lexicon')
```

* Once the `vader_lexicon` is available, the `SentimentIntensityAnalyzer()` can be initialized. [This class](https://www.nltk.org/_modules/nltk/sentiment/vader.html#SentimentIntensityAnalyzer) gets a sentiment intensity score to a sentence based on VADER.

```python
analyzer = SentimentIntensityAnalyzer()
```

* The `page_size` parameter is used on the `newsapi.get_everything()` method to define a page size of 100 articles.

```python
libra_headlines = newsapi.get_everything(
    q="facebook AND libra",
    language="en",
    page_size=100,
    sort_by="relevancy"
)
```

* The sentiment scores are retrieved using a `for-loop` that creates a DataFrame; every row contains the text of each news article and its four VADER sentiment scores.

  ![DataFrame creation including VADER sentiment scores](Images/vader_sentiment_df_creation.png)

* The descriptive stats from the DataFrame are useful to understand the average sentiment of the news, as well as to identify the news with the most negative or positive sentiment.

  ![Sample VADER sentiment descriptive stats](Images/vader_df_stats.png)

Answer any questions from class before moving on.

---

### 10. BREAK (15 min)

---

### 11. Student Do: The Feelings of the Crisis (20 min)

On this activity, students will use VADER to score the sentiment of news title and text to verify whether they have the same sentiment. This activity includes a facilitated discussion in the last four to five minutes to talk about students' findings.

**Instructions:**

* [README.md](Activities/11-Stu_Crisis_Feelings/README.MD)

**Files:**

* [crisis_feelings.ipynb](Activities/11-Stu_Crisis_Feelings/Unsolved/crisis_feelings.ipynb)

---

### 12. Instructor Do: Review The Feelings of the Crisis (5 min)

**Files:**

* [crisis_feelings.ipynb](Activities/11-Stu_Crisis_Feelings/Solved/crisis_feelings.ipynb)

Open the solution and walk through the code, highlighting the following:

* It's important to use the `encoding='utf-8-sig'` to load the CSV file when creating the DataFrame, especially to get all the special characters from the news articles in French.

  ```python
  file_path = Path("Data/crisis_news_en_fr.csv")
  news_df = pd.read_csv(file_path, encoding='utf-8-sig')
  ```

* The VADER sentiment module is only trained to score sentiment in English, so a new DataFrame with only news in English is created. Students will learn how to score sentiment in multiple languages later.

  ```python
  news_en_df = news_df[news_df["language"] == "en"]
  ```

* Two empty Python dictionaries are used to create the DataFrame's structure that will store the sentiment scoring results for the title and the text from the news articles.

  ```python
  title_sent = {
      "title_compound": [],
      "title_pos": [],
      "title_neu": [],
      "title_neg": [],
      "title_sent": []
  }
  text_sent = {
      "text_compound": [],
      "text_pos": [],
      "text_neu": [],
      "text_neg": [],
      "text_sent": []
  }
  ```

* The `compound` score will be used to measure the sentiment, so a function called `get_sentiment()` is created to translate the `compound` score to a normalized value as follows: `1` for positive sentiment, `-1` for negative sentiment, and `0` for neutral sentiment.

  ```python
  def get_sentiment(score):
    """
    Calculates the sentiment based on the compound score.
    """
    result = 0  # Neutral by default
    if score >= 0.05:  # Positive
        result = 1
    elif score <= -0.05:  # Negative
        result = -1

    return result
  ```

* The VADER sentiment score for each news article's title and text is calculated within a `for-loop`; this loop iterates across the `news_en_df` DataFrame using the `iterrows()` method to create the final result's DataFrame structure.

  ![Sentiment scores calculation](Images/crisis_feelings_title_text_code.png)

* Two DataFrames are created with the resulting VADER sentiment scores for titles and the text. These DataFrames are added as new columns to the `news_en_df` DataFrame using the `join()` function.

  ```python
  # Titles' sentiments DataFrame
  title_sentiment_df = pd.DataFrame(title_sent)

  # Texts' sentiments DataFrame
  text_sentiment_df = pd.DataFrame(text_sent)

  # Sentiment scoring results added to the news_en_df DataFrame
  news_en_df = news_en_df.join(title_sentiment_df).join(text_sentiment_df)
  ```

* A bar chart is created using the `plot()` method from the DataFrame to review whether the title and the text of a news article have the same sentiment or not. The chart's grid is added to identify how the bars for each news articles behave.

  ```python
  news_en_df.plot(y=["title_sent", "text_sent"],
                  kind='bar',
                  title="News Title and Text Sentiment Comparison",
                  figsize = (10, 8),
                  grid=True
  )
  ```

  ![Sample sentiments bar chart](Images/crisis_feelings_bar_chart.png)

Answer any additional question before moving to the next activity.

---

### 13. Instructor Do: Tone Analysis (20 min)

In this activity, students will be introduced to tone analysis and how they can score the tone of human speech using the **IBM Watson Tone Analyzer service** and its Python library.

**Files:**

* [tone_analysis.ipynb](Activities/13-Ins_Tone_Analysis/Solved/tone_analysis.ipynb)

* [keys.sh](Activities/13-Ins_Tone_Analysis/Solved/keys.sh)

Start by opening the lesson slides, go to the Tone Analysis section and highlight the following:

* Tone analysis offers new possibilities for sentiment analysis since it goes beyond the simple classic classification as positive, negative or neutral and looks to understand human emotions.

* Tone analysis is a complex and costly task since it requires training algorithms with thousands of documents that need to be previously tagged to understand the emotion behind the words.

* IBM Watson Tone Analyzer is a cloud service to analyze tone on text communications. This service is  available for English and French languages.

* IBM Watson Tone Analyzer can be used via its Python API.

After the brief definition of tone analysis and the intro to IBM Watson Tone Analyzer, slack out [the URL for this service](https://cloud.ibm.com/catalog/services/tone-analyzer) and guide students on creating their IBM Cloud account and setting up their Tone Analyzer instance. Ask TAs to assist students on creating their personal IBM Cloud account and follow the lesson slides as a guided tour by highlighting the following:

* Students will use the Lite plan of Tone Analyzer, it allows 2,500 API call per month for free and no credit card is required to use it.

* Student only need to fill out their personal account information on the registration form.

  ![IBM Cloud registration form](Images/ibm_cloud_registration_form.png)

* Students will receive an email and have to click on the "Confirm account" button to start using the Tone Analyzer service.

  ![IBM Cloud confirmation e-mail sample](Images/ibm_cloud_registration_form.png)

* After the new IBM Cloud account is confirmed, students will see their dashboard. The "Create resource" button should be clicked to continue.

  ![IBM Cloud dashboard](Images/ibm_cloud_dashboard.png)

Once students have access to their IBM Cloud dashboard, they need to create an instance of the Tone Analyzer Service. At the Catalog, students should type `label:lite tone analyzer` in the search box to find the service. Once the service appears in the results, ask students to click on the "Tone Analyzer Service" to configure the instance.

  ![IBM Cloud catalog](Images/ibm_cloud_catalog.png)

* To create the Tone Analyzer instance, just the "Service name" should be provided on the Tone Analyzer configuration page. After the "Create" button is clicked, the instance is ready to be used.

  ![Tone Analyzer configuration page](Images/tone_analyzer_create_instance.png)

Now that the Tone Analyzer instance is ready to use, ask students get their API keys and the instance URL by clicking on the "Show credentials" link.

  ![Tone Analyzer instance sample](Images/show_tone_analyzer_credentials.png)

* Students will find their credentials under the section titled Step 1: Using the general-purpose endpoint via the POST request method.

* Students will see the API key and the instance URL as it's shown below. The URL can differ from the image but it ends with `/api`.

  ![Tone Analyser credentials](Images/get_tone_analyzer_key.png)

Ask students to create two environment variables, one for the API key and the other for the URL. Open the [unsolved Jupyter notebook](Activities/13-Ins_Tone_Analysis/Solved/tone_analysis.ipynb) and switch to the code demo, highlighting the following:

* The IBM Watson Python library need to be installed using `pip` as follows. This demo runs using version 3.

  ```bash
  pip install --upgrade "ibm-watson>=3.0.3"
  ```

* The Tone Analyzer service is imported from the `ibm_watson` library as follows:

  ```python
  from ibm_watson import ToneAnalyzerV3
  ```

* The Tone Analyzer response is given in JSON format, so the [`json_normalize` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.json.json_normalize.html) is imported from Pandas to transform the JSON response to a DataFrame.

  ```python
  from pandas.io.json import json_normalize
  ```

* The Tone Analyzer service should be initialized passing as parameters the version that is going to be used, the API key and the URL.

  ```python
  tone_analyzer = ToneAnalyzerV3(version="2017-09-21", iam_apikey=tone_api, url=tone_url)
  ```

* The IBM Watson Tone Analyzer has two main methods:

  * `tone()`: The general tone analysis, aimed to score tone on short text (such as reviews, emails, or social media) or even larger texts (such as articles or blog post)

  * `tone_chat()`: The customer engagement tone analysis, designed to monitor customer service and support conversations based on utterances between an agent and a customer

The `tone()` method is presented first. Explain students that it only needs to receive a text to score, however, additional parameters could be used to define the `content_language` (only `en` for English or `fr` for `french` are available in the current version) or the `accept_language`, that is the language to be used for the name of tones.

```python
# Define text to analyze
text = """
Team, I know that times are tough!
Product sales have been disappointing for the past three quarters.
We have a competitive product, but we need to do a better job of selling it!
"""

# Analyze the text's tone with the 'tone()' method.
tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json',
    content_language='en',
    accept_language='en'
).get_result()

# Display tone analysis results
print(json.dumps(tone_analysis, indent=2))
```

* On the `JSON` response, the tone is given for the entire document on the `document_tone` element as well as for each sentence of the document on the `sentences_tone` element.

  ```json
  {
    "document_tone": {
      "tones": [
        {
          "score": 0.6165,
          "tone_id": "sadness",
          "tone_name": "Sadness"
        },
        {
          "score": 0.829888,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    },
    "sentences_tone": [
      {
        "sentence_id": 0,
        "text": "Team, I know that times are tough!",
        "tones": [
          {
            "score": 0.801827,
            "tone_id": "analytical",
            "tone_name": "Analytical"
          }
        ]
      },
      {
        "sentence_id": 1,
        "text": "Product sales have been disappointing for the past three quarters.",
        "tones": [
          {
            "score": 0.771241,
            "tone_id": "sadness",
            "tone_name": "Sadness"
          },
          {
            "score": 0.687768,
            "tone_id": "analytical",
            "tone_name": "Analytical"
          }
        ]
      },
      {
        "sentence_id": 2,
        "text": "We have a competitive product, but we need to do a better job of selling it!",
        "tones": [
          {
            "score": 0.506763,
            "tone_id": "analytical",
            "tone_name": "Analytical"
          }
        ]
      }
    ]
  }
  ```

* The `JSON` response is transformed into a Pandas DataFrame using the `json_normalize()` function.

  ![Sample document tone as DataFrame](Images/document_tone_df.png)

Next, the `tone_chat()` method is presented. Explain to students that this method is intended to analyze tone from customer engagement conversations, between an agent and a customer, where all the utterances are passed as parameter to score the tone of each one.

```python
# Define conversational utterances
utterances = [
    {
        "text": "Hello, I'm having a problem with your product.",
        "user": "customer"
    },
    {
        "text": "OK, let me know what's going on, please.",
        "user": "agent"
    },
    {
        "text": "Well, nothing is working :(",
        "user": "customer"
    },
    {
        "text": "Sorry to hear that.",
        "user": "agent"
    }
]

# Analyze utterances using the 'tone_chat' methos
utterance_analysis = tone_analyzer.tone_chat(
    utterances = utterances,
    content_language='en',
    accept_language='en'
).get_result()
print(json.dumps(utterance_analysis, indent=2))
```

* On the `JSON` response, all the tone scores for each utterance are under the `utterances_tone` element.

  ```json
  {
    "utterances_tone": [
      {
        "utterance_id": 0,
        "utterance_text": "Hello, I'm having a problem with your product.",
        "tones": [
          {
            "score": 0.686361,
            "tone_id": "polite",
            "tone_name": "Polite"
          }
        ]
      },
      {
        "utterance_id": 1,
        "utterance_text": "OK, let me know what's going on, please.",
        "tones": [
          {
            "score": 0.92724,
            "tone_id": "polite",
            "tone_name": "Polite"
          }
        ]
      },
      {
        "utterance_id": 2,
        "utterance_text": "Well, nothing is working :(",
        "tones": [
          {
            "score": 0.997795,
            "tone_id": "sad",
            "tone_name": "Sad"
          }
        ]
      },
      {
        "utterance_id": 3,
        "utterance_text": "Sorry to hear that.",
        "tones": [
          {
            "score": 0.730982,
            "tone_id": "polite",
            "tone_name": "Polite"
          },
          {
            "score": 0.672499,
            "tone_id": "sympathetic",
            "tone_name": "Sympathetic"
          }
        ]
      }
    ]
  }
  ```

* The `JSON` response is converted to a Pandas DataFrame using the `json_normalize` method. The `meta` argument is used to include the `utterance_id` and `utterance_text` on each row.

  ![Sample utterances tone](Images/char_tone_df.png)

Inform students that they will use this cloud service in the next class. Slack out the Tone Analyzer docs for the [`tone()`](https://cloud.ibm.com/docs/services/tone-analyzer?topic=tone-analyzer-utgpe) and [`tone_chat()`](https://cloud.ibm.com/docs/services/tone-analyzer?topic=tone-analyzer-utco) methods, and close the activity by answering any remaining question.

---

### 14. Instructor Do: Recap (10 min)

Take a moment to congratulate the students on wrapping up a really fun and intense week of natural language processing. Remind them that NLP and, in particular, sentiment analysis have a lot of interesting applications in FinTech, such as market prediction or product benchmarking.

Recap by asking students to summarize with one word or a three-word phrase what they learned today. Ask for volunteers, and then eventually go round-robin if necessary.

**Answer:** Finance has emotions

**Answer:** Complexity

**Answer:** Human speech understanding

**Answer:** Algorithms measure emotions

**Answer:** Sentiments visualization

Emphasize to students how they used some of the skills they already master to work on today's activities; sentiment analysis is a multidisciplinary area that requires not only algorithms to score sentiments of human speech, but also data cleaning and meaningful data visualizations to present results and share insights.

Explain that NLP and sentiment analysis is still a cutting-edge research area. In particular, new deep-learning techniques such as recurrent neural networks have transformed NLP and pushed it toward what we only imaged before as science fiction. Encourage students to keep learning and trying new libraries and technologies as this specialization of machine learning continues to expand.

### END CLASS

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
