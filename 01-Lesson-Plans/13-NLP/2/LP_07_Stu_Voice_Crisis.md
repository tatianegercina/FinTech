### 7. Student Do: The Voice of the Crisis (10 mins)

On this activity students will use the News API to retrieve news articles on English and Spanish about the financial crisis of 2008. At the end of the activity students will create a CSV file that will be used on the forthcoming student's activities.

**Instructions:**

* [README.md](Activities/07-Stu_Crisis_Voice/README.md)

**Files:**

* [voice_crisis.ipynb](Activities/07-Stu_Crisis_Voice/Unsolved/voice_crisis.ipynb)

---

### 8. Instructor Do: Review The Voice of the Crisis (5 mins)

**Files:**

* [voice_crisis.ipynb](Activities/07-Stu_Crisis_Voice/Solved/voice_crisis.ipynb)

* [crisis_news_en_es.csv](Activities/07-Stu_Crisis_Voice/Solved/Data/crisis_news_en_es.csv)

Walk through the solution and highlight the following:

* As can be read on [the News Api documentation for the `Everything` endpoint](https://newsapi.org/docs/endpoints/everything) it's possible to use logical operator to include or exclude keywords.
  ![Documentation for the q parameter of the News API](Images/new_api_q_param.png)

* In oder to fetch all the articles containing the three keywords the `AND` operator should be used, either for English and Spanish news.

```python
# Fetch news about the financial crisis on 2008 in English
crisis_news_en = newsapi.get_everything(
    q="financial AND crisis AND 2008",
    language="en"
)

# Fetch news about the financial crisis on 2008 in Spanish
crisis_news_es = newsapi.get_everything(
    q="crisis AND financiera AND 2008",
    language="es"
)
```

On the code of the `create_df()` function remark the following:

* In order to create the DataFrame a list of dictionaries is used, so an empty list `articles` is created before starting the iteration across all the news articles.

* Since we want to keep only few fields from the `articles` list, a for-loop is used to iterate across al list elements to fetch every article data.

* A new element is appended to the list on every iteration with an additional key for the language.

* Comment to students that a `try - except` block is used to bypass any list attribute error.

![Important points on the create_df() function](Images/create_df_function.png)

Once the `create_df()` function is coded, one DataFrame per language is created and both DataFrames are concatenated with the `pd.concat()` function.

```python
# Create a DataFrame with the news in English
crisis_en_df = create_df(crisis_news_en["articles"], "en")

# Create a DataFrame with the news in Spanish
crisis_es_df = create_df(crisis_news_es["articles"], "es")

crisis_df = pd.concat([crisis_en_df, crisis_es_df])
```

Finally the head an tail of the DataFrame is shown and it's saved as a CSV file for further usage on the next activities.

Answer any additional question before moving to the next activity.
