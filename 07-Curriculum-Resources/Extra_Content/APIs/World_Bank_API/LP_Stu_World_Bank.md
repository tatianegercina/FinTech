### X. Students Do: World Bank API (15 mins)

**Instructions:**

* [README.md](Activities/05-Stu_World_Bank/README.md)

**Files:**

* [world_bank_api.ipnb](Activities/05-Stu_World_Bank/Unsolved/world_bank_api.ipynb)

### X. Instructor Do: Review World Bank API (10 mins)

**Files:**

* [world_bank_api.ipnb](Activities/05-Stu_World_Bank/Solved/world_bank_api.ipynb)

Live code the solution and explain the following:

* The world bank api provides data in multiple formats. The `format=json` section tells the API to send the JSON version of the data.

   ```python
   url = "http://api.worldbank.org/v2/countries?format=json"
   ```

* To identify the country id, we can either print all of the countries (messy), or we can use the name field to only print Aruba.

  ```python
  countries = data[1]
  for country in countries:
      if country["name"] == "Aruba":
          print(country["name"], country["id"])
  ```

 * The country id can be used to filter the indicators to a single country. Without this filter, all countries would be returned in the data.

    ```python
    country = "ABW"
    url = f'http://api.worldbank.org/v2/country/{country}/indicator/NY.GDP.MKTP.CD?format=json'
    ```


 Explain that it is very common to have to chain API requests in order to obtain all of the data needed from an API.

 Ask for any remaining questions before moving on.
