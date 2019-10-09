# The Voice of the Crisis

Despite it happening over a decade ago, the financial crisis of 2008 is still in the news because of its effects on the global economy. In this activity, you will retrieve news articles about this historical economic event in English and French to capture the voice of the crisis in two different languages.

## Instructions

### Getting News Articles in English

In this section you have to fetch news articles using the News API with the keywords `financial`, `crisis`, and `2008` in English.

Refer to [the `everything` endpoint documentation](https://newsapi.org/docs/endpoints/everything) of the News API to find out how you can include these three keywords on the `q` parameter.

### Getting News Articles in French

Fetching news in French will require keywords in this language, so retrieve the news articles using the News API with the keywords `crise`, `financière`, and `2008`. Be aware of the grave accent on the first `è` in `financière`.

### Create a DataFrame with All the Results

The first task in this section is to create a function called `create_df(news, language)` that will transform the `articles` list in a DataFrame. This function will receive two parameters: `news` is the `articles` list and `language` is a string to specify the language of the news articles.

The resulting DataFrame should have the following columns:

* Title: The article's title
* Description: The article's description
* Text: The article's content
* Date: The date when the article was published on the format `YYYY-MM-DD` (eg. 2019-07-11)
* Language: A string specifying the news language (`en` for English, `fr` for French)

Once you finished the function do the following:

* Use the `create_df()` function to create a DataFrame for the English news and another for the French news.
* Concatenate both DataFrames having the English news at the top and the French news at the bottom.
* Save the final DataFrame as a CSV file for further analysis in the forthcoming activities.
* In order to preserve special characters, especially those in French, it's important to save the CSV using the `encoding='utf-8-sig'` parameter.

Your final DataFrame should look like this:

![Final news DataFrame example](Images/crisis_news_df.png)

### Hints

You can use a `for-loop` with the `create_df()` function inside to iterate across the news articles list to create the DataFrame's structure.



© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.