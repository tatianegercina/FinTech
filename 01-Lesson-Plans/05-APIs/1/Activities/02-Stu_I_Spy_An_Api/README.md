# I Spy an API

You've received an email from your Python mentor, Julia. Read it below to see if she has any new tasks for you.

> Good Morning Mentee,
>
> I was going through some old documents and came across this list of FinTech APIs that I researched when implementing a Monte Carlo portfolio simulation (see attached). They're not too fancy, but you could use them if you're ever in a bind and need to get financial data quickly. I've included brief descriptions of what each API does.
>
> Full disclosure: I haven't checked these APIs out in a while. I'd suggest testing them out to see if they're still functioning. Let me know your findings.
>
> All the Best,
>
>Julia

## Instructions

Investigate the following APIs using Postman. Be aware that you will need an API key for some of them.

APIs to investigate:

* [Quandl](https://www.quandl.com/): This API provides historical stock data, and would be useful if you needed to calculate cumulative returns for `GOOG`.

  > <https://www.quandl.com/api/v3/datasets/WIKI/GOOG.json?api_key=YOUR_KEY_GOES_HERE>

* [The World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889386-developer-information-overview): This API has a wealth of international bank data. If you wanted to analyze the growth rate of each country's gross domestic product values (GDP), you could extract GDP values, by year, from [The World Bank's Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation).

  > <http://api.worldbank.org/v2/country/ca/indicator/NY.GDP.MKTP.CD?format=json>

* [Coinbase](https://www.coinbase.com/): This API provides price data for cryptocurrencies. Use it if you need to get the price of a crypto at any given moment, such as `BTC`.

  > <https://api.coinbase.com/v2/prices/BTC-CAD/buy?format=json>

## Instructions

Using `Postman`, submit `GET` requests to the above APIs using the provided request URLs. Confirm that a response has been received from the servers.

It is recommended that you save each API request and the output so that it can be leveraged for future assignments.

1. Get `GOOG` stock data using `Quandl API`.

2. Get `GDP` data for `CA` using `World Bank API`.

3. Get the current `Bitcoin` price using `Coinbase API`.

The TAs will be circulating during this activity. Feel free to ask for assistance if you experience any trouble using Postman or any of the APIs.

Let the TAs know when you've finished the core activity. If time remains, give the challenge section a try.

### Challenge

1. Change the above `Quandl` request URL to query for `AMD` instead of `GOOG`.

2. Update the `Coinbase` request URL to query for `ETH-CAD` instead of `BTC-CAD`.

3. Use the `Quandl API` to get `GOOG` stock data in `CSV` format. Take note of how the change in URL alters the format (JSON vs. CSV) of the data returned by the API.

### Hint

The output format of an API can be changed by altering the `?format=` part of the link, or changing the extension of the target file from `json` to `csv`. See below for examples.

* Quandl -> <https://www.quandl.com/api/v3/datasets/WIKI/GOOG.json?api_key=YOUR_KEY_GOES_HERE>

* Quandl -> <https://www.quandl.com/api/v3/datasets/WIKI/GOOG.csv?api_key=YOUR_KEY_GOES_HERE>

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
