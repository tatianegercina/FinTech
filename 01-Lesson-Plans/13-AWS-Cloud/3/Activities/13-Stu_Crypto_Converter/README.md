# Extended Crypto Converter

Customers just loved the new chatbot to convert from US Dollars to Bitcoin, however people started to ask about some other cryptocurrencies. After reviewing the conversations logs, you realized that customers are interested on Bitcoin, Ethereum and Ripple, so you decide to extend your crypto converter to allow customers to convert from US Dollars to one of these three cryptocurrencies.

## Instructions

### Create a custom slot

1. Login into the AWS Management Console using your `Admin` user, navigate to the Amazon Lex console and create a new custom slot in the `convertUSD` intent of the `Crypto_Converter` bot as follows:

    * **Slot type name:** `CryptoCurrency`
    * **Description:** `Available cryptocurrencies to convert.`
    * **Slot Resolution:** Choose _Restrict to Slot values and Synonyms_.
    * **Value:** Add three values and synonyms, one per each cryptocurrency as can be seen bellow.

  ![New custom slot configuration](Images/configure-new-slot-type.png)

2. Add a new slot named `crypto`, click on the _Slot type_ dropdown list and you will see your brand new slot type, select `CryptoCurrency` from the list. End the slot configuration by typing `What cryptocurrency do you want to convert to?` on the prompt.

![Crypto slot configuration](Images/add-crypto-slot.png)

3. In order to use your new `crypto` slot on the bot's conversation, modify your sample utterances to add a better dialog that includes the new slot as is shown bellow.

![New utterances](Images/new-crypto-utterances.png)

4. Build the bot and test it on the Test bot window. Start with typing the sample utterance `I want to invest in crypto` in oder to elicit all the slots as follows.

![Sample bot test](Images/custom_slots_1.gif)

5. Modify the `crypto` slot to add one response card to allow users to choose between Bitcoin, Ethereum or Ripple. Use the following configurations:

    * **Image URL:** Select any image of your preference, remember that this image should be publicly accessible.
    * **Tittle:** `Available CryptoCurrencies`
    * **Subtitle:** `Choose one crypto to convert`
    * Add one button per cryptocurrency as is shown bellow.

    ![Card buttons](Images/card-slot-values.png)

6. Build the bot and test it on the Test bot window. Start with typing the sample utterance `I want to buy crypto` in oder to elicit all the slots as follows.

![Response cards](Images/custom_slots_cards.gif)

## Hints

* You can store the response card image on an AWS S3 bucket, remember to configure public access to the image.
