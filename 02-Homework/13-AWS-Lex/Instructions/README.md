# Unit 13 Homework Assignment - The Power of the Cloud and Unsupervised Learning

## Background

It is time to take what you have learned about unsupervised learning and the AWS services and apply it to new situations. For this assignment, you will need to complete **one of two** (not both) challenges. Which challenge you take on is your choice. Just be sure to give it your all -- as the skills you hone will become powerful tools in your FinTech tool belt.

### Before You Begin

1. Create a new repository for this project called `unit13-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. Inside your local git repository, create a directory for the challenge assignment you choose. Use folder names corresponding to the challenges: **RoboAdvisor** or  **ClusteringCrypto**.

4. Add your solution files to this folder.

5. Push the above changes to GitHub or GitLab.

---

## Option 1: Robo Advisor for Retirement Plans

![Robot](Images/robot.jpg)

*Photo by [Alex Knight](https://www.pexels.com/@alex-knight-1272316?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from [Pexels](https://www.pexels.com/photo/high-angle-photo-of-robot-2599244/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) | [Free License](https://www.pexels.com/photo-license/)*

### Background

You were hired as a digital transformation consultant by one of the most prominent retirement plan providers in the country; they want to increase their client portfolio, especially by engaging young people. Since machine learning and natural language processing are disrupting finance to improve customer experience, you decide to create a robo advisor that could be used by customers or potential new customers to get investment portfolio recommendations for retirement.

In this homework assignment, you will combine your new skills with Amazon Web Services with your already mastered Python superpowers, to create a bot that will recommend an investment portfolio for a retirement plan.

You are asked to accomplish the following main tasks:

1. **[Initial Robo Advisor Configuration:](#Initial-Robo-Advisor-Configuration)** Define an Amazon Lex bot with a single intent that establishes a conversation about the requirements to suggest an investment portfolio for retirement.

2. **[Build and Test the Robo Advisor](#Build-and-Test-the-Robo-Advisor):** Make sure that your bot is working and responding accurately along with the conversation with the user, by building and testing it.

3. **[Enhance the Robo Advisor with an Amazon Lambda Function:](#Enhance-the-Robo-Advisor-with-an-Amazon-Lambda-Function)** Create an Amazon Lambda function that validates the user's input and returns the investment portfolio recommendation. This task includes testing the Amazon Lambda function and making the integration with the bot.

---

### Files

* [lambda_function.py](Starter-Files/RoboAdvisor/lambda_function.py)
* [correct_dialog.txt](Starter-Files/RoboAdvisor/Test-Cases/correct_dialog.json)
* [age_error.txt](Starter-Files/RoboAdvisor/Test-Cases/age_error.json)
* [incorrect_amount_error.txt](Starter-Files/RoboAdvisor/Test-Cases/incorrect_amount_error.json)
* [negative_age_error.txt](Starter-Files/RoboAdvisor/Test-Cases/negative_age_error.json)

---

### Instructions

#### Initial Robo Advisor Configuration

In this section, you will create the `RoboAdvisor` bot and add an intent with its corresponding slots.

Sign-in into your AWS Management Console using your `administrator` IAM user and [create a new custom Amazon Lex bot](https://console.aws.amazon.com/lex/home). Use the following parameters:

* **Bot name:** `RoboAdvisor`

* **Output voice**: `Salli`

* **Session timeout:** `5 minutes`

* **Sentiment analysis:** `No`

* **COPPA**: `No`

Create the `RecommendPortfolio` intent, and configure some sample utterances as follows (you can add more utterances at your criteria):

* `I want to save money for my retirement`

* `I'm ​{age} and I would like to invest for my retirement`

* `I'm ​{age}​ and I want to invest for my retirement`

* `I want the best option to invest for my retirement`

* `I'm worried about my retirement`

* `I want to invest for my retirement`

* `I would like to invest for my retirement`

Move to the "Confirmation Prompt" section, and set the following messages:

* **Confirm:** `Thanks, now I will look for the best investment portfolio for you.`

* **Cancel:** `I will be pleased to assist you in the future.`

On this bot, you will use four slots, three using built-in types and one custom slot named `riskLevel`. Define the three initial required slots as follows:


| Name             | Slot Type            | Prompt                                                                    |
| ---------------- | -------------------- | ------------------------------------------------------------------------- |
| firstName        | AMAZON.US_FIRST_NAME | Thank you for trusting on me to help, could you please give me your name? |
| age              | AMAZON.NUMBER        | How old are you?                                                          |
| investmentAmount | AMAZON.NUMBER        | How much do you want to invest?                                           |

The `riskLevel` custom slot will be used to retrieve the risk level the user is willing to take on the investment portfolio; create this custom slot as follows:

* **Slot type name:** `riskLevel`

* **Description:** `Level of investment risk.`

* **Slot values and synonyms:**

  | Value | Synonym |
  | ----- | ------- |
  | None  | None    |
  | Very Low | Very Low |
  | Low | Low |
  | Medium | Medium |
  | High | High |
  | Very High | Very High|

![riskLevel slot initial configuration](Images/risk_level_slot.png)

Rename the `slotFour` as `riskLevel` and set the prompt as `What level of investment risk would you like to take?`.

Configure the `riskLevel` slot with four response cards, to add a new card click on the plus sign below the card configuration.

![Add a new slot response card](Images/add-slot-card.png)

Configure the response cards as follows; the image for each card should be uploaded to your Amazon S3 bucket.

| Card 1                              | Card 2                              |
| ----------------------------------- | ----------------------------------- |
| ![Card 1 sample](Images/card1.png)  | ![Card 2 sample](Images/card2.png)  |

| Card 3                              | Card 4                              |
| ----------------------------------- | ----------------------------------- |
| ![Card 3 sample](Images/card3.png)  | ![Card 4 sample](Images/card4.png)  |

**Note:** You can download free icons for your cards from [Iconfinder](https://www.iconfinder.com/), or you can use the icons provided on the [`Icons` directory](Starter-Files/RoboAdvisor/Icons) into the `RoboAdvisor` starter files folder.

#### Build and Test the Robo Advisor

In this section, you will test your Robo Advisor. Build the bot and test it on the chatbot window. You should see a conversation like the one below.

![Robo Advisor test](Images/bot-test-no-lambda.gif)

#### Enhance the Robo Advisor with an Amazon Lambda Function

In this section, you will create an Amazon Lambda function that will validate the data provided by the user on the Robo Advisor. Start by creating a new lambda function from scratch and name it `recommendPortfolio`. Select Python 3.7 as runtime.

Use the starter code provided on [lambda_function.py](Starter_Files/lambda_function.py) and complete the `recommend_portfolio()` function by following these guidelines:

##### User Input Validation

* The `age` should be greater than zero and less than 65.
* the `investment_amount` should be equals o greater than 5000.

##### Investment Portfolio Recommendation

Once the intent is fulfilled, the bot should response with an investment recommendation based on the selected risk level as follows:

* **none:** "100% bonds (AGG), 0% equities (SPY)"
* **very low:** "80% bonds (AGG), 20% equities (SPY)"
* **low:** "60% bonds (AGG), 40% equities (SPY)"
* **medium:** "40% bonds (AGG), 60% equities (SPY)"
* **high:** "20% bonds (AGG), 80% equities (SPY)"
* **very high:** "0% bonds (AGG), 100% equities (SPY)"

Be creative while coding your solution, you can have all the code on the `recommend_portfolio()` function, or you can split the functionality across different functions, put your Python coding skills in action!

Once you finish coding your lambda function, test it using the [sample test cases](Test_Cases/) provided for this homework.

After successfully testing your code, open the Amazon Lex Console and navigate to the `RecommendPortfolio` bot configuration, integrate your new Lambda function by selecting it on the _Lambda initialization and validation_ and _Fulfillment_ sections. Build your bot, and you should have a conversation as follows.

![Robo Advisor test with Lambda](Images/bot-test-with-lambda.gif)

### Option 1 Submission

You should create a brand new repository in GitHub and upload the following files to your repo.

* A python script with your final lambda function.

* From the Amazon Lex Console, export your bot using `Amazon Lex` as the target platform and upload the ZIP file to your repo.

* Create a short video or animated GIF showing a demo of your Robo Advisor in action from the test window. Upload the video or animated GIF file to your repo.

Once you have uploaded all the files into the repo, post a link to your homework's repository in BootCamp Spot.

### Hints

* If you are using a Mac, you can create a screen-recording using the built-in QuickTime player. Follow [this link](https://support.apple.com/en-us/HT208721#quicktime) to learn more.

* If you are using Windows 10, you can create a screen-recording using the built-in Xbox Game Bar. Follow [this link](https://beta.support.xbox.com/help/friends-social-activity/share-socialize/record-game-clips-game-bar-windows-10) to learn more.

---

## Option 2: Clustering Crypto

![Cryptocurrencies coins](Images/cryptocurrencies-coins.jpg)
_[Cryptocurrencies coins by Worldspectrum](https://www.pexels.com/@worldspectrum?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) | [Free License](https://www.pexels.com/photo-license/)_

### Background

You are a Senior Manager at the Advisory Services team on a [Big Four firm](https://en.wikipedia.org/wiki/Big_Four_accounting_firms), one of your most important clients, a prominent investment bank, is interested in offering a new cryptocurrencies investment portfolio for its customers; however, they are lost in the immense universe of cryptocurrencies, they ask you to present a report of what cryptocurrencies are on the trading market and how cryptocurrencies could be grouped towards creating a classification for developing this new investment product.

In this homework assignment, you have the opportunity to put in action your new unsupervised learning and Amazon SageMaker skills to cluster cryptocurrencies and create some plots to present your results.

You are asked to accomplish the following main tasks:

* **[Data Preprocessing](#Data-Preprocessing):** Prepare data for dimension reduction with PCA and clustering using K-Means.

* **[Reducing Data Dimensions Using PCA](#Reducing-Data-Dimensions-Using-PCA):** Reduce data dimension using the `PCA` algorithm from `sklearn`.

* **[Clustering Cryptocurrencies Using K-Means](#Clustering-Cryptocurrencies-Using-K-Means):** Predict clusters using the cryptocurrencies data using the `KMeans` algorithm from `sklearn`.

* **[Visualizing Results](#Visualizing-Results):** Create some plots and data tables to present your results.

* **[Challenge](#Challenge):** Deploy your notebook to Amazon SageMaker.

---

### Files

* [crypto_clustering.ipynb](Starter-Files/ClusteringCrypto/crypto_clustering.ipynb)

* [crypto_data.csv](Starter-Files/ClusteringCrypto/Resources/crypto_data.csv)

---

### Instructions

#### Data Preprocessing

In this section, you have to load the information about cryptocurrencies from the provided `CSV` file and perform some data preprocessing tasks. The data was retrieved from  _CryptoCompare_ using this endpoint: `https://min-api.cryptocompare.com/data/all/coinlist`.

Upload the starter `crypto_clustering.ipynb` notebook to the root folder of Amazon SageMaker Studio, also, upload the `crypto_data.csv` data file to Amazon SageMaker Studio into a folder called `Data`.

Open the starter Jupyter notebook and select the `Python 3 (Data Science)` kernel and perform the following data preprocessing task.

1. Load the data into a Pandas DataFrame named `crypto_df`.

2. Remove all cryptocurrencies that are not on trading.

3. Remove all cryptocurrencies that have not an algorithm defined.

4. Remove the `IsTrading` column.

5. Remove all cryptocurrencies with at least one null value.

6. Remove all cryptocurrencies without coins mined.

7. Store the names of all cryptocurrencies on a DataFramed named `coins_name`, use the `crypto_df.index` as the index for this new DataFrame.

8. Remove the `CoinName` column.

9. Create dummies variables for all the text features, store the resulting data on a DataFrame named `X`.

10. Use the [`StandardScaler` from `sklearn`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) to standardize all the data of the `X` DataFrame. Remember, this is important prior to using PCA and K-Means algorithms.

#### Reducing Data Dimensions Using PCA

Use the [`PCA` algorithm from `sklearn`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) to reduce the dimensions of the `X` DataFrame down to three principal components.

Once you have reduced the data dimensions, create a DataFrame named `pcs_df` using as columns names `"PC 1", "PC 2"` and `"PC 3"`;  use the `crypto_df.index` as the index for this new DataFrame.

You should have a DataFrame like the following.

![pcs_df](Images/pcs_df.png)

#### Clustering Cryptocurrencies Using K-Means

In this section, you will use the [`KMeans` algorithm from `sklearn`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) to cluster the cryptocurrencies using the PCA data.

Perform the following tasks:

1. Create an Elbow Curve to find the best value for `k`, use the `pcs_df` DataFrame.

2. Once you define the best value for `k`, run the `Kmeans` algorithm to predict the `k` clusters for the cryptocurrencies data. Use the `pcs_df` to run the `KMeans` algorithm.

3. Create a new DataFrame named `clustered_df`, that includes the following columns `"Algorithm", "ProofType", "TotalCoinsMined", "TotalCoinSupply", "PC 1", "PC 2", "PC 3", "CoinName", "Class"`. You should maintain the index of the `crypto_df` DataFrames as is shown bellow.

    ![clustered_df](Images/clustered_df.png)

#### Visualizing Results

In this section, you will create some data visualization to present the final results. Perform the following tasks:

1. Create a 2D-Scatter plot using the `plot()` method of Pandas to show the clusters using the `clustered_df` DataFrame. You can test different combinations for the `x` and `y` parameters, for example, you can start by setting `x="PC 1"` and `y="PC 2"`.

2. Display all the rows of the DataFrame to create a data table with all the current tradable cryptocurrencies. The table should have the following columns: `"CoinName", "Algorithm", "ProofType", "TotalCoinSupply", "TotalCoinsMined", "Class"`

3. Create a 2D-Scatter plot using the `plot()` method of Pandas to present the clustered data about cryptocurrencies having `x="TotalCoinsMined"` and `y="TotalCoinSupply"` to contrast the number of available coins versus the total number of mined coins.

### Option 2 Submission

* Code your solution using the provided starter Jupyter notebook.

* Create and upload a repository with the Jupyter notebook containing the solution to GitHub and post a link in BootCamp Spot.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
