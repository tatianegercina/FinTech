### 11. Students Do: The Feelings of the Crisis (15 mins)

On this activity, students will use VADER to score the sentiment of news' title and text to verify if they have the same sentiment. This activity includes a facilitated discussion along the last four to five minutes to talk about students findings.

**Instructions:**

* [README.md](Activities/11-Stu_Crisis_Feelings/README.md)

**Files:**

* [crisis_feelings.ipynb](Activities/11-Stu_Crisis_Feelings/Unsolved/crisis_feelings.ipynb)

---

### 12. Instructor Do: Review The Feelings of the Crisis (5 min)

**Files:**

* [crisis_feelings.ipynb](Activities/11-Stu_Crisis_Feelings/Solved/crisis_feelings.ipynb)

Open the solution and walk through the code highlighting the following:

* It's important to use the `encoding='utf-8-sig'` to load the CSV file when creating the DataFrame, especially to get all the special characters from the news articles in French.

  ```python
  file_path = Path("Data/crisis_news_en_fr.csv")
  news_df = pd.read_csv(file_path, encoding='utf-8-sig')
  ```

* The VADER sentiment module is only trained to score sentiment on English language, so a new DataFrame only with news in English is created. Students will learn how to score sentiment in multiple languages later.

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

* The VADER sentiment score for each news article's title and text is calculated within a `for-loop`, this loop iterates across the `news_en_df` DataFrame using the `iterrows()` method to create the final results DataFrame structure.

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

* A bar chart is created using the `plot()` method from the DataFrame to review when the title and the text of a news article have the same sentiment or not. The chart's grid is intentionally added to identify how the bars for each news articles behave.

  ```python
  news_en_df.plot(y=["title_sent", "text_sent"],
                  kind='bar',
                  title="News Title and Text Sentiment Comparisson",
                  figsize = (10, 8),
                  grid=True
  )
  ```

  ![Sample sentiments bar chart](Images/crisis_feelings_bar_chart.png)

Answer any additional question before moving to the next activity.
