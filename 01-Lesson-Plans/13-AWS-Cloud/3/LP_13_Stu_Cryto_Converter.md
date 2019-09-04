### 13. Students Do: Crypto Converter (20 mins)

In this activity, students will extend their cryptocurrency converter by adding a custom slot to allow users to select between Bitcoin, Ethereum or Ripple to convert from US Dollars. Also, business logic to identify the cryptocurrency selected by the user and make the conversion will be added to the Lambda function.

**Instructions:**

* [README.md](Activities/13-Stu_Crypto_Converter/README.md)

**Files:**

* [lambda_function.py](Activities/13-Stu_Crypto_Converter/Unsolved/lambda_function.py)

---

### 14. Instructor Do: Review Crypto Converter (10 mins)

**Files:**

* [lambda_function.py](Activities/13-Stu_Crypto_Converter/Solved/lambda_function.py)

Start by reviewing the bot configuration. Open the Amazon Lex console, navigate to the `ConvertUSD` intent editor on the `Crypto_Converter` bot and highlight the following:

* As you presented on the previous demo, students should have created a new slot type called `CryptoCurrency` with the following structure:

  ![CrytoCurrency Slot Type](Images/cryptocurrency_slot_type.png)

* The user can use either, the value or the synonyms to refer to the cryptocurrencies while talking to the bot.

* Once the new slot type is created, it's possible to add the `crypto` slot to the intent.

* The `crypto` slot is configured to show prompt response cards as follows:

  ![Crypto slot response cards](Images/crypto_slot_response_cards.png)

* The card image should be a public image, it can be stored anywhere on the web; an AWS S3 public asset could be the best option.

Continue to the Lambda function code, open the solution on your AWS Lambda online code editor and highlight the following:

* There is no need to validate the name of the cryptocurrency since it is not typed by the user.

* On the `get_cryptoprice()` function, the price for each cryptocurrency is retrieved from CoinMarketCap using an URL defined on a `nested-if` structure.

  ```python
  def get_cryptoprice(crypto):
      """
      Retrieves the current price of BTC, ETH or XRP in US Dollars from CoinMarketCap.
      """
      url = ""
      if crypto == "Bitcoin":
          url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
      elif crypto == "Ethereum":
          url = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
      else:
          url = "https://api.coinmarketcap.com/v1/ticker/ripple/"

      response = requests.get(url)
      response_json = response.json()
      price_usd = parse_float(response_json[0]["price_usd"])
      return price_usd
  ```

* To fetch the value of the `crypto` slot, a new variable called `crypto` were defined at the beginning of the `convert_usd()` function.

  ```python
  crypto = get_slots(intent_request)["crypto"]
  ```

* The `get_cryptoprice()` function is used in the `convert_usd()` function to fetch the current price of the selected cryptocurrency, next the conversion to US Dollars is calculated.

  ```python
  # Get the current price of BTC, ETH or XRP in USD and make the conversion from USD.
  crypto_value = parse_float(usd_amount) / get_cryptoprice(crypto)

  crypto_value = round(crypto_value, 4)
  ```

* The fulfillment message is formated in the `convert_usd()` function to include the name of the selected crypto currency dynamically.

  ```python
  # Return a message with conversion's result.
  return close(
      intent_request["sessionAttributes"],
      "Fulfilled",
      {
          "contentType": "PlainText",
          "content": """Thank you for your information;
          you can get {} {} for your {} US Dollars.
          """.format(
              crypto_value, crypto, usd_amount
          ),
      },
  )
  ```

Continue to the Amazon Lex console, test the bot to validate the changes made on Lambda; you should see a dialog as follows.

![Extended Cryto Converter demo](Images/crypto_converter_extended.gif)

Answer any reminder question before moving forward.
