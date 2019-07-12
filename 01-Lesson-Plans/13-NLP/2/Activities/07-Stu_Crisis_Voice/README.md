# The Voice of the Crisis

Despite it happened over a decade ago, the financial crisis of 2008 is still on the news due to its effects in global economy. On this activity you will retrieve news articles about this historical economic fact in English and Spanish to capture the voice of the crisis in two different languages.

## Retrieve News Articles in English

In this section you have to fetch all the news articles using the News API using the keywords `financial`, `crisis`, and `2008` in English.

Refer to [the `everything` endpoint documentation](https://newsapi.org/docs/endpoints/everything) of the News API to find out how you can include these three keywords on the `q` parameter.

## Retrieve News Articles in Spanish

Fetching news on Spanish will require keywords on this language, so retrieve all the news articles using the News API using the keywords `crisis`, `financiera`, and `2008`.

## Create a DataFrame with All the Results

The first task on this section is to create a function called `create_df(news, language)` that will transform the `articles` list in a DataFrame. This function will receive two parameters: `news` is the `articles` list and `language` is a string to specify the language of the news articles.

The resulting DataFrame should have the following columns:

* Title: The article's title
* Description: The article's description
* Text: The article's content
* Date: The date when the article was published on the format `YYY-MM-DD` (eg. 2019-07-11)
* Language: A string specifying the news language (`en` for English, `es` for Spanish)

**Hint:** You can use a for-loop to iterate across all the news articles to create the DataFrame's structure.

Once you finished the function do the following:

* Use the `create_df()` function to create a DataFrame for the English news and another for the Spanish news.
* Concatenate both DataFrames having the English news at the top and the Spanish news at the bottom.
* Save the final DataFrame as a CSV file for further analysis on the forthcoming activities.
* In order to preserve special characters, especially those in Spanish, it's important to save the CSV using the `encoding='utf-8-sig'` parameter.

Your final DataFrame should look like this:

![Final news DataFrame example](../../Images/crisis_news_df.png)
