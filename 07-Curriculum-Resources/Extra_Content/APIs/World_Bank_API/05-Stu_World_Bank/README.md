# World Bank API

In this activity, you will use the world bank api to `GET` GDP information for Aruba.

## Instructions

* Use the [countries endpoint](https://datahelpdesk.worldbank.org/knowledgebase/articles/898590-country-api-queries) to GET the abbreviation for Aruba.

* Print the country name and id for all countries in the response.

* Use the [country id](https://datahelpdesk.worldbank.org/knowledgebase/articles/898599-indicator-api-queries) for Aruba to `GET` the GDP information.

## Bonus

* If time remains, try to create a line chart with the GDP information for each date.

## Hints

* In case you need some help with the API, visit the [documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures) to learn more.

Use the following URL for the GDP request. Simply replace the country id with the actual id for Aruba.

```python
url = f'http://api.worldbank.org/v2/country/{COUNTRY_ID}/indicator/NY.GDP.MKTP.CD'
```
