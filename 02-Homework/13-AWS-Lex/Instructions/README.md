# Unit 13 Homework Assignment: Robo Advisor for Retirement Plans

![Robot](Images/robot.jpg)

*Photo by [Alex Knight](https://www.pexels.com/@alex-knight-1272316?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from [Pexels](https://www.pexels.com/photo/high-angle-photo-of-robot-2599244/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) | [Free License](https://www.pexels.com/photo-license/)*

## Background

You were hired as digital transformation consultant by one of the most prominent retirement plans providers in the country, they want to increase their client portfolio especially by engaging young people. Since machine learning and NLP are disrupting on finance to improve customer experience, you decide to create a robo advisor that could be used by customers or potential new customers to get investment portfolio recommendations for retirement using Slack.

In this homework assignment, you will combine your new skills about Amazon Web Services with your already mastered Python superpowers, to create a bot that will recommend an investment portfolio for a retirement plan.

You are asked to accomplish the following main tasks:

1. **[Initial Robo Advisor Configuration:](#Initial-Robo-Advisor-Configuration)** Define an Amazon Lex bot with a single intent that stablish a conversation about the requirements to suggest an investment portfolio for retirement.

2. **[Build and Test the Robo Advisor](#Build-and-Test-the-Robo-Advisor):** Make sure that your bot is working and responding accurately along the conversation with the user, by building and testing it.

3. **[Deploy the Robo Advisor on Slack](#Deploy-the-Robo-Advisor-on-Slack):** Publish the bot and create a Robo Advisor Slack app.

4. **[Enhance the Robo Advisor with an Amazon Lambda Function:](#Enhance-the-Robo-Advisor-with-an-Amazon-Lambda-Function)** Create an Amazon Lambda function that validates the user's input and returns the investment portfolio recommendation. This task includes testing the Amazon Lambda function and making the integration with the bot.

5. **Deploy the Robo Advisor Powered by Amazon Lambda:** Publish a new version of your bot that includes the new Amazon Lambda function, also test the new version of your bot on Slack.

---

## Files

* [lambda_function.py](Starter_Files/lambda_function.py)
* [correct_dialog.txt](Test_Cases/correct_dialog.txt)
* [age_error.txt](Test_Cases/age_error.txt)
* [incorrect_amount_error.txt](Test_Cases/incorrect_amount_error.txt)
* [negative_age_error.txt](Test_Cases/negative_age_error.txt)

---

## Instructions

### Initial Robo Advisor Configuration

On this section your will create the `RoboAdvisor` bot and add an intent with its corresponding slots.

Sign in into your AWS Management Console and [create a new custom Amazon Lex bot](https://console.aws.amazon.com/lex/home). Use the following parameters:

* **Bot name:** RoboAdvisor
* **Output voice**: Salli
* **Session timeout:** 5 minutes
* **COPPA**: No

Create the `RecommendPortfolio` intent, and configure some sample utterances as follows (you can add more utterances at your own criteria):

* I want to save money for my retirement
* I'm ​`{age}​` and I would like to invest for my retirement
* I'm `​{age}​` and I want to invest for my retirement
* I want the best option to invest for my retirement
* I'm worried about my retirement
* I want to invest for my retirement
* I would like to invest for my retirement

Move to the *Confirmation Prompt* section, and set the following messages:

* **Confirm:** Thanks, now I will look for the best investment portfolio for you.
* **Cancel:** I will be pleased to assist you in the future.

On this bot you will use four slots, three using built-in types and one custom slot named `riskLevel`. Define the three initial slots as follows:


| Name             | Slot Type            | Prompt                                                                    |
| ---------------- | -------------------- | ------------------------------------------------------------------------- |
| firstName        | AMAZON.US_FIRST_NAME | Thank you for trusting on me to help, could you please give me your name? |
| age              | AMAZON.NUMBER        | How old are you?                                                          |
| investmentAmount | AMAZON.NUMBER        | How much do you want to invest?                                           |

The `riskLevel` custom slot will be used to retrieve the risk level the user is willing to take on the investment portfolio; create this custom slot as follows:

* **Name:** riskLevel
* **Prompt:** What level of investment risk would you like to take?
* **Maximum number of retries:** 2
* **Prompt response cards:** 4

Configure the response cards for the `riskLevel` slot as is shown bellow:

| Card 1                              | Card 2                              |
| ----------------------------------- | ----------------------------------- |
| ![Card 1 sample](Images/card1.png)  | ![Card 2 sample](Images/card2.png)  |

| Card 3                              | Card 4                              |
| ----------------------------------- | ----------------------------------- |
| ![Card 3 sample](Images/card3.png)  | ![Card 4 sample](Images/card4.png)  |

**Note:** You can download free icons from [this website](https://www.iconfinder.com/) or you can use the icons provided on the [`Icons` directory](Icons/).

Leave the error handling configuration for the `RecommendPortfolio` bot with the default values.

![Error handling configuration](Images/error_handling.png)

### Build and Test the Robo Advisor

On this section you will test your Robo Advisor. Build the bot and test it on the chatbot window, you should see a conversation like the one bellow.

![Robo Advisor test](Images/bot-test-no-lambda.gif)

### Deploy the Robo Advisor on Slack

Congratulations! You have your Robo Advisor working. Now in this section, your mission is to publish the first version of your bot and configure the connection to Slack.

1. From the Amazon Lex console, publish the version 1 of the `RoboAdvisor` bot.
2. Login into to the [Slack API website](https://api.slack.com) and create a new app called `Robo Advisor` into the development Slack workspace you defined before on class.
3. Go to the Amazon Lex Console, navigate to the *Channels* tab on the `RoboAdvisor` bot configuration and setup the Slack connection details.
4. Complete the Slack integration and test it.

After completing these tasks you should get your bot working on Slack as follows.

![Robo Advisor test on Slack](Images/robo-advisor-slack-no-lambda.gif)

### Enhance the Robo Advisor with an Amazon Lambda Function

In this section, you will create an Amazon Lambda function that will validate the data provided by the user on the Robo Advisor. Start by creating a new lambda function from scratch and name it `recommendPortfolio`. Select Python 3.7 as runtime.

Use the starter code provided on [lambda_function.py](Starter_Files/lambda_function.py) and complete the `recommend_portfolio()` function by following these guidelines:

#### User Input Validation

* The `age` should by greater than zero and less than 65.
* the `investment_amount` should be equals o greater than 5000.

#### Investment Portfolio Recommendation

Once the intent is fulfilled, the bot should response with an investment recommendation based on the selected risk level as follows:

* **none:** "100% bonds (AGG), 0% equities (SPY)"
* **very low:** "80% bonds (AGG), 20% equities (SPY)"
* **low:** "60% bonds (AGG), 40% equities (SPY)"
* **medium:** "40% bonds (AGG), 60% equities (SPY)"
* **high:** "20% bonds (AGG), 80% equities (SPY)"
* **very high:** "0% bonds (AGG), 100% equities (SPY)"

Be creative while coding your solution, you can have all the code on the `recommend_portfolio()` function, or you can split the functionality across different functions, put your Python coding skills in action!

Once you finish coding your lambda function, test it using the [sample test cases](Test_Cases/) provided for this homework.

After successfully testing your code, open the Amazon Lex Console and navigate to the `RecommendPortfolio` bot configuration, integrate your new lambda function by selecting it on the _Lambda initialization and validation_ and _Fulfillment_ sections. Build your bot, and you should have a conversation as follows.

![Robo Advisor test with Lambda](Images/bot-test-with-lambda.gif)

### Deploy the Robo Advisor Powered by Amazon Lambda

Now your bot is ready to advice customers about retirement plans on Slack. Publish a new version of the bot and test it on Slack. Your final solution should look like this.

![Robo Advisor test with Lambda on Slack](Images/robo-advisor-slack-with-lambda.gif)

## Submission

* Create a python script with your final lambda function.
* From the Amazon Lex Console export your bot, intent and slot using `Amazon Lex` as target platform.
* Create a short video showing a demo of your Robo Advisor in action from Slack.
* Create and upload a repository with the above files to GitHub and post a link in BootCamp Spot.
