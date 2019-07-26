### 11. Instructor Do: Review Correlating Returns (10 mins)

**Files:**

* [correlating_returns.ipynb](Activities/06-Stu_Correlating_Returns/Solved/correlating_returns.ipynb)

Open the solved notebook. First, ask a volunteer to walk through the code in the headline download function below, explaining the input and output.

* The newsapi allows only a limited number of articles to be accessed for each day, which is why we only use the 20 most relevant articles. It also truncates the full text of the article. 

```python
def get_headlines(keyword):
    all_headlines = []
    all_dates = []
    date = '2019-07-24'
    while date > '2019-06-25':
        articles = (newsapi.get_everything(q=keyword, 
                                              from_param=date, 
                                              to=date,
                                              language='en',
                                              sort_by='relevancy',
                                              page=1))
        headlines = []
        for i in range(0, len(articles['articles'])):
            headlines.append(articles['articles'][i]['title'])
        all_headlines.append(headlines)
        all_dates.append(date)
        date = datetime.strftime(datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1), '%Y-%m-%d')
    return all_headlines, all_dates
```

Walk through the next few blocks of code, which contain the keywords we chose to look for. Ask the class what other keywords they used, and why they thought those topics might be correlated with Apple stock. 

* The function below calculates an average sentiment score for each day for each topic. We chose to take the average of the compound sentiment score as implemented by vader. 

```python
def headline_sentiment_summarizer_avg(headlines):
    sentiment = []
    for day in headlines:
        day_score = []
        for h in day:
            if h == None:
                continue
            else:
                day_score.append(sid.polarity_scores(h)['compound'])
        sentiment.append(sum(day_score) / len(day_score))
    return sentiment
```

* After calculating the sentiment scores and merging it with the stock return that we get from the IEX API, we generate the correlatation coefficients between each variable in the DataFrame. One useful trick when looking for strong correlations, especially when there are many variables of interest, is to use pandas' style module to visualize the DataFrame as a heatmap. 

```python
topic_sentiments.corr().style.background_gradient()
```

  ![corr1](Images/corr1.png)

Ask students whether they found topic sentiments that are more closely correlated with AAPL returns. Ask volunteers whether they might expect correlations between sentiment and returns to remain stable over time for a given topic/stock pairing. 