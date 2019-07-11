### 9. Instructor Do: Intro to VADER Sentiment (15 mins)

**Files:**

* [Lesson Slides - Intro to VADER Sentiment Section](#)

* [vader_sentiment.ipynb](Activities/09-Ins_Vader_Sentiment/Solved/vader_sentiment.ipynb)

Open the lesson slides, move to the _Intro to VADER Sentiment_ section and highlight the following:

* VADER (**V**alence **A**ware **D**ictionary and s**E**ntiment **R**easoner) is a tool used to calculate the sentiment of human speech based on a set of rules and a [lexicon](https://dictionary.cambridge.org/dictionary/english/lexicon) (a kind of list of words).

* VADER calculates the polarity of a sentiment using its built-in rules and the predefined lexicon that was manually tagged as positive or negative according to their semantic orientation. This work was conducted by C.J. Hutto and Eric Gilbert from the Georgia Institute of Technology. [Here](http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf) you can read the research paper where this work is presented.

* Explain students how VADER measures the sentiment using the `pos`, `neu`, `neg` and `compound` scores.

* The `pos`, `neu` and `neg` scores assess the sentiment from 0 to 1,  the sum of these three scores barely adds one.

* The `compound` score is the most useful metric if a single measure of sentiment for a given sentence is needed. it can be seen as a normalized, weighted composite score.

* The `compound` score ranges between -1 (most extreme negative) and +1 (most extreme positive); the following rule can be followed to interpret this measure:

  > positive sentiment: `compound` score >= 0.05
  >
  > neutral sentiment: (`compound` score > -0.05) and (`compound` score 0.05)
  >
  > negative sentiment: `compound` score <= -0.05

Open the Jupyter notebook, live code the solution and highlight the following:

* On this demo we will use the News API to fetch news about Facebook Libra and analyze sentiment using the [`NLTK` VADER sentiment module](https://www.nltk.org/api/nltk.sentiment.html#module-nltk.sentiment.vader).

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

* For this demo the `page_size` parameter is used on the `newsapi.get_everything()` method to define a page size of 100 articles.

```python
libra_headlines = newsapi.get_everything(
    q="facebook AND libra",
    language="en",
    page_size=100,
    sort_by="relevancy"
)
```

* The sentiment scores are retrieved on the for-loop that creates the DataFrame, in this way, we are taking advantage of the DataFrame creation to add to each row the VADER sentiment scores.
  ![DataFrame creation including VADER sentiment scores](Images/vader_sentiment_df_creation.png)
