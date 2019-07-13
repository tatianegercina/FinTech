### 11. Student Do: The Feelings of the Crisis (15 mins)

On this activity student will use VADER sentiment to score the sentiment of news title and text to contrast if they have the same sentiment. This activity includes some open discussion on the class about the findings on scoring sentiment and the contrast between the sentiment a news title and its content. Encourage students to share their insights in the last 4 or 5 minutes of the activity.

**Instructions:**

* [README.md](Activities/11-Stu_Crisis_Feelings/README.md)

**Files:**

* [crisis_feelings.ipynb](Activities/11-Stu_Crisis_Feelings/Unsolved/crisis_feelings.ipynb)

---

### 12. Instructor Do: Review The Feelings of the Crisis (5 min)
**Files:**

* [crisis_feelings.ipynb](Activities/11-Stu_Crisis_Feelings/Solved/crisis_feelings.ipynb)

Walk through the solution and highlight the following:

* Remark students that it's important to use the `encoding='utf-8-sig'` to load the CSV file when creating the DataFrame.

```python
file_path = Path("Data/crisis_news_en_es.csv")
news_df = pd.read_csv(file_path, encoding='utf-8-sig')
```

* When reviewing the English news DataFrame creation, comment to students that the VADER sentiment module only works by default with English language, explain that there are three general approaches to use VADER in different languages: (1) to translate all text to English (2) to use a VADER lexicon for each language (this is quite complex to build) and  (3) to use a cloud sentiment scoring service.

* For the DataFrame creation, two Python dictionaries are created to store all the sentiments scores using a key per score.

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

* To calculate the sentiment score for each news article title and text, a for-loop is used to iterate across all the DataFrame using the `iterrows()` method. Next the sentiment is scored for each title and text to later be appended as a new element on their corresponding dictionaries keys.
  ![Sentiment scores calculation](Images/crisis_feelings_title_text_code.png)

* To append the new columns with the sentiment scores, a DataFrame is created for each dictionary and added to the English news articles using the `join()` function.

```python
title_sentiment_df = pd.DataFrame(title_sent)
text_sentiment_df = pd.DataFrame(text_sent)
news_en_df = news_en_df.join(title_sentiment_df).join(text_sentiment_df)
```

* To create the bar chart the `plot()` method from the DataFrame is used. Grid is intentionally added to identify how the bars for each news articles behave. Comment to students that this chart helps to see when the title and the text of a news article have the same sentiment or not.

```python
news_en_df.plot(y=["title_sent", "text_sent"],
                kind='bar',
                title="News Title and Text Sentiment Comparisson",
                figsize = (10, 8),
                grid=True
)
```

Answer any additional question before moving to the next activity.
