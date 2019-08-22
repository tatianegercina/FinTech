### 13. Instructor Do: Custom Slots (10 mins)

In this activity, students will learn how to create a custom slot and add it to an Amazon Lex bot intent.

**Files:**

* [Crypto Converter export file](Activities/13-Ins_Custom_Slots/Solved/Crypto_Converter_2_4aefdbf6-55cc-4892-b302-dc428c404e29_Bot_LEX_V1.zip)

Comment to students that it's possible to create custom slot types, this is intended to gather specific data values for a slot, for example the size of a pizza (personal, small, medium or large) on a pizza ordering bot. Explain to students that now you will show them how to create a custom slot to allow users to choose the cryptocurrency they want to convert to.

Open the Amazon Lex console and navigate to the `convertUSD` intent editor, on the left side menu, click on the blue plus symbol next to the _Slot types_ option to add a new custom slot type.

![Adding a new slot type](Images/add-slot-type.png)

Next, a popup window will appear, click on the _Create slot type_ option to continue.

![Create a new slot type](Images/create-slot-type.png)

Configure the new slot type as follows:

* **Slot type name:** `CryptoCurrency`
* **Description:** `Available cryptocurrencies to convert.`
* **Slot Resolution:** Choose _Restrict to Slot values and Synonyms_. By selecting this option the user has to choose only among the available options.
* **Value:** Add three values and synonyms, one per each cryptocurrency as can be seen bellow.

Once you are done, click on the _Save slot type_ button.

![Configuring the new slot type](Images/configure-new-slot-type.png)

Come back to the `convertUSD` intent editor, add a new slot named `crypto`, click on the _Slot type_ dropdown list and you will see your brand new slot type, select `CryptoCurrency` from the list. End the slot configuration by typing `What cryptocurrency do you want to convert to?` on the prompt.

![Add the crypto slot](Images/add-crypto-slot.png)

Explain students that now the bot is configured to elicit the `crypto` slot, however, we need to modify the utterances to add a better dialog that includes the new slot.

Modify the utterances to have the _Sample utterances_ like the ones shown bellow.

![New sample utterances](Images/new-crypto-utterances.png)

Highlight to students that on the new utterances, the word `bitcoin` has been substituted by the slot `crypto` in order to allow users to specify on their dialog what cryptocurrency they want to convert to, for example by typing `I want to convert USD to Ripple`.

Build the bot and test it on the _Test bot_ window. Start with typing the sample utterance `I want to invest in crypto` in oder to elicit all the slots as follows.

![Sample utterance 1](Images/custom_slots_1.gif)

Explain to students that, when the `crypto` slot is elicited, only the three options will be valid, however, giving the user the chance to type any cryptocurrency name could be prone to errors, that's why using _Card Slots_ could be useful.

To create a _Card Slot_, click on the gear icon next to `cypto` slot's prompt.

![Create a card slot](Images/create-card-slot.png)

The _Crypto settings_ window will open, scroll down to the _Prompt response cards_ section and start by adding this URL in the _Image URL_ text field: https://cdn1.iconfinder.com/data/icons/cryptocurrency-set-2018/375/Asset_1480-128.png. Comment to students that this URL should point to a public image that they can store as a public asset on an AWS S3 bucket, for this demo we are using a free public image from [Iconfinder](https://www.iconfinder.com/).

![Add card slot image](Images/add-card-slot-image.png)

Comment to students that a card slot can have up to five cards, in this demo we will create one card with three options. Continue by adding the tittle and subtitle as is shown bellow.

* **Tittle:** `Available CryptoCurrencies`
* **Subtitle:** `Choose one crypto to convert`

Next, explain to student that each option will appear as a button on the card, so a tittle should be defined for each one together with a value; the value is taken from the values defined when the custom slot type is created. In this demo you will see three possible values on the _Button value_ dropdown list as it's shown bellow. Once you finish, click on the _Save_ button con continue.

![Card slot values](Images/card-slot-values.png)

Click on the _Build_ button, once the build process is done, test your bot on the _Test bot_ window, show to students how the card's options are presented and click on `Ethereum`; as you can see bellow something strange is happening, despite we selected `Ethererum` the bot is converting to `Bitcoin`.

![Sample card slot demo](Images/custo_slots_cards.gif)

**What is happening?** Explain students that the bot dialog and elicitation process is working perfectly, however, we have to modify the Lambda function to allow the bot to make to correct conversion. This is going to be done in the next activity.

Answer any pending question before continue.
