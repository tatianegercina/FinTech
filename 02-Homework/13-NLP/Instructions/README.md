# Unit 11 - Tales from the Crypto

![Stock Sentiment](Images/sentimental.jpeg)

## Background

There's been a lot of hype in the news lately about Cryptocurrency, so you want to "take stock" so-to-speak of the latest news headlines regarding Bitcoin and Ethereum to get a better feel for the current public sentiment around each coin.

In this assignment, you will apply natural language processing to understand the sentiment in the latest news articles featuring Bitcoin and Ethereum. You will also apply fundamental NLP techniques to better understand the other factors involved with the coin prices such as common words and phrases and organizations/entities mentioned in the articles.

Complete the following tasks:

1. [Sentiment Analysis](#Sentiment-Analysis)
2. [Natural Language Processing](#Natural-Language-Processing)
3. [Named Entity Recognition](#Named-Entity-Recognition)

- - -

### Files

[Starter Notebook](Starter_Code/stock_sentiment.ipynb)

- - -

### Instructions

#### Sentiment Analysis

Use the [newsapi](https://newsapi.org/) to pull the latest news articles for bitcoin and ethereum and create a DataFrame of sentiment scores for each coin.

Use descriptive statistics to answer the following questions:

> Which coin had the highest mean positive score?
>
> Which coin had the highest negative score?
>
> Which coin had the highest positive score?

#### Natural Language Processing

In this section, you will use NLTK and Python to tokenize the text for each coin. Be sure to:

1. Lowercase each word
2. Remove Punctuation
3. Remove Stopwords

Next, look at the ngrams and word frequency for each coin.

1. Use NLTK to produce the n-grams for N = 2.
2. List the top 10 words for each coin.

Finally, generate word clouds for each coin to summarize the news for each coin.

![btc-word-cloud.png](Images/btc-word-cloud.png)

![eth-word-cloud.png](Images/eth-word-cloud.png)

#### Named Entity Recognition

In this section, you will build a named entity recognition model for both coins and visualize the tags using SpaCy.

![btc-ner.png](Images/btc-ner.png)

![eth-ner.png](Images/eth-ner.png)

- - -

### Resources

[Vader Sentiment Analysis](http://www.nltk.org/howto/sentiment.html)

- - -

### Hints and Considerations

The free developer version of the news api limits the total monthly requests, so be careful not to exceed the free limits.

- - -

### Submission

* Create Jupyter Notebooks for the NLP analysis and host the notebooks on Github.

* Include a Markdown that summarizes your homework and include this report in your Github repo.

* Submit the link to your Github project to Bootcampspot.
