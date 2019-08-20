### 2. Instructor Do: Intro to Amazon Lex (10 mins)

In this activity, students will be introduced to Amazon Lex; they will learn how to create a bot using the Amazon Lex console that returns parameters to the client by configuring a single intent, some slots and a confirmation prompt.

**Files:**

* [Lesson 13.3 Slides](#)

* [Share_The_Bill Bot](Activities/02-Ins_Intro_Lex/Solved/Share_The_Bill_1_d57679ca-cc90-4b74-9a61-2211a93f7208_Bot_LEX_V1.zip)

* [ShareBill Intent](Activities/02-Ins_Intro_Lex/Solved/ShareBill_6_6f154262-76b0-465f-aed1-ce1f3914c492_Intent_LEX_V1.zip)

Start this activity by opening the [lesson slides](#), navigate to the _Intro to Lex_ section and highlight the following:

* Amazon Lex is an AWS service that allows developers to create conversational interfaces powered by the same deep learning technologies as Alexa.

* Getting started with Amazon Lex is quite easy, it's just a four step process.

* All the complexity of deep learning algorithms is encapsulated, no coding is needed to start using it.

Introduce the Amazon Lex jargon to students using a day-to-day example like booking a hotel room; comment to students that they will gain hands-on experience with these concepts in Today's class.

Clarify to students the AWS regions where Amazon Lex is available, pricing varies among regions. We will use `US West (Oregon)` for running the examples.

Slack out the [Amazon Lex Pricing policies](https://aws.amazon.com/lex/pricing/), remind students that from the date they get started with Amazon Lex, they can process up to 10,000 text requests and 5,000 speech requests per month for free for the first year. **Note:** This is subject to change, so they should verify the pricing structure using the link above.

Close the presentation and open the AWS Management Console, explain students that now you will create an Amazon Lex bot that will assist users to split a bill between a given number of people.

Follow the next steps to perform a live demo.

* **Step 1:** Login into the AWS Management Console using your IAM Admin user and URL.

  ![Step 1](Images/lex-step1.png)

* **Step 2:** Select `US West (Oregon)` as the AWS region for this demo.

  ![Step 2](Images/lex-step2.png)

* **Step 3:** On the _Find Services_ search box, type `Lex` and select the `Amazon Lex` service from the list.

  ![Step 3](Images/lex-step3.png)

* **Step 4:** If this is the fist time you use Amazon Lex, you will see the following page to get started with your first bot.

  ![Step 4a](Images/lex-step4a.png)

  If you have already created a bot, you will be led to the following page instead where you can see a list with your current bots.

  ![Step 4b](Images/lex-step4b.png)

* **Step 5:** To create a new bot, click on the _Custom bot_ option and fill-out the following, next click the `Create` button to continue:

  * _Bot name:_ Share_The_Bill
  * _Output voice:_ Mathew
  * _Session timeout:_ 5 min
  * _COPPA:_ Select `No`

  ![Step 5](Images/lex-step5.png)

* **Step 6:** Now you will create an intent to respond to user's actions. Click on the _Create Intent_ button and you will see the a pup-up window entitled _Add intent_ as you can see bellow. Click on the _Create intent_ option to continue.

  ![Step 6](Images/lex-step6.png)

* **Step 7:** In this step you should give a name to the intent, explain students that normally intents are named as actions to be performed by the bot; type `ShareBill` and click on the _Add_ button to continue.

  ![Step 7](Images/lex-step7.png)

* **Step 8:** In this step, you will configure the intent to allow the bot to interact with the user. Start by adding the following sample utterances:

  * `We want to split the bill`
  * `Please help me to share the bill`
  * `I want to share the bill with my friends`

  At this point, explain to student that these sample utterances will be used by the deep learning algorithm of Amazon Lex to understand the context of the conversation, the more different sample utterances you add, the best the conversation will flow between the bot and the user.

  ![Step 8](Images/lex-step8.png)

  Add two slots as follows:

  | Name         | Slot type     | Prompt                                                   |
  | ------------ | ------------- | -------------------------------------------------------- |
  | totalAmount  | AMAZON.NUMBER | I'll be please to help, what is the bill's total amount? |
  | numberPeople | AMAZON.NUMBER | How many people is going to pay the bill?                |

  On the _Confirmation prompt_ section, enable the confirmation prompt and type the following confirm and cancel prompts:

  * _Confirm prompt:_ `Are you sure you want to split a bill for ${totalAmount} between {numberPeople} people?`
  * _Cancel prompt:_ `Okay, let's start again.`

  Explain students that in the confirm prompt, `{totalAmount}` and `{numberPeople}` are a kind of variables that will be filled out with the values given by the user.

* **Step 9:** Now it's time to see the bot in action, build your bot by clicking on the _Build_ button and confirming the build option on the pop-up window.

  ![Step 9a](Images/lex-step9a.png)

  The building process takes a couple of minutes, once the process finished, you will see the following confirmation message and the _Test bot_ window will appear. You can now close the confirmation message and test your bot.

  ![Step 9b](Images/lex-step9b.png)

* **Step 10:**  Test your boot using the first sample utterance, you should have a dialog with the bot as follows.

  ![Step 10](Images/lex-step10.gif)

  Explain to students that at this time the bot has no business rules logic attached, that's why the final message the bot sends after fulfilling all the slots is a kind of non-friendly confirmation message. We will improve this by adding an Amazon Lambda function to the bot.

  ![Fulfillment message](Images/lex-step10msg.png)

Answer any pending questions before continue.
