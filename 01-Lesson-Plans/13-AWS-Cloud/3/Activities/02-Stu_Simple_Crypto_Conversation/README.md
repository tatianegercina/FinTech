# Crypto Converter

You are part of the innovation team at one of the biggest banks in the country. Top management wants to know if there is any interest from current customers on cryptocurrencies, so you are asked to find a creative way to ask customers about it.

You decided to go beyond the typical online survey or the old-fashioned phone call, so you resolve to create a chatbot that will help customers to convert from US Dollars to Bitcoin. Your hypothesis is if there is any interest from customers on cryptocurrencies, they will, at least, ask about their value.

## Instructions

### Create a custom bot

1. Log-in to the AWS Management Console using your `Admin` user, navigate to the Amazon Lex console and create a new custom bot with the following parameters:

    * _Bot name:_ `Crypto_Converter`
    * _Output voice:_ Salli
    * _Session timeout:_ 5 min
    * _Sentiment analysis_: `No`
    * _COPPA:_ Select `No`

    ![Crypto converter creation](Images/cypto_converter_creation.png)

### Create and configure an intent

2. Add a new intent and name it `ConvertUSD`.

3. Define some sample utterances, start by adding the following:

    * `I want to convert USD to BTC`
    * `I want to convert dollars to BTC`
    * `I want to convert dollars to bitcoin`

4. Add two slots as follows:

    | Name | Slot type | Prompt |
    | --------- | ------------- | ------------------------------------------------------------------------------------------------------- |
    | birthday | AMAZON.DATE | This service can only be used by people over 21 years old, could you please give me your date of birth? |
    | usdAmount | AMAZON.NUMBER | How many US Dollars do you want to convert? |

5. Add the following two utterances; how do you think they will work?

    * `I want to convert ​{usdAmount}​ dollars to bitcoin`
    * `I want to convert ​{usdAmount}​ dollars to BTC`

6. On the _Confirmation prompt_ section, add the following confirm and cancel prompts.

    * _Confirm prompt:_ `Are you sure you want to convert {usdAmount} to Bitcoin?`
    * _Cancel prompt:_ `Okay, let's start again.`

In the end, your intent's configuration should look like this.

![Sample intent configuration](Images/converusd_intent.png)

### Build and test the bot

7. Build the bot by clicking on the _Build_ button.

8. Once the build process ends, test your bot with the sample utterances, you should have a final conversation flow like the following.

![Sample bot test](Images/crypto_converter_1.gif)

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
