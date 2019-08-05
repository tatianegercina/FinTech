### 9. Instructor Do: Intro to VADER Sentiment (15 mins)

In this activity students will understand how VADER sentiment works and how to interpret sentiment polarity; also students will learn how to score sentiment using the VADER module of NLTK.

**Files:**

* [Lesson Slides - Intro to VADER Sentiment Section](#)

* [vader_sentiment.ipynb](Activities/09-Ins_Vader_Sentiment/Solved/vader_sentiment.ipynb)

Open the lesson slides, move to the _Intro to VADER Sentiment_ section and highlight the following:

* VADER (**V**alence **A**ware **D**ictionary and s**E**ntiment **R**easoner) is a tool used to score the sentiment polarity of human speech as positive, neutral or negative based on a set of rules and a [lexicon](https://dictionary.cambridge.org/dictionary/english/lexicon) (a kind of list of words).

* VADER calculates the polarity of a sentiment using its built-in rules and a predefined lexicon that was manually tagged as positive or negative according to their semantic orientation.

* VADER generates four scores for each analyzed text: positive (`pos`), neutral (`neu`), negative (`neg`) and `compound`.

* The `pos`, `neu` and `neg` scores assess the sentiment from 0 to 1,  the sum of these three scores barely adds one.

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

* Prior to use `nltk vader` the `vader_lexicon` should be downloaded.

```python
nltk.download('vader_lexicon')
```

* Once the `vader_lexicon` is available the `SentimentIntensityAnalyzer()` can be initialized. [This class](https://www.nltk.org/_modules/nltk/sentiment/vader.html#SentimentIntensityAnalyzer) gets a sentiment intensity score to a sentence based on VADER.

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

* The sentiment scores are retrieved using a `for-loop` that creates a DataFrame, every row contains the text of each news article and its four VADER sentiment scores.

  ![DataFrame creation including VADER sentiment scores](Images/vader_sentiment_df_creation.png)

* The descriptive stats from the DataFrame are useful to understand the average sentiment of the news, as well as to identify those news with the most negative or positive sentiment.

  ![Sample VADER sentiment descriptive stats](Images/vader_df_stats.png)

Answer any questions from class before moving on.
