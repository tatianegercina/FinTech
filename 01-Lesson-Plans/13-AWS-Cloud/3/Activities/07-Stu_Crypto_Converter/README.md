# Extended Crypto Converter

Customers just loved the new chatbot to convert from US Dollars to Bitcoin; however people started to ask about some other cryptocurrencies. After reviewing the logs of the conversations, you realized that customers are interested in Bitcoin, Ethereum, and Ripple, so you decide to extend your crypto converter to allow customers to convert from US Dollars to one of these three cryptocurrencies.

## Instructions

### Create a custom slot

1. Log-in to the AWS Management Console using your `Admin` user, navigate to the Amazon Lex console and create a new custom slot in the `ConvertUSD` intent of the `Crypto_Converter` bot as follows:

    * **Slot type name:** `CryptoCurrency`
    * **Description:** `Available cryptocurrencies to convert.`
    * **Slot Resolution:** Choose _Restrict to Slot values and Synonyms_.
    * **Value:** Add three values and synonyms, one per each cryptocurrency, as can be seen, below.

    ![New custom slot configuration](Images/configure-new-slot-type.png)

2. Add a new slot named `crypto`, click on the _Slot type_ dropdown list, and you will see your brand new slot type, select `CryptoCurrency` from the list. End the slot configuration by typing `What cryptocurrency do you want to convert to?` on the prompt.

    ![Crypto slot configuration](Images/add-crypto-slot.png)

3. To use your new `crypto` slot on the bot's conversation, modify your sample utterances to add a better dialog that includes the new slot, as is shown below.

    ![New utterances](Images/new-crypto-utterances.png)

4. Build the bot and test it in the Test bot window. Start with typing the sample utterance `I want to invest in crypto` to elicit all the slots as follows.

    ![Sample bot test](Images/custom_slots_1.gif)

5. Modify the `crypto` slot to add one response card to allow users to choose between Bitcoin, Ethereum, or Ripple. Use the following configurations:

    * **Image URL:** Select any image of your preference, remember that this image should be publicly accessible.
    * **Title:** `Available CryptoCurrencies`
    * **Subtitle:** `Choose one crypto to convert`
    * Add one button per cryptocurrency as is shown below.

    ![Card buttons](Images/card-slot-values.png)

6. Build the bot and test it on the Test bot window. Start with typing the sample utterance `I want to buy crypto` to elicit all the slots as follows.

    ![Response cards](Images/custom_slots_cards.gif)

### Add Ethereum and Ripple conversion to Lambda

As you noticed, the bot allows users to select between Bitcoin, Ethereum, and Ripple, however it's not making the accurate cryptocurrency conversions from US Dollars, now it's time to extend your Lambda function to solve this issue.

1. Open the code of your `convertUSD` Lambda function on the AWS Lambda online code editor, make a backup copy just in case you need to restore your function.

2. Create a new helper function called `get_cryptoprice(crypto)` that will receive as parameter the name of the cryptocurrency selected by the user and should return the price of the selected cryptocurrency in US Dollars. As a starting code, you can use the `get_btcprice()` function's code. To retrieve the current price of Ethereum and Ripple, use the following endpoints from the alternative.me Crypto API.

    * **Ethereum:** https://api.alternative.me/v2/ticker/Ethereum/?convert=USD
    * **Ripple:** https://api.alternative.me/v2/ticker/Ripple/?convert=USD

3. Modify the `convert_usd()` function as follows:

    * Add the code needed to fetch the value of the `crypto` slot.
    * Modify the following code at your convenience, to call the `get_cryptoprice()` function, and calculate the conversion from US Dollars to the selected cryptocurrency.

      ```python
      btc_value = parse_float(usd_amount) / get_btcprice()
      btc_value = round(btc_value, 4)

      # Return a message with conversion's result.
      return close(
          intent_request["sessionAttributes"],
          "Fulfilled",
          {
              "contentType": "PlainText",
              "content": """Thank you for your information;
              you can get {} Bitcoins for your {} US Dollars.
              """.format(
                  btc_value, usd_amount
              ),
          },
      )
      ```

4. Remove the `get_btcprice()` function - you won't need it anymore.

5. Create at least three test events, one per cryptocurrency, to validate that the code is working correctly.

6. Open the Amazon Lex console and test the bot in the _Test bot_ window. Since you only made changes to Lambda, there is no need to build the bot. You should now see accurate conversions for each cryptocurrency as it's shown below.

    ![Extended Crypto Converted demo](Images/crypto_converter_extended.gif)

## Hints

* You may have to refresh the Lex intent page after creating the custom slot and the lambda function in order to see them in the options.

* Make sure your intent and slot names are named correctly in your Lambda code.  The names in Lex should match the names in Lambda exactly:

![Lex_Names1](Images/Lex_names1.png)
![Lex_Names2](Images/Lex_names2.png)

* You can store the response card image on an AWS S3 bucket, remember to configure public access to the image.

* Remember to save your Lambda function once in a while to prevent code loses.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
