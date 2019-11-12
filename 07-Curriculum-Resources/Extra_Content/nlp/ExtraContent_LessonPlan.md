### 1. Student Do: Crisis Analysis Dashboard (40 min)

In this mini-project activity, students will use their new sentiment analysis skills in combination with some of the skills they have already mastered, such as Pandas, PyViz, Plotly Express, and PyViz Panel, to create a data visualization dashboard.

Students will analyze sentiment and tone about the news related to the financial crisis of 2008 that was published in the past month, fetching articles from the News API. By default, the developer account gives access to news articles up to a month old.

Present the solution demo to students before starting the activity and join TAs to assist students with this activity.

* This activity can be done in teams of up to three students.

**Instructions:**

* [README.md](Activities/14-Stu_Sentiment_Dashboard/README.md)

**Files:**

* [sentiment_analysis.ipynb](Activities/14-Stu_Sentiment_Dashboard/Unsolved/sentiment_analysis.ipynb)

* [sentiment_dashboard.ipynb](Activities/14-Stu_Sentiment_Dashboard/Unsolved/sentiment_dashboard.ipynb)

---

### 2. Instructor Do: Review Crisis Analysis Dashboard (10 min)

**Files:**

* [sentiment_analysis.ipynb](Activities/14-Stu_Sentiment_Dashboard/Solved/sentiment_analysis.ipynb)

* [sentiment_dashboard.ipynb](Activities/14-Stu_Sentiment_Dashboard/Solved/sentiment_dashboard.ipynb)

Start by opening the `sentiment_analysis.ipynb` solution; walk through the solution and highlight the following:

* In this activity, students will use their new sentiment analysis skills, in combination with some of the skills they've already mastered, such as Pandas, Pyviz, Plotly Express and PyViz Panel, why the initial imports section is quite large.

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

* It is important to define the `page_size=100` on the News API instance to have a more interesting number of news articles to analyze.

  ```python
  crisis_news_en = newsapi.get_everything(
      q="financial AND crisis AND 2008",
      language="en",
      page_size=100
  )
  ```

* When the news articles' sentiments DataFrame is created, a `try-except` block is used to pass any `AttributeError` that could occur. This is important to have to avoid problems when launching the dashboard web application.

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
* On the Challenge section, take into account that the `for-loop` to create the DataFrame structure containing the news articles and their tone scoring results will take up to five minutes to complete, so a kind of progress bar is created by printing asterisks on each iteration.

  ![DataFrame creation sample with news articles and tone analysis results](Images/tone_analysis_progress_bar.png)

Explain to students that it is important to create the CSV files on this section to reduce the processing time on the dashboard creation by only reading the final results from the files.

Continue the review activity by opening the `sentiment_dashboard.ipynb` Jupyter notebook; walk through the solution and highlight the following:

* As students did on the PyViz unit homework, on this notebook they have to compile all the plots into functions to be used on a PyViz Panel Dashboard.

* Instead of doing all the sentiment and tone scoring, these functions will load the data from the CSV files previously created.

  * The `news_vader.csv` file with all the news articles and the VADER sentiment scores

  * The `tone_data.csv` file with the IBM Watson Tone Analyzer results

  * The `top_words_data.cvs` file with the top 20 words for creating the word cloud based on the bag-of-words method

  * The `top_words_tfidf_data.cvs` file with the top 20 words for creating the word cloud based on TF-IDF

On the Plots Functions section comment to students on the following:

* It is important to include any DataFrame transformation or manipulation code required along with the plotting code.

* Each function should return a Panel pane object that will be used to build the dashboard.

* Any `.show()` methods should be removed from the code.

* The final dashboard could be like the one shown below.

  ![Sample dashboard](Images/sentiment_analysis_dashboard.gif)
