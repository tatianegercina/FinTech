### 6. Instructor Do: Getting Data for Sentiment Analysis (15 mins)

On this activity students will learn how to retrieve news articles from the [News API](https://newsapi.org/) and its [python library](https://newsapi.org/docs/client-libraries/python).

**Files:**

* [sentiment_analysis_data.ipynb](Activities/06-Ins_Sentiment_Analysis_Data/Solved/sentiment_analysis_data.ipynb)
* [keys.sh](Activities/06-Ins_Sentiment_Analysis_Data/Solved/keys.sh)

Explain students that there are several ways to retrieve data for sentiment analysis such as web scrapping, manual corpus creation from documents digitalization, documents transformations (e.g. from PDF, word processors or spreadsheets to raw text) and using APIs. Among these data retrieval mechanisms APIs is one of the most used, so in this activity students will learn how to retrieve news articles using the [News API](https://newsapi.org/) and its [python library](https://newsapi.org/docs/client-libraries/python).

Open the [News API](https://newsapi.org/) website and explain that it's an easy-to-use API that returns JSON metadata for headlines and articles live all over the web right now, so the results retrieved at this moment could be totally different than the results retrieved in 20 minutes.

Slack-out the News API web address to students (https://newsapi.org/) and ask them to create an account by clicking on the **Get API Key** button on the upper right corner.

![News API homepage](Images/news_api_homepage.png)

Guide students on the account process creation by following these steps:

* On the registration form, the **I am an individual** option should be selected to create a free developer account. It's also important to select the last two check boxes since this is a free service.
  ![News API registration form](Images/news_api_registration_form.png)

* Once the account is created the API key shown on [the Account page](https://newsapi.org/account).

  ![News API account page](Images/news_api_account_details.png)

Ask students to create an environment variable called `news_api` by adding their API key to the `keys.sh` script and executing it on the terminal window as they did on the APIs Unit.

You are almost ready to code! Before starting the demo, ask students to install the [News API python library](https://newsapi.org/docs/client-libraries/python) on their virtual environment by executing the following command.

  ```bash
  pip install newsapi-python
  ```

Open [the unsolved Jupyter notebook](Activities/06-Ins_Sentiment_Analysis_Data/Unsolved/sentiment_analysis_data.ipynb) and live code the demo by highlighting the following:

* The `NewsApiClient` class should be imported to interact with the News API service.

  ```python
  from newsapi import NewsApiClient
  ```

* To create a `NewsApiClient` object the API key should be passed as parameter.

  ```python
  newsapi = NewsApiClient(api_key=api_key)
  ```

Switch to the [the News API documentation](https://newsapi.org/docs/endpoints) and explain that there are three different endpoints, encourage students to review the API documentation to learn more about all the different request parameters they have available:

* _Top Headlines:_ Returns breaking news headlines, the most relevant request parameters are `q` for the search terms, `language` and `country`.
* _Everything:_ Retrieves news and articles from over 30,000 different sources, the most relevant request parameters are `q` for the search terms, `language` and `sort_by`.
* _Sources:_ Returns information about the most important article sources that this service indexes.

Switch back to the Jupyter notebook and mention to students that you will focus on using the _Top Headlines_ and _Everything_ endpoints, slack-out the [News API Python Client Library reference page](https://newsapi.org/docs/client-libraries/python) and encourage them to learn more about this library and it's options.

Start the live coding demo by highlighting the following:

* The `get_top_headlines()` method fetches top news articles about the keyword defined on the `q` parameter. This example gets top headlines about oil (`q="oil"`) in English language (`language="en"`) from the United States (`country="us"`).

  ```python
  oil_headlines = newsapi.get_top_headlines(
    q="oil",
    language="en",
    country="us"
  )
  ```

* The python client library transform the API response to a python dictionary, so elements of the JSON schema can be accessed by key.

  ![News API sample reponse](Images/news_api_sample_response.png)

* The total number of articles can be retrieved from the `totalResults` key and the content of a single article from the `articles` key.

  ![Accessing the News API dictionary](Images/news_api_top_headlines.png)

Show students how they can create a DataFrame using the response python dictionary for further analysis, data manipulation or storing the data.

  ![Creating a DataFrame from the response python dictionary](Images/news_api_df.png)

Live code the `newsapi.get_everything()` demo by highlighting that it's also possible to send more than one keyword as search term, like this example to fetch news about _Facebook Libra_ using `q="facebook libra"` as parameter.

* Separating two keywords by a blank space is equivalent to use `q="facebook AND libra"`.

  ```python
  libra_headlines = newsapi.get_everything(
      q="facebook libra",
      language="en",
      sort_by="relevancy"
  )
  ```

Answer any question that could arise and move to the next activity.
