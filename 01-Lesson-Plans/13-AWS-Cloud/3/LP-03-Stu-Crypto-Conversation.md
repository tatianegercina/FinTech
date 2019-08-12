### 3. Students Do: Simple Crypto Conversation (15 mins)

In Today's class, students will create a bot that converts a given amount on US Dollars to its value in bitcoin `BTC`, ethereum `ETH` or ripple `XRP`. In this activity, students will start creating the bot by defining an intent, some sample utterances and two slots in order to convert from US Dollars to `BTC`.

**Instructions:**

* [README.md](Activities/03-Stu_Simple_Crypto_Conversation/README.md)

---

### 4. Instructor Do: Review Simple Crypto Conversation (10 min)

**Files:**

* [Crypto Converted export file](Activities/03-Stu_Simple_Crypto_Conversation/Solved/Crypto_Converter_1_c99b8f7e-ea4d-4a6e-bb46-f179beeb5e60_Bot_LEX_V1.zip)

You can chose to live demo the solution or import the solution file into your Amazon Lex console.

To import the solution, click on the _Import_ option into the _Actions_ button and select the provided ZIP file; once the import process ends, you will have the bot and the intent available on your Amazon Lex console, be sure to build the bot before starting the review activity.

![Import Lex Bot](Images/import-lex-bot.png)

Click on the `Crypto_Converter` bot, once the `convertUSD` intent is on the screen highlight the following:

* Adding `{usdAmount}` on the sample utterances, will allow the user send messages like `I want to convert **100** dollars to BTC` where the deep learning algorithms will match the `{usdAmount}` label with a number on the utterance speech, as can be seen on the demo gif file bellow.

* When the bot is tested, the date of birth can be given on any format (e.g. `12/16/1978`, `16/12/1978`, `Dec 16, 1978`), using the `AMAZON.DATE` slot type will transform the date automatically to the `YYYY-mm-dd` format as can be seen on the demo gif file bellow.

  ![Demo bot test](Images/crypto_converter_1.gif)

Answer any questions before moving on.
