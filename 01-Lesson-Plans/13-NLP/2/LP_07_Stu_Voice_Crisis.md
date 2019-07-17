### 7. Student Do: The Voice of the Crisis (10 mins)

On this activity students will use the News API to retrieve news articles on English and French about the financial crisis of 2008. At the end of the activity students will create a CSV file that will be used on the forthcoming student's activities.

**Instructions:**

* [README.md](Activities/07-Stu_Crisis_Voice/README.md)

**Files:**

* [voice_crisis.ipynb](Activities/07-Stu_Crisis_Voice/Unsolved/voice_crisis.ipynb)

---

### 8. Instructor Do: Review The Voice of the Crisis (5 mins)

Open the [solution](Activities/07-Stu_Crisis_Voice/Solved/voice_crisis.ipynb) and walk through the code highlight the following:

* As can be read on [the News Api documentation for the `Everything` endpoint](https://newsapi.org/docs/endpoints/everything) it's possible to use logical operators to include or exclude keywords.
  ![Documentation for the q parameter of the News API](Images/new_api_q_param.png)

* All the articles containing the three keywords are retrieved using the `AND` operator, either for English and French news. The queries are sensitive to orthographic signs, so it's important to use de accent over the first `è` on `financière`.

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

* A `try - except` block is used to bypass any list attribute error.

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

Save the DataFrame as a CSV file for further usage on the next activities, warn students that is important to use the `encoding='utf-8-sig'` parameter when saving the file to preserve special characters, especially in French, on the CSV file.

```python
file_path = Path("Data/crisis_news_en_fr.csv")
crisis_df.to_csv(file_path, index=False, encoding='utf-8-sig')
```

Answer any additional question before moving to the next activity.
