# The Voice of the Blockchain

Canada lies at the frontier of the blockchain sector with increasing adoption rates and favorable regulations. For this activity, you will retrieve news articles in English and French regarding blockchain in Canada, to capture the voice of the blockchain.

## Instructions

### Loading Environment Variables

Create a .env file based on the the [example.env](Unsolved/example.env) starter file to create and export environment variables for the News API Key. Then, read and set the environment variables defined in your .env using the load_dotenv method.

### Getting News Articles in English

In this section, you will fetch news articles using the News API with the keywords `blockchain`, `canada`, and `2020` in English.

Refer to [the `everything` endpoint documentation](https://newsapi.org/docs/endpoints/everything) of the News API to find out how you can include these three keywords on the `q` parameter.

### Getting News Articles in French

Fetching news in French will require keywords in this language, so retrieve the news articles using the News API with the keywords `blockchain`, `canada`, and `2020`.

### Create a DataFrame with All the Results

The first task in this section is to create a function called `create_df(news, language)` that will transform the `articles` list in a DataFrame. This function will receive two parameters: `news` is the `articles` list and `language` is a string to specify the language of the news articles.

The resulting DataFrame should have the following columns:

* Title: The article's title
* Description: The article's description
* Text: The article's content
* Date: The date when the article was published on the format `YYYY-MM-DD` (eg. 2019-07-11)
* Language: A string specifying the news language (`en` for English, `fr` for French)

Once you have finished the function, do the following:

1. Use the `create_df()` function to create a DataFrame for the English news, and another for the French news.
2. Concatenate both DataFrames, with the English news at the top and the French news at the bottom.
3. Save the final DataFrame as a CSV file for further analysis in the forthcoming activities.
4. In order to preserve special characters, especially those in French, it's important to save the CSV using the `encoding='utf-8-sig'` parameter.

Your final DataFrame should look like this:

![Final news DataFrame example](Images/blockchain_news_df.png)

### Hint

You can use a for loop with the `create_df()` function inside to iterate across the news articles list to create the DataFrame's structure.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
