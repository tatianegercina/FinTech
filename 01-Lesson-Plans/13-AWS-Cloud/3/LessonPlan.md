## 13.3 Lesson Plan - Amazon Lex and Robo-advisors

### Overview

In today's class, students will be introduced to conversational user interfaces (CUIs) and learn how they are disrupting the FinTech industry, especially in finance and banking. Students will also create a robo-advisor using Amazon Lex and Amazon Lambda.

### Class Objectives

By the end of the class, students will be able to:

* Explain what conversational interfaces are, and their general applications in FinTech.

* Describe the specific applications of conversational interfaces for finance and banking.

* Recognize how machine learning and natural language processing contribute to creating conversational interfaces.

* Create conversational interfaces using Amazon Lex.

* Apply their Python skills to add new features to an Amazon Lex bot using Amazon Lambda.

### Instructor Notes

* Slack out the [Deep Learning Installation Guide](../../14-Deep-Learning/Supplemental/deep_learning_installation_guide.md). Tell students to complete the installation and verify it with a TA before the end of the next class. Students will need this installed before the next unit.

* There are several misconceptions and myths about what can be achieved with a robo-advisor. Make sure that students understand what a robo-advisor is, and invite them to think about the endless possibilities of this technology for FinTech.

* Today's class may be challenging for students because they are going to deal with different AWS services, so be sure to get familiar with all the activities before class.

* Amazon Lambda functions will be created and edited using the online code editor. This editor sometimes has issues or freezes up, so tell students to back up their code with a local Python script.

* Testing Amazon Lambda functions can be tricky and frustrating, so have your TAs assisting students while they are coding and testing them.

* **Important:** At the end of today´s class, have students create a local copy of all their deployments on AWS, so they can delete them from the cloud to avoid additional charges. Also, remind students to be aware of the AWS free tier and trial expiration date.

### Sample Class Video (Highly Recommended)

* To watch an example class lecture, go here: [13.3 Class Video.](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0f288da5-fe69-4899-b21d-aaf1013917e1) Note that this video may not reflect the most recent lesson plan.

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 13.3 Slides](https://docs.google.com/presentation/d/1GTrVc7OrtTQC43RCUSf8YFbV6I8S7ZcAnZeIdZh95Bc/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (10 min)

In this activity, students will be introduced to conversational user interfaces (CUIs). They will learn how CUIs are disrupting financial services and what tools they need to use to create a robo-advisor.

Welcome students to Day 3! Explain that today we will learn about conversational user interfaces, one of the most refreshing applications of natural language processing. Tell students that they will create a robo-advisor with conversational capabilities by the end of the day.

Open the lesson slides and move to the "Conversational User Interfaces (CUIs) and Robo Advisors_ section, highlighting the following:

* In the early years of computing history, people used to communicate with computers using text interfaces and some non-human-friendly commands.

* Thanks to AI, and especially to the advances in natural language processing (NLP), we can communicate with computer systems using human language through conversational user interfaces via voice or text.

* Chatbots are the most common applications of CUIs; however, Amazon Alexa, Apple Siri, or Google Assistant are also examples of CUIs.

* CUIs and robo-advisors enhance customer engagement by using digital communication channels (social media or messaging apps).

Point out to students that this technology has been disruptive in finance and banking via robo-advisors, which are used as an additional communication channel for customers.

Highlight the following about chatbots in finance and banking:

* According to Juniper Research, banks will save about $8 billion USD annually by 2020, thanks to chatbot use.

* Chatbots can improve customer experience by performing tasks 24/7. Customers don't need to wait for human replies for most common tasks or inquiries.

* Using NLP and sentiment analysis, chatbots understand how people speak, allowing financial institutions to respond more appropriately to customers' needs.

Now show students the "Chatbots Use Cases" section. As you present these, engage students by asking who is familiar with these types of services and what their experiences were like.

Highlight the following about chatbots use cases:

* The first robo-advisors were introduced in the Canadian FinTech industry in 2014.

* Financial assets management aided by robo-advisors are expected to show an annual growth rate of 26.7% from 2020 to 2023; with a forecast of $23.5M CAD by 2023.

* Depending on how a robo-advisor operates (e.g., as a portfolio manager or investment advisor), one must register with the Investment Industry Regulatory Organization of Canada (IIROC) and follow suitability obligations, like disclosing investing risks to their clients.

* Wealthsimple.

  * It is rated by several analysts as the best robo-advisor in the Canadian market.

  * Founded in 2014 in Toronto, it's an online investment management service focused on millennials. As of August 2019, the firm holds over $5 billion CAD in assets under management.

* Nest Wealth.

  * The firm created Canada’s first SaaS-based digital wealth management platform to allow investors access to personalized and transparent wealth management services.

  * Based in Toronto, it was founded in 2014.

* Bolt from the Bank of Montreal (BMO).

  * BMO launched Bolt in 2018 to allow customers to contact the bank via Facebook or Twitter for inquiries about products, foreign exchange rates, as well as branch locations and ATMs, 24×7.

* Erica from Bank of America.

  * This was launched in 2018 to offer customers a digital banking experience that encompassed voice, in-app messaging and predictive analytics.

  * By December 2019, Erica reached more than 10 million users.

Continue the presentation by introducing the technologies we will use today, making sure to highlight the following:

* By the end of today's class, we will create a robo-advisor using two services in AWS.

* Amazon Lex is a service using the same technology behind Amazon Alexa; it's useful for building conversational interfaces into any application using voice and text.

* AWS Lambda is a computing service that runs code in response to events. We will use this service to program the actions of the robo-advisor.

* To interact with final users, a bot created with Amazon Lex can be deployed on a mobile application or a messaging platform such as Slack, Kik, or Facebook Messenger.

Slack out [this article from Deloitte](../Supplemental/deloitte-nl-fsi-chatbots-adopting-the-power-of-conversational-ux.pdf) where they can learn more about the impact of chatbots in financial services.

Answer any additional questions before moving forward.

---

### 2. Everyone Do: Creating Your First Bot Using Amazon Lex (30 min)

In this activity, students will learn how to create a bot using the Amazon Lex console that returns parameters to the client by configuring a single intent, some slots, and a confirmation prompt.

**Files:**

* [Crypto_Converter Bot](Activities/01-Evr_Intro_Lex/Solved/Crypto_Converter_1_a363e85f-1be3-4c14-a3d4-b0814792e3f7_Bot_LEX_V1.zip)

Start this activity by opening the slides to the "Intro to Amazon Lex" section and highlight the following:

* Amazon Lex is an AWS service that allows developers to create conversational interfaces powered by the same deep learning technologies like Alexa.

* It uses automatic speech recognition to convert speech to text, and natural language understanding to recognize the intent of the text.

* It encapsulates all the complexity of deep learning algorithms; no coding is needed to start using it.

* It allows integration with third-party applications, AWS services, and your code via AWS Lambda.

* Getting started with Amazon Lex is quite easy–it is just a four-step process.

  1. Create a bot and configure it to understand the user's goals/intent.

  2. Test the bot on the Amazon Lex console. Make sure it engages in conversation with the user.

  3. Publish the bot and create an alias.

  4. Deploy the bot on a mobile application or a messaging platform such as Slack, Kik, or Facebook Messenger.

Introduce the Amazon Lex jargon to students, and reassure them that they will gain hands-on experience with these concepts in today's class.

* **Bot:** This is the core component of Amazon Lex. A bot performs automated tasks such as booking a hotel, making a wire transfer, or suggesting an investment portfolio.

* **Intent:** Represents an action that the user wants to perform, such as BookHotel, TransferMoney, or SuggestPortfolio. A bot can have more than one intent.

* **Utterances:** Speech or text phrases that trigger the intent. They refer to the dialogue between the user and the bot.

* **Slots:** A piece of data that is necessary for the chatbot to fulfill the user’s intent. Think of it as required user input.

* **Fulfillment:** When the chatbot has collected all the slot values, it proceeds with the logic in the fulfillment section. This is where an AWS lambda function can be used if you need some business logic.

Clarify to students that Amazon Lex is available only in a few AWS regions (Oregon, N. Virginia, Ireland, and Sidney), and pricing varies among regions.

For the latest list of the supported Amazon Lex AWS regions, slack out to students [the link of the AWS Region Table for all AWS global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). We will use `US West (Oregon)` for running the examples.

Slack out the [Amazon Lex Pricing policies](https://aws.amazon.com/lex/pricing/), remind students that from the date they get started with Amazon Lex, they can process up to 10,000 text requests and 5,000 speech requests per month for free for the first year. **Note:** This is subject to change, so they should verify the pricing structure using the link above.

Close the presentation and log in to the AWS Management Console using your `administrator` IAM user. Explain to students that you will now create an Amazon Lex bot together, to assist users in converting dollars to bitcoin.

Ask students to log in as well with their `administrator` IAM users. Once everyone is ready, ask them to follow along as you perform the live demo. Highlight the following:

* From the AWS Management Console, select `US West (Oregon)` AWS region for this demo.

  ![Switching to the US West AWS Region](Images/amazon-lex-choose-region.png)

* On the "Find Services" search box, type `lex` and select the `Amazon Lex` service from the list.

  ![Launching Amazon Lex](Images/amazon-lex-search-service.png)

* You will now see the following page to get started with your first bot. Click on the "Get Started" button to continue.

  ![Get started page of Amazon Lex](Images/amazon-lex-get-started-page.png)

**Important Note:** If you created a bot before, you would be led to the following page instead, where you can see a list with your current bots.

  ![Step 4b](Images/lex-step4b.png)

* Choose the "Custom bot" option and fill in the following:

  * _Bot name:_ `Crypto_Converter`
  * _Output voice:_ Salli
  * _Session timeout:_ 5 min
  * _Sentiment analysis_: `No`
  * _IAM role:_ Leave the default value.
  * _COPPA:_ Select `No`
  * _Advanced options:_ Select `No`

  ![Setting the initial Amazon Lex's bot configurations](Images/amazon-lex-setting-initial-conf.png)

Explain to students that late in 2019, Amazon Web Services added the "sentiment analysis" feature to Amazon Lex. This feature allows scoring the sentiment of users' utterances using another service called [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) that applies additional charges. We are not going to use this feature in today's class, but slack out [the sentiment analysis documentation](https://docs.aws.amazon.com/lex/latest/dg/sentiment-analysis.html) to students for further research.

Highlight to students that we will set the "Advanced option" parameter to `No` for information privacy concerns. If we select `Yes`, we will send the dialogs as training data to improve AWS algorithms. Before selecting `Yes`, it's recommendable to review the company's information privacy policies or customer where we plan to deploy a chatbot using Amazon Lex.

Explain that Amazon Lex is only available in US English now, so there are some considerations to make (which will be covered later in more depth).

Once you configure the bot, click the "Create" button to continue:

![Creating an Amazon Lex bot](Images/amazon-lex-create-bot.png)

* Now, we will create an intent to respond to the user's actions. Click the "Create Intent" button. You will see a pop-up window entitled "Add intent." Click on the "Create intent" option to continue.

  ![Adding an intent](Images/amazon-lex-add-intent.gif)

* In this window, you should give a name to the intent. Usually, intents are named as actions to be performed by the bot. Type `convertCAD`, and click on the "Add" button to continue.

  ![Naming the intent](Images/amazon-lex-name-intent.png)

* Now, we need to configure the intent to allow the bot to interact with the user via natural language.

* To allow the bot to interact with a user, we need to provide some starting context about the conversation that the bot can conduct. We provide this context using sample utterances.

* Sample utterances are phrases that a user can use to start a conversation with the bot.

* These sample utterances will be used by the deep learning algorithm of Amazon Lex to understand the context of the conversation. The more different sample utterances are added, the better the conversation will flow between the bot and the user. We will start by adding the following sample utterances:

  * `I want to convert CAD to BTC`
  * `I want to convert dollars to BTC`
  * `I want to convert dollars to bitcoin`

  ![Adding sample utterances](Images/amazon-lex-add-utterances.png)

* Once we define the sample utterances, we need to determine the possible questions or dialogue that the bot can conduct to gather information from the user.

* In this demo, we want to convert dollars to bitcoin, so we need some way to allow the bot to ask how many dollars the user wants to convert to bitcoin.

* We fetch data from the user and allow the bot to ask a question using "slots".

* Slots are like variables in a Python script; you need to define a name to the slot, a data type (that is known as "slot type" in the context of Amazon Lex), and a prompt. A prompt is a question or phrase the bot is going to use to fetch the data to fulfill a slot.

Continue the demo by adding the following two slots:

  | Name      | Slot type     | Prompt                                                                                                  |
  | --------- | ------------- | ------------------------------------------------------------------------------------------------------- |
  | birthday  | AMAZON.DATE   | This service can only be used by people over 18 years old, could you please give me your date of birth? |
  | cadAmount | AMAZON.NUMBER | How many dollars do you want to convert?                                                                |

* To add a slot, scroll down to the "Slots" section. Start by typing the name of the slot in the "Name" box.

  ![Adding the name of a slot](Images/amazon-lex-add-slot-name.png)

* Next, you need to define the "Slot type." Slot types are similar to data types in programming languages, since they define the kind of data that you can fetch and save in the slot. Amazon Lex provides several built-in slot types for the most common types of data that may be fetched in a conversation.

  ![Choosing a slot type](Images/amazon-lex-choosing-slot-type.gif)

* To finish the slot configuration, you need to add the prompt in the "Prompt" box.

  ![Setting the prompt in a slot](Images/amazon-lex-define-slot-prompt.png)

* After adding the two slots, be sure that the "Required" option is checked for both slots.

  ![Checking required slots](Images/amazon-lex-required-slots.png)

Explain to students that the final step is to define how the bot should respond when it successfully fulfills all the slots, as well as how to respond if the user wants to cancel the intent action. This is done in the "Confirmation prompt" section.

Scroll down to the "Confirmation prompt" section, check the "Confirmation prompt" option, and type the following confirm and cancel prompts:

* _Confirm prompt:_ `Are you sure you want to convert ${cadAmount} to Bitcoin?`

* _Cancel prompt:_ `Okay, let's start again.`

![Setting confirmation prompts](Images/amazon-lex-confirmation-prompt.png)

Explain to students that in the confirm prompt, `{cadAmount}` is a kind of variable that will be filled out with the value given by the user.

You have defined all the configurations needed to test your bot. Ensure that all students have reached this point before continuing. Highlight the following:

* Now, it's time to see the bot in action! First, you need to build your bot by clicking on the "Build" button at the upper right corner and confirming the build option on the pop-up window.

  ![Building the bot for testing](Images/amazon-lex-build-bot.gif)

* The building process takes a couple of minutes. Once that's finished, you will see a confirmation message, and the "Test bot" window will appear.

  ![Bot building confirmation](Images/amazon-lex-bot-build-success.png)

* To test your bot, you can close the confirmation message. Start testing your bot using the first sample utterance.

  ![Testing the Amazon Lex bot](Images/amazon-lex-testing-bot.gif)

* When the bot is tested, the date of birth can be given in any format (e.g., `12/16/1978`, `16/12/1978`, `Dec 16, 1978`). Using the `AMAZON.DATE` slot type will transform the date automatically to the `YYYY-mm-dd` format, as can be seen on the demo gif file below.

* Be aware that currently, Amazon Lex only supports US English. Hence, date transformations for birthdays like June 5, 1980, typed in a numerical format like 5/6/78, as in Canadian English or Spanish, will be transformed to `1980-05-06` (May 6, 1980).

Explain to students that at this time, the bot has no business rules logic attached. This is why the final message the bot sends after fulfilling all the slots is a somewhat impersonal confirmation message. We will improve this by adding an Amazon Lambda function to the bot later today.

![Fulfillment message](Images/amazon-lex-fulfillment-message.png)

Ensure that all students have successfully tested their bot, then answer any pending questions before continuing with the next activity.

---

### 3. Instructor Do: Intro to AWS Lambda (15 min)

This activity will introduce AWS Lambda to students. Also, students will learn how they can integrate Lambda functions into an Amazon Lex bot. The full code of the lambda function can be found in the "Solved" directory.

**Files:**

* [lambda_function.py](Activities/02-Ins_Intro_Lambda/Solved/lambda_function.py)

Start the activity by opening the lesson slides, navigate to the "Intro to AWS Lambda" section, and highlight the following:

* Sometimes AWS Lambda is seen as a web service or an API since it runs code remotely. However, AWS Lambda is a serverless technology where you just upload your code and Lambda takes care of everything.

* In general terms, _serverless_ means that you do not have to be worried about any server configuration or administration.

* AWS Lambda can have your code automatically trigger from other AWS services or call it directly from any web or mobile app.

Continue with the lesson slides, and [open the video "Intro to AWS Lambda"](https://youtu.be/eOBq__h4OJ4) for a three-minute video introduction to illustrate how AWS Lambda works.

When the video ends, continue with the slides. Explain that we are going to use AWS Lambda by triggering code from an Amazon Lex Bot. Highlight the following:

* AWS Lambda enhances chatbots by combining the NLP capabilities of Amazon Lex to understand human speech, with the possibility of running code to fulfill user's requests. Examples could be booking a hotel room, making a wire transfer, or providing financial advice about an investment portfolio.

* AWS Lambda interacts with other AWS services by processing events messages in `JSON`. Each Amazon Web Service has a specific format.

* Amazon Lex "talks" to AWS Lambda to perform initialization and validation, fulfillment, or both.

Explain to students that in this demo, you will show how to process `ElicitSlots`, `Delegate`, and `Close` response events to communicate Amazon Lex and AWS Lambda.

Close the slides and log in into the AWS Management Console using your IAM `administrator` user, once you are logged in, type `lambda` into the "Find Services" search box, and click on choose "Lambda" from the list to open the AWS Lambda console.

![Search for AWS Lambda service on the AWS Management console](Images/search-lambda-service.png)

In the AWS Lambda console, click on "Functions" on the left side menu; continue by clicking on the "Create function" button.

![AWS Lambda console](Images/aws-lambda-console.png)

On the "Create function" page, select the "Author from scratch" option, fill out the following information, and click on the "Create function" button to continue:

* **Function name:** `convertCAD` (This is the name to identify our new Lambda function)

* **Runtime:** `Python 3.7`

**Note:** Though AWS Lambda offers support for Python 3.8, be sure to choose version 3.7 as the runtime to avoid version conflicts with the code in today's lesson.

![Create function page](Images/aws-lambda-create-function.png)

Explain to students that now AWS will create the `convertCAD` Lambda function environment by provisioning the infrastructure needed to run a serverless application; this process takes a few seconds.

Once the Lambda function is created, you will see the following page.

![convertCAD function created](Images/convertCAD-created.png)

Scroll down to the "Function code" section and explain to students that this code is a starter `Hello World` example. Highlight that a lambda function has a main events handler; its goal is to manage all the incoming messages and dispatch them depending on the business logic defined.

* We will use the `lambda_handler` function to route the incoming requests based on the user's intents captured by the Amazon Lex bot.

![Function code section](Images/convertCAD-function-code.png)

Open the slides and show students the anatomy of the lambda function you are going to use. Let the students know that this code can be used as a boilerplate template to code business logic to extend Amazon Lex bots functionality.

![Lambda function anatomy](Images/lambda-function-anatomy.png)

Explain to students that the lambda function contains six general building blocks; present these blocks by highlighting the following:

1. **Required Libraries:** This section contains all the necessary libraries to code the business logic on the lambda functions. Although AWS Lambda supports Python, the AWS Lambda's runtime doesn't support some common packages, such as `pandas`, `numpy` or `requests`, so alternative packages should be used or installed.

    In this demo, we take the current price of bitcoin, making an API call to the [alternative.me Crypto API](https://alternative.me/crypto/api/), so the `requests` library is imported from the [`botocore` package](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html). A complete list of the python modules available on AWS Lambda can be found [here](https://gist.github.com/gene1wood/4a052f39490fae00e0c3).

2. **Functionality Helper Functions:** These functions implement business logic and data validation. In this demo, we have four helper functions.

    * `parse_float()`: This function securely parses a non-numeric value to float.

    * `get_btcprice()`: Retrieves the current price of bitcoin in dollars from the alternative.me Crypto API.

    * `build_validation_result()`: This function defines an internal validation message structured as a Python dictionary.

    * `validate_data()`: This function validates the data provided by the user across the intent's dialogue on Amazon Lex according to the business logic. In this demo, there are only two rules: (1) the user should be at least 18 years old (2) the amount in dollars to convert must be greater than zero.

    Explain to students that the `validate_data()` function uses the `build_validation_result()` function to return a validation result message. In this demo, if the user's age is less than `18` or the amount to convert is less than `0`, a `False` result is returned; otherwise, a `True` result is returned.

3. **Dialog Actions Helper Functions:** These functions handle the input and response events data from the conversation between Amazon Lex and AWS Lambda. The `get_slots()` function fetches all the slots and their values from the current intent. The `elicit_slot()`, `delegate()` and `close()` functions, construct response messages structured as a valid JSON Lex event. The full structure of event data that Amazon Lex exchanges with a Lambda function can be reviewed [here](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html).

4. **Intents Handlers:** The core business logic is coded into an intent handler. An intent handler is a function that implements the functionality that is willing to fulfill the user's intent.

    Explain to students that in this demo, the `convert_cad()` function contains all the logic to validate the user's input stored in the `slots` using the `validate_data()` helper function; along with the conversation between the user and the bot, if any of the `slots` have invalid data, an `elicitSlot` dialogue is returned to request the data again to the user, otherwise a `delegate()` dialogue is returned to direct Lex to choose the next course of action according to the bot's configuration.

    Highlight to students that once the conversation between the user and the bot ends, the current price of bitcoin in dollars is fetched using the `get_btcprice()` function, the conversion from dollars to bitcoin is done, and the `close()` dialogue function is called to return a `Fulfilled` event message to Lex.

5. **Intents Dispatcher:** An Amazon Lex bot can have one or more intents. The purpose of the `dispatch()` function is to validate that the current intent is valid, and to dispatch the intent to the corresponding intent handler. In this demo, we only have one intent, so we only have one intent handler call to the `convert_cad()` function.

6. **Main Handler:** Every time a user sends a message to Amazon Lex, using text or voice, an event will be sent to AWS Lambda; the `lambda_handler()` function catches every event and returns a response to Lex via the `dispatch()` function.

After presenting the Lambda function's building blocks, open the `lambda_function.py` script on VSCode, delete the sample code, and copy and paste the code from VSCode to the code editor on the AWS Lambda console. Click the "Save" button to continue.

![Sample copied Lambda code](Images/copied-lambda-code.png)

The next step is to communicate Amazon Lex with the Amazon Lambda function. Open the Amazon Lex console and open the `Crypto_Converter` bot.

![Opening the Amazon Lex console from the AWS Lambda console](Images/open-lex-from-lambda.gif)

Scroll down to the "Lambda initialization and validation" section, enable the _Initialization and validation code hook_ option and select the `convertCAD` Lambda from the list. Be sure to select the `Latest` version.

A pop-window asking you for permissions to your Lambda Function may appear; click the "OK" button to continue. Explain to students that this permission is needed to allow communication between the bot and Lambda.

![Configure the Lambda initializations and validation](Images/initializing-lambda-in-lex.gif)

Scroll down to the "Confirmation prompt" section and disable the checkbox. Continue by opening the "Fulfillment" section and choose the "AWS Lambda function" option. Select the `convertCAD` Lambda and the `Latest` version.

Click on the "Build" button on the upper right corner. Now the bot is connected to Lambda to control the user's intent.

![Confirmation and fulfillment configuration](Images/lambda-confirmation-fulfillment.png)

Test the Lambda powered bot with some of the sample utterances; you should have a final conversation as it is shown below.

| _Bot demo conversation with valid user's data_ | _Bot demo conversation with invalid user's data_ |
| --- | ---|
| ![Converter without errors](Images/converter_ok.gif) | ![Converter with errors](Images/converter_errors.gif) |

Congratulations! You have created your first bot assisted by AWS Lambda. Answer any pending questions from the class before moving forward.

---

### 4. Student Do: Understanding Lambdas (15 min)

In this activity, students will inspect the code of a Lambda function to have a better understanding of how it works. Students will create their Lambda function by importing the provided code and will build a new version of their bot. Be sure to slack out the `lambda_function.py` code to students before starting the activity.

**Instructions:**

* [README.md](Activities/03-Stu_Understanding_Lambdas/README.md)

**Files:**

* [lambda_function.py](Activities/03-Stu_Understanding_Lambdas/Solved/lambda_function.py)

---

### 5. Instructor Do: Review Understanding Lambdas (10 min)

**Files:**

* [lambda_function.py](Activities/03-Stu_Understanding_Lambdas/Solved/lambda_function.py)

Open the Lambda function code in VSCode, and then conduct a facilitated discussion by asking students about their findings, insights, or additional questions after reviewing the provided code. Consider starting with the following questions:

* Does anyone have a different idea on how to organize the function's _building blocks_?

  **Sample Answer:** Maybe we can omit the `parse_float()`, `get_btcprice()` and `validate_data()` helper functions and embed all the functionality on the `convert_cad()` intent handler function.

  **Sample Answer:** We can drop the `dispatch()` function by adding the intents' name validation into the `lambda_handler()` function.

* Do you think we can avoid using the `parse_float()` function?

  **Sample Answer:** Yes, but we can only do that by using the `float()` function.

  **Sample Answer:** Yes, we can avoid defining the `parse_float()` function and use the `float()` function instead. Having this function return the value of `nan` for non-numeric values is more secure and eases testing.

* Is there any other way to define the dialogue helper functions?

  **Sample Answer:** We could define a function that receives all the data from the current intent and have some nested `if` controlling the kind of dialogue and response.

  **Sample Answer:** I think this is a very efficient way to handle the different dialogue types.

Slack out the following resources and encourage students to learn more about AWS Lambda and Lex.

* [Lambda Function Input Event and Response Format](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html#using-lambda-input-event-format)

* [Amazon Lex and AWS Lambda Blueprints](https://docs.aws.amazon.com/lex/latest/dg/lex-lambda-blueprints.html)

Answer any remaining questions, and move to the next activity.

---

### 6. Instructor Do: Testing AWS Lambda Functions (15 min)

In this activity, students will learn how to test AWS Lambda functions that validate Amazon Lex intents.

**Files:**

* [convertOkText.json](Activities/04-Ins_Testing_Lambdas/Solved/convertOkText.json)

* [convertErrAmount.json](Activities/04-Ins_Testing_Lambdas/Solved/convertErrAmount.json)

* [convertErrDate.json](Activities/04-Ins_Testing_Lambdas/Solved/convertErrDate.json)

Explain to students that one of the challenges of working with AWS Lambda is dealing with errors, so it is essential to know how to test a Lambda function on the AWS Lambda console. For this activity, three test cases are provided.

Explain to students that Lambda functions are tested using a `JSON` file to send a testing event to Lambda; the structure of the event depends on the kind of service you are connecting to Lambda. This demo will only cover how to test Amazon Lex intents.

Open the `convertCAD` lambda function on the AWS Lambda console to show students how to create a test case. Click on the "Test" button on the upper right corner, then choose the "Create new test event" option.

![Creating a test case](Images/amazon-lambda-create-test.gif)

You will note that there is a `Hello World` test case. Explain to students that this is a general test case. Testing Lambda functions connected with Amazon Lex require a particular format.

Delete the starter test case code from the "Configure test event" window, then open the `convertOkText.json` in VSCode and copy and paste the code in the "Configure test event" window.

```json
{
  "messageVersion": "1.0",
  "invocationSource": "DialogCodeHook",
  "userId": "John",
  "sessionAttributes": {},
  "bot": {
    "name": "Crypto_Converter",
    "alias": "$LATEST",
    "version": "$LATEST"
  },
  "outputDialogMode": "Text",
  "currentIntent": {
    "name": "convertCAD",
    "slots": {
      "birthday": "1978-12-16",
      "cadAmount": "10"
    },
    "confirmationStatus": "None"
  }
}
```

After pasting the test case code, type `convertOkText` in the "Event name" box and highlight the following about the test event code:

![Creating a new test event](Images/lambda-text-case.png)

* On the `bot` key, the name of the Amazon Lex bot is defined, so you should be sure that this name matches with your bot's name.

* The `$LATEST` is the default value to use for the `alias` and the `version` keys.

* Since this test event is passed as text, the value of the `outputDialogMode` key is `text`.

* Under the `currentIntent` key, the values of the bot's slots are given. You should be aware that those names match with your slots names.

* This is a test event where the `birthday` and `cadAmount` slots have valid data.

Click the "Create" button to continue.

Tell students that the name of the new test case now appears on the dropdown list, next to the "Test" button. Click the "Test" button, and you will see the test results on the window below the Lambda function code.

![Test results](Images/lambda-test-ok.png)

Since this test case has valid data for both slots, explain to students that the test status is `Succeeded`, and the execution results show a response with both slots fulfilled with the data passed on the test case.

Now show students how to add a new test case. Click on the test events dropdown list and choose the "Configure test events" option.

![Add new test event](Images/lambda-add-new-test-event.png)

By default, you will see that the last used test case is selected. Notice that the "Edit saved test events" option is chosen so that you can edit the test event.

![Edit saved test event](Images/lambda-add-new-test-default-selection.png)

Choose the "Create new test event" option, and you will notice that the previous test event remains as a template. Change the value of the `cadAmount` slot to zero, to test the amount validation coded on the Lambda and name the new event as `convertErrAmount`. Click on the "Create" button to continue.

![Create a new test event to cast amount value](Images/lambda-add-convertErrAmount.png)

Select the `convertErrAmount` test on the "Test events" dropdown list, and click the "Test" button.

Explain to students that the test ran successfully again. However, now Lambda responds with an `ElicitSlot` type of dialogue where the message defined on the Lambda can be read. This test event is validating that the code catches the incorrect value at the Lambda, and the appropriate new data elicitation is sent to the user via Amazon Lex.

![Running the convertErrAmount test event](Images/lambda-testing-convertErrAmount.png)

Create a final test event, but now to validate what happens when the user gives an invalid date of birth. Repeat the same process described before to create a new test event. Introduce `2014-12-16` on the `birthday` slot and name the test event as `convertErrDate`.

![Adding the convertErrDate test event](Images/lambda-add-convertErrDate.png)

Execute the `convertErrDate` test, and tell students that the date validation was successfully run, since the `ElicitSlot` dialogue type is returned together with the message asking for a different date of birth.

![Test results from convertErrDate](Images/lambda-testing-results-convertErrDate.png)

Close the execution results window. You will now introduce a typo on the code to raise a runtime error. On the `parse_float()` function, delete the closing parenthesis on line 12. Click the "Save" button and run any of the testing events.

![Provoking a runtime error](Images/lambda-provoking-runtime-error.png)

After running the test event, explain to students that the test status is `Failed` and that the response contains the error description and the line where the error was detected.

![Runtime error](Images/lambda-runtime-error.png)

Comment to the students that these types of errors are difficult to catch on Amazon Lex. That is why it is crucial to test Lambdas on the AWS Lambda console before linking the Lambda to the Amazon Lex bot.

Answer any remaining questions and continue to the next activity.

---

### 7. Student Do: Buggy Lambdas (15 min)

In this activity, students will test their Lambda functions and practice their ability to find runtime errors. Slack out the instructions to students along with the starter test event.

**Instructions:**

* [README.md](Activities/05-Stu_Buggy_Lambdas/README.md)

**Files:**

* [convertOkTest.json](Activities/05-Stu_Buggy_Lambdas/Unsolved/convertOkTest.json)

---

### 8. Instructor Do: Review Buggy Lambdas (10 min)

**Files:**

* [convertOkText.json](Activities/05-Stu_Buggy_Lambdas/Solved/convertOkText.json)

* [convertErrNegAmount.json](Activities/05-Stu_Buggy_Lambdas/Solved/convertErrNegAmount.json)

* [convertOldAge.json](Activities/05-Stu_Buggy_Lambdas/Solved/convertOldAge.json)

Start the review activity by adding the `convertErrNegAmount` and `convertOldAge` test events to your `convertCAD` Lambda. Run both tests, and highlight the following:

* The `convertErrNegAmount` behaviour is the same as the case when a zero is passed, an `ElicitSlot` type is returned, asking the user for an amount greater than zero.

* The `convertOldAge` text case runs as a correct test event, there is no further validation to prevent a very old person from using the bot.

Open a facilitated discussion with the students by asking the following question:

* How can you prevent a possible fake date of birth from being given to the bot?

  **Sample Answer:** Let us suppose that if a person's average life expectancy is 85 years old, we can supplement an additional condition to validate that the age is between 18 and 85 years.

  **Sample Answer:** We can unfairly discriminate an older person to use the service, so I would not be worried about this kind of validation.

Continue the discussion by asking for volunteers that want to share their experiences with finding the bugs that were planted by her or his partner.

* **Sample Answer:** It was frustrating since the error messages returned by Lambda were not clear.

* **Sample Answer:** It was fun being a bug detective.

* **Sample Answer:** It was an excellent opportunity to practice my debugging skills.

Close the discussion by answering any remaining questions before moving forward.

---

### 9. BREAK (40 min)

---

### 10. Instructor Do: Custom Slots (15 min)

In this activity, students will learn how to create a custom slot and add it to an Amazon Lex bot intent.

Comment to students that it is possible to create custom slot types. This is intended to gather specific data values for a slot; for example, the size of a pizza (personal, small, medium, or large) on a pizza ordering bot.

Explain to students that you will show them how to create a custom slot to allow users to choose the cryptocurrency they want to convert to.

Open the Amazon Lex console and navigate to the `convertCAD` intent editor. On the left side menu, click on the blue plus symbol next to the "Slot types" option to add a new custom slot type.

![Adding a new slot type](Images/add-slot-type.png)

Next, a pop-up window will appear. Click the "Create slot type" option to continue.

![Create a new slot type](Images/create-slot-type.png)

Configure the new slot type as follows:

* **Slot type name:** `CryptoCurrency`

* **Description:** `Available cryptocurrencies to convert.`

* **Slot Resolution:** Choose "Restrict to Slot values and Synonyms." By selecting this option, the user has to choose only among the available options.

* **Value:** Add three values and synonyms, one per each of the following cryptocurrencies.

  | Value | Synonym |
  |-------|---------|
  | Bitcoin | BTC |
  | Ethereum | ETH |
  | Ripple | XRP |

Once you are done, click on the "Add slot to intent" button.

![Configuring the new slot type](Images/configure-new-slot-type.png)

Back in the `convertCAD` intent editor, you will note that a new slot named `slotThree` was added with the `CryptoCurrency` slot type.

![The new slot three added](Images/new-slotThree-added.png)

Change the name of the `slotThree` to `crypto`, set the prompt as `What cryptocurrency do you want to convert to?` and be sure the "Required" checkbox is selected.

![Add the crypto slot](Images/add-crypto-slot.png)

Explain to students that the bot is now configured to elicit the `crypto` slot. However, we need to modify the utterances to add a better dialogue that includes the new slot.

Modify the utterances to have the following "Sample utterances":

* `I want to invest in cryptocurrencies`

* `I want to convert dollars to a cryptocurrency`

* `I want to buy {crypto}`

* `I want to convert CAD to {crypto}`

* `I want to convert dollars to {crypto}`

* `I want to convert {cadAmount} dollars to {crypto}`

![New sample utterances](Images/new-crypto-utterances.png)

Highlight to students that on the new utterances, the words `bitcoin` and `BTC` should be deleted with `{crypto}` typed instead, to allow users to specify on their dialogue what cryptocurrency they want to convert to. For example—by typing `I want to convert dollars to Ripple`, `Ripple` will be taken as the `crypto` slot.

Also, explain that students should not have repeated utterances, since an error will arise when they compile the bot.

Build the bot and test it on the "Test bot" window. Start with typing the sample utterance: `I want to invest in cryptocurrencies` to elicit all the slots as follows.

![Sample utterance 1](Images/custom_slots_1.gif)

Explain to students that when the `crypto` slot is elicited, only the three options will be valid. However, giving the user the chance to type any cryptocurrency name could be prone to errors, which is why using "Card Slots" could be useful.

To create a "Card Slot," click on the gear icon next to the `crypto` slot's prompt.

![Create a card slot](Images/create-card-slot.png)

The "crypto settings" window will open. Scroll down to the "Prompt response cards" section, and add this URL in the "Image URL" text field: <https://cdn1.iconfinder.com/data/icons/cryptocurrency-set-2018/375/Asset_1480-128.png>.

Comment to students that this URL should point to a public image that they can store as a public asset on an AWS S3 bucket. For this demo, we are using a free public image from [Iconfinder](https://www.iconfinder.com/).

![Add card slot image](Images/add-card-slot-image.png)

Explain to the students that a card slot can have up to five cards. In this demo, we will create one card with three options. Now add the following title and subtitle.

* **Title:** `Available Cryptocurrencies`
* **Subtitle:** `Choose one crypto to convert`

![Adding title and subtitle to the card](Images/add-tilte-and-subtile-slot.png)

Next, explain to students that each option will appear as a button on the card, so a title should be defined for each button together with a value. The value is taken from the values assigned when the custom slot type is created.

In this demo, you will see three possible values on the "Button value" dropdown list, as shown below. Once you finish, click  the "Save" button to continue.

![Card slot values](Images/card-slot-values.png)

Click the "Build" button once the build process is done. Test your bot on the "Test bot" window and show to students how the card's options are presented.

Click on `Ethereum`. As you can see below, something strange is happening. Despite selecting `Ethererum`, the bot is converting to `Bitcoin`.

![Sample card slot demo](Images/custom_slots_cards.gif)

**What is happening?** Explain to students that the bot dialogue and elicitation process is working correctly; however, we have to modify the Lambda function to allow the bot to make the correct conversion. This is going to be done in the next activity.

Answer any questions before moving on.

---

### 11. Student Do: Crypto Converter (20 min)

In this activity, students will extend their cryptocurrency converter by adding a custom slot to allow users to select between Bitcoin, Ethereum, or Ripple to convert from dollars. We will also add business logic to identify the cryptocurrency chosen by the user and make the conversion, to the Lambda function.

**Instructions:**

* [README.md](Activities/06-Stu_Crypto_Converter/README.md)

**Files:**

* [lambda_function.py](Activities/06-Stu_Crypto_Converter/Unsolved/lambda_function.py)

---

### 12. Instructor Do: Review Crypto Converter (10 min)

**Files:**

* [lambda_function.py](Activities/06-Stu_Crypto_Converter/Solved/lambda_function.py)

Start by reviewing the bot configuration. Open the Amazon Lex console, navigate to the `convertCAD` intent editor on the `Crypto_Converter` bot and highlight the following:

* As presented in the previous demo, you should have created a new slot type called `CryptoCurrency` with three possible values: Bitcoin, Ethereum, and Ripple.

* The user can either use the value or the synonyms to refer to the cryptocurrencies while talking to the bot.

* Once the new slot type is created, it is possible to add the `crypto` slot to the intent.

* The `crypto` slot should be configured to show prompt response cards as follows:

  ![Crypto slot response cards](Images/crypto_slot_response_cards.png)

* The card's image should be public, it can be stored anywhere on the web; an Amazon S3 public asset may be the best option.

Continue to the Lambda function code. Open the solution on your AWS Lambda online code editor and highlight the following:

* There is no need to validate the name of the cryptocurrency, since the user does not type it.

* On the `get_cryptoprice()` function, the price for each cryptocurrency and its `ID` is retrieved from the alternative.me API using a URL defined on a `nested-if` structure.

  ```python
  def get_cryptoprice(crypto):
      """
      Retrieves the current price of BTC, ETH or XRP in Canadian Dollars from the alternative.me Crypto API.
      """
      url = ""
      id = ""
      if crypto == "Bitcoin":
          url = "https://api.alternative.me/v2/ticker/Bitcoin/?convert=CAD"
          id = "1"
      elif crypto == "Ethereum":
          url = "https://api.alternative.me/v2/ticker/Ethereum/?convert=CAD"
          id = "1027"
      else:
          url = "https://api.alternative.me/v2/ticker/Ripple/?convert=CAD"
          id = "52"

      response = requests.get(url)
      response_json = response.json()
      price_cad = parse_float(response_json["data"][id]["quotes"]["CAD"]["price"])
      return price_cad
  ```

* To fetch the value of the `crypto` slot, a new variable called `crypto` was defined at the beginning of the `convert_cad()` function.

  ```python
  crypto = get_slots(intent_request)["crypto"]
  ```

* The `get_cryptoprice()` function is used in the `convert_cad()` function to fetch the current price of the selected cryptocurrency; then the conversion to Canadian Dollars is calculated.

  ```python
  # Get the current price of BTC, ETH or XRP in CAD and make the conversion from CAD.
  crypto_value = parse_float(cad_amount) / get_cryptoprice(crypto)
  crypto_value = round(crypto_value, 4)
  ```

* The fulfillment message is formatted in the `convert_cad()` function to include the name of the selected cryptocurrency dynamically.

  ```python
  # Return a message with conversion's result.
  return close(
      intent_request["sessionAttributes"],
      "Fulfilled",
      {
          "contentType": "PlainText",
          "content": """Thank you for your information;
          you can get {} {} for your ${} dollars.
          """.format(
              crypto_value, crypto, cad_amount
          ),
      },
  )
  ```

Continue to the Amazon Lex console. Test the bot to validate the changes made on Lambda; you should see a dialogue as follows:

![Extended Crypto Converter demo](Images/crypto_converter_extended.gif)

Open the lesson slides, and go to the slide titled "Deploying Amazon Lex Bots." Highlight the following:

* Once you create your bot in Amazon Lex, you may want to put it into action and have it talk with your potential users.

* You have two options to deploy your Amazon Lex bot into a productive environment to interact with potential users; you can deploy your Amazon Lex bot in mobile applications, or via messaging platforms.

* To integrate your bot with mobile applications, you can use the AWS SDK or the AWS Mobile Hub service.

* Amazon Lex provides four built-in channels to deploy your bot in messaging platforms—Slack, Facebook Messenger, Kik, or Twilio SMS.

Slack out to students the [Amazon Lex deployment guide](https://docs.aws.amazon.com/lex/latest/dg/examples.html), and encourage them to try any of these deployment options by themselves.

Answer any questions before moving on.

---

### 13. Instructor Do: Structured Review (35 min)

**Note:** If you are teaching this lesson on a weeknight, please save this 35-minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address any misunderstandings.

---

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
