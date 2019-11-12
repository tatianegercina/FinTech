# Crisis Sentiment Analysis Dashboard

This activity is a mini-project where you'll create a data visualization dashboard. You will analyze sentiment and tone about the news related to the financial crisis of 2008 that were published in the past month. You'll retrieve the news articles from the News API; by default, the developer account gives access to news articles up to a month old.

In this activity, you will use your new sentiment analysis skills in combination to some of the skills you have already mastered. such as Pandas, PyViz, Plotly Express, and PyViz Panel.

---

## Instructions

For this activity you have two starting files:

* [sentiment_analysis.ipynb](Resources/sentiment_analysis.ipynb): Start working with this Jupyter notebook; it's a sandbox workspace where you will conduct the sentiment analysis tasks and charts creation before assembling the dashboard.

* [sentiment_dashboard.ipynb](Resources/sentiment_dashboard.ipynb): In this Jupyter notebook, you will compile the visualizations from the previous analysis into functions that can be used for a Panel dashboard.

This activity is intended to be done on teams up to three people.

### Crisis Sentiment Analysis

In this section, you will work with the `sentiment_analysis.ipynb` starter Jupyter notebook and perform the following tasks.

#### Fetching the Latests News About the Crisis of 2008

Using the News API, get all the news in English about the financial crisis of 2008 using the keywords `"financial AND crisis AND 2008"` in the `q` parameter. Define a `page_size=100` to have at least 100 news articles to analyze.

#### Creating a VADER Sentiment Scoring Function

Use the VADER sentiment scoring function from `NLTK` to score the sentiment polarity of the 100 news articles you fetched.

For convenience, start downloading the `vader_lexicon` in order to initialize the VADER sentiment analyzer.

In order to score the VADER sentiment, create a function named `get_sentiment_scores(text, date, source, url)` that will receive four parameters.

* `text` is the text whose sentiment will be scored.
* `date` the date the news article was published using the format `YYYY-MM-DD`.
* `source` is the name of the news article's source.
* `url` is the URL that points to the article.

The `get_sentiment_score()` function should return a Python dictionary with the scoring results. This dictionary is going to be used in the next section to create a DataFrame. The structure of the dictionary is the following:

* `date` the date passed as parameter to the function.
* `text` the text passed a parameter to the function.
* `source` the source passed as parameter to the function.
* `url` the URL passed as parameter to the function.
* `compound` the compound score from the VADER sentiment analyzer.
* `pos` the positive score from the VADER sentiment analyzer.
* `neu` the neutral score from the VADER sentiment analyzer.
* `neg` the negative score from the VADER sentiment analyzer.
* `normalized` the normalized scored based on the `compound` results. Its value should be `1` for positive sentiment, `-1` for negative sentiment, and `0` for neutral sentiment.

This is an example of the function's return value:

```python
{'date': '2019-06-24',
 'text': '\nMore than a decade since the global economic meltdown of 2008
  devastated lives across the world, no one who caused the crisis has
  been held responsible.\n\n"The 2008 financial crisis displayed what
  the world now identifies as financial contagion," says Philip J Baker,
  the former managing partner of a US-based \nhedge fund that collapsed
  during the financial crisis.\n\nDespite this, "zero Wall Street chief
  executives have been to prison, even though there is today absolutely
  no doubt that Wall Street executives and politicians \nwere complicit
  in creating the crisis," he says. \n\nBaker was among the few
  relatively smaller players imprisoned for the part they played.\n\n
  In July 2009, he was arrested in  Germany and extradited to the
  United States where he faced federal court on charges of fraud and
  financial crimes.\n\nHe pled guilty and was sentenced to 20 years
  in prison for costing some 900 investors about $294mn worldwide.
  He served eight years in jail and is now on \nparole and advocates
  against financial crime.\n',
 'source': 'aljazeera',
 'url': 'https://www.aljazeera.com/programmes/specialseries/2019/06/men-stole-world-2008-financial-crisis-190611124411311.html',
 'compound': -0.9911,
 'pos': 0.048,
 'neu': 0.699,
 'neg': 0.254,
 'normalized': -1}
```

#### Creating the News Articles' Sentiments DataFrame

In this section, you have to create a DataFrame that is going to be used to plot the sentiment analysis results.

Using a `for-loop`, iterate across all the news articles you fetched to create the DataFrame structure.

Define an empty list to append the sentiment scoring results for each news article and create the DataFrame using the list as data source.

Once you create the DataFrame do the following:

* Sort the DataFrame rows by the `date` column.
* Define the `date` column as the DataFrame index.
* Save the DataFrame as a CSV file in order to use it on the sentiment analysis dashboard creation.

The DataFrame should look like this:

![Sample news articles DataFrame](Images/news_df_sample.png)

#### Creating the Average Sentiment Chart

Use `hvPlot` to create a two lines chart that compares the average `compound` and `normalized` sentiment scores along the last month. You can see a sample plot bellow.

![Two line chart sample](Images/two_line_sentiment_plot.png)

#### Creating the Sentiment Distribution Chart

Based on the `normalized` sentiment score, create a bar chart like the one bellow using `hvPlot` that shows the number of negative, neutral and positive news articles. This chart represents the overall sentiment distribution.

![Overall sentiment bar chart sample](Images/overall_sentiment_dist.png)

#### Getting the Top 10 Positive and Negative News Articles

In this section you have to create two DataFrames, one with the top 10 positive news according to the `compound` score, and other with the top 10 negative news.

Refer to the [`hvplot.table()` documentation](https://hvplot.pyviz.org/user_guide/Plotting.html#Tables) to create two tables presenting the following columns of these news articles:

* Date
* Source
* Text
* URL

A sample table is shown bellow.

![Sample hvPlot table](Images/sample_hvplot_table.png)

#### Creating the Sentiment Distribution by News Article's Source

In this section, use `hvPlot` to create a bar chart like the one bellow that presents the distribution of negative, neutral and positive news according to the `normalized` score; the results should be grouped by `source`.

![Sample bar char of sentiments by source](Images/sentiments_by_source.png)

#### Creating the Word Clouds

In this section you will create two word clouds, one using the bag-of-words method and other using TF-IDF.

#### Bag-of-Words' Word Cloud

Use the `CountVectorizer` module from `sklearn` to create a word cloud with the top 20 words with the highest counting.

Save the DataFrame with the top 20 words as a CSV file named `top_words_data.csv` for future use on the dashboard creation.

![Sample bag-of-words word cloud](Images/bow_wordcloud.png)

#### TF-IDF Word Cloud

Use the `TfidfVectorizer` module from `sklearn` to create a word cloud with the top 20 words with the highest frequency.

Save the DataFrame with the top 20 words as a CSV file named `top_wors_tfidf_data.csv` for future use on the dashboard creation.

![Sample TF-IDF word cloud](Images/tfidf_wordcloud.png)

### Crisis Sentiment Dashboard

On this section, you will use the `sentiment_dashboard.ipynb` starter file to compile the visualizations from the previous analysis into functions to be used for a Panel dashboard.

#### Loading Data

In this section, you will load the CSV files you created on the analysis notebook:

* The `news_vader.csv` file with all the news articles and the VADER sentiment scores.

* The `tone_data.csv` file with the IBM Watson Tone Analyzer results.

* The `top_words_data.cvs` file with the top 20 words for creating the word cloud based on the bag-of-words method.

* The `top_words_tfidf_data.cvs` file with the top 20 words for creating the word cloud based on TF-IDF.

#### Plots Functions

In this section, you will copy the code for each plot type from your analysis notebook and place it into separate functions that the Panel can use to create panes for the dashboard. These functions will convert the plot object to a Panel pane.

Be sure to include any DataFrame transformation or manipulation code required along with the plotting code.

Return a Panel pane object from each function that can be used to build the dashboard.

**Note:** Remove any .show() lines from the code. We want to return the plots instead of showing them. The Panel dashboard will then display the plots.

#### Dashboard Creation

In this section, you will combine all of the plots into a single dashboard view using Panel. Be creative with your dashboard design!

Bellow you can find a sample dashboard.

![Sample DashBoard](Images/sentiment_analysis_dashboard.gif)

## Challenge: Radar Chart with Tone Analysis

In this challenge section, you will use Plotly Express and IBM Watson Tone Analyzer to create a radar chart presenting the tone of all the news articles that you retrieved.

Refer to the [polar coordinates chart demo](https://plot.ly/python/plotly-express/#polar-coordinates) and the [Plotly Express reference documentation](https://www.plotly.express/plotly_express/#plotly_express.scatter_polar) to learn more about how to create this chart.

In order to create the radar chart, you need to score the tone of each article and retrieve the `document_tone`.

Create a function named `get_tone(text,url)` that will receive two parameters and will get the tone score for a particular article.

* `text` the content of the article

* `url` the URL pointing to the article

The `get_tone()` function will use the `tone()` method from the `ToneAnalyzerV3` module to score the article's tone. Remember that for each document (or text), the `tone()` method of IBM Watson Tone Analyzer [scores one or more overall document tones](https://cloud.ibm.com/apidocs/tone-analyzer#analyze-general-tone-get), you can also get and empty result if no tone were scored; this function should return a dictionary with the first document tone's score with the following structure:

* `score` refers to the first `tone` from the `document_tone`.

* `tone_id` refers to the `tone_id` from the first `tone`.

* `tone_name` refers to the `tone_name` from the first `tone`.

* `text` the text passed as parameter.

* `url` the URL passed as parameter.

This is an example of the function's return value:

```python
{'score': 0.616581,
 'tone_id': 'sadness',
 'tone_name': 'Sadness',
 'text': '\nMore than a decade since the global economic meltdown of 2008
  devastated lives across the world, no one who caused the crisis has
  been held responsible.\n\n"The 2008 financial crisis displayed what
  the world now identifies as financial contagion," says Philip J Baker,
  the former managing partner of a US-based \nhedge fund that collapsed
  during the financial crisis.\n\nDespite this, "zero Wall Street chief
  executives have been to prison, even though there is today absolutely
  no doubt that Wall Street executives and politicians \nwere complicit
  in creating the crisis," he says. \n\nBaker was among the few
  relatively smaller players imprisoned for the part they played.\n\n
  In July 2009, he was arrested in  Germany and extradited to the
  United States where he faced federal court on charges of fraud and
  financial crimes.\n\nHe pled guilty and was sentenced to 20 years
  in prison for costing some 900 investors about $294mn worldwide.
  He served eight years in jail and is now on \nparole and advocates
  against financial crime.\n',
'url': 'https://www.aljazeera.com/programmes/specialseries/2019/06/men-stole-world-2008-financial-crisis-190611124411311.html'}
```

Create a DataFrame with the tone scoring from all the news articles. Use an empty list to create a the DataFrame's structure and a `for-loop` to iterate across all the news to score their tone using the `get_tone()` function.

The final DataFrame should look as follows.

![Sample DataFrame for the radar chart](Images/radar_chart_df.png)

Save the DataFrame as a CSV file named `tone_data.csv` for further use on the dashboard creation.

Create a radar chart like the one bellow using the `bar_polar()` method from Plotly Express as follows:

* Use the `score` column for the `r` and `color` parameters.

* Use the `tone_name` column for the `theta` parameter.

* Use the `url` column for the `hover_data` parameter.

* Define a `title` for the chart.

  ![Sample radar chart](Images/radar_chart.png)





© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
