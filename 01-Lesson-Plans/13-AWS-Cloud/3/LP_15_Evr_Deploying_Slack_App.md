### 15. Everyone Do: Deploying an Amazon Lex bot to Slack (15 mins)

This is a group activity, students will follow you on the process to publish the `Crypto_Converter` bot, and later, you will show them how to deploy the bot as a Slack App.

Follow the next steps, ask your TAs to assist students along the demo and be sure all the class is following you along the process.

#### Step 1: Publish the Amazon Lex bot

1. Open the Amazon Lex console and navigate to the `Crypto_Converter` bot.

2. Click on the _Publish_ button located at the upper right corner. You should publish your bot before deploying it on any messaging or mobile application.

3. A popup window will appear where you should give a name for your bot's published instance. Name the bot as `CryptoConverterBot` and click on the _Publish_ button to continue.

  ![Publishing a bot](Images/publish-amazon-lex-bot.png)

4. Once the publishing process is finished, you will see the following window. Click on _Close_ to continue.

  ![Publishing bot process done](Images/bot-publishing-done.png)

#### Step 2: Create a Slack Team

Explain to students that, in order to publish the Amazon Lex bot as a Slack App, the first step is to create a Slack Team to deploy the app. Perform the following tasks and be sure students are on track as you move forward.

1. To create a new Slack Team, open your web browser and navigate to https://slack.com/create. Enter your e-mail address and click on the _Next_ button to continue.

  ![Create Slack worspace - step 1](Images/slack-workspace-1.png)

2. A six digit verification code will be sent to your e-mail, check your inbox and type the code in the six boxes to continue.

  ![Create Slack worspace - step 2](Images/slack-workspace-2.png)

3. Once you confirm your six digit code, you will see the next page where you have to create a Slack Team. Type an original name for your team and click on the _Next_ button to continue.

  ![Create Slack worspace - step 3](Images/slack-workspace-3.png)

4. On the next page, you'll be asked for the name of a current project on your team. Type `Crypto Converter Bot` and click on the _Next_ button to continue.

  ![Create Slack worspace - step 4](Images/slack-workspace-4.png)

5. Next you are asked to invite some people to your team, skip this to continue.

  ![Create Slack worspace - step 5](Images/slack-workspace-5.png)

6. You have finished the Slack Team creation, click on the _See Your Channel in Slack_ button to open your brand new channel.

  ![Create Slack worspace - step 6](Images/slack-workspace-6.png)

#### Step 3: Create a Slack Application

Comment to students that now, you are going to login into the Slack Api to create a new Slack Application. The Slack Application will be the bridge between Amazon Lex and Slack to allow users to talk to the bot.

1. Open your web browser and navigate to the Slack API Console at http://api.slack.com. Click on the _Start Building_ button to continue.

  ![Create a Slack App - step 1](Images/slack-app-1.png)

2. Type a name for your new app, for this demo, name the app as `Crypto Converter Bot`. From the _Development Slack Workspace_ dropdown list, select the name of the team's workspace you created on **Step 2**. Click on the _Create App_ button to continue.

  ![Create a Slack App - step 2](Images/slack-app-2.png)

3. After you have successfully created the application, Slack displays the Basic Information page for the application.

  ![Create a Slack App - step 3](Images/slack-app-3.png)

4. In the left menu, choose _Bot Users_ and then choose _Add a bot user_.

  ![Create a Slack App - step 4](Images/slack-app-4.png)

5. Configure the new user as follows:

    * Left the default _Display name_ and a _Default username_ values.
    * On the _Always Show My Bot as Online_, choose `On`.
    * Save the changes by clicking on the _Add Bot User_ button.

  ![Create a Slack App - step 5](Images/slack-app-5.png)

6. In the left menu, choose _Interactive Components_. Toggle the _Interactivity_ option to `On` and specify any valid URL in the _Request URL_ textbox. Use https://slack.com to get the verification token that you need in the next step. You will update this URL later. Click on the _Save Changes_ button to continue.

  ![Create a Slack App - step 6](Images/slack-app-6.png)

7. In the left menu, under _Settings_, choose _Basic Information_. Record the following application credentials to be used in the next step. To protect your credentials privacy, be sure to regenerate your _Client Secret_ and _Verification Token_ after the class.

    * Client ID
    * Client Secret
    * Verification Token

  ![Create a Slack App - step 7](Images/slack-app-7.png)

#### Step 4: Integrate the Slack Application with the Amazon Lex Bot

Now that you have Slack application credentials, you can integrate the application with your Amazon Lex bot. To associate the Slack application with your bot, we will add a bot channel association in Amazon Lex.

1. Open the Amazon Lex console, select the `Crypto_Converter` bot and navigate to the _Channels_ tab. Choose _Slack_ from the left _Channels_ menu to continue.

  ![Integrating Slack App - step 1](Images/slack-integration-1.png)

2. Configure the _Slack_ channel as follows:

    * **Name:** `CyptoConverterSlackApp`
    * **Description:** `Slack channel for the Crypto Converter bot`
    * **KMS Key:** `aws/lex`
    * **Alias:** `CryptoConverterBot`
    * Type the _Client Id_, _Client secret_, and _Verification Token_, which you recorded in the preceding step. These are the credentials of the Slack application.

  ![Integrating Slack App - step 2](Images/slack-integration-2.png)

3. Click on the _Activate_ button to continue. The console creates the bot channel association and returns two URLs, record them.

    * **Postback URL:** It's the Amazon Lex bot's endpoint that listens to Slack events.
    * **OAuth URL:** It's your Amazon Lex bot's endpoint for an OAuth handshake with Slack.

  ![Integrating Slack App - step 3](Images/slack-integration-3.png)

#### Step 5: Complete Slack Integration

Comment to students that, in this section, you'll use the Slack API console to complete the integration of the Slack application.

1. Comeback to the Slack API console, in the left menu, choose _OAuth & Permissions_.

  ![Complete Slack integration - step 1](Images/complete-slack-integration-1.png)

2. In the _Redirect URLs section_, click on the _Add a new Redirect URL_ and add the OAuth URL that Amazon Lex provided in the preceding step. Once you typed the URL, click on the _Add_ button to continue and on _Save URLs_.

  ![Complete Slack integration - step 2](Images/complete-slack-integration-2.png)

3. In the _Scopes_ section, you need to add two permissions. In the _Select Permission Scopes_ dropdown list, filter the list with the following text to add the permissions:

    * `chat:write:bot`
  ![Complete Slack integration - step 3a](Images/complete-slack-integration-3a.png)

    * `team:read`
    ![Complete Slack integration - step 3b](Images/complete-slack-integration-3b.png)

    Click on the _Save Changes_ button to continue.

4. In the left menu, choose _Interactive Components_, update the _Request URL_ value to the Postback URL that Amazon Lex provided in the preceding step. Click on the _Save Changes_ button to continue.

  ![Complete Slack integration - step 4](Images/complete-slack-integration-4.png)

5. In the left menu, choose _Event Subscriptions_, configure this feature as follows:

    * Toggle the _Enable events_ option to `On`.

    * Set the _Request URL_ value to the Postback URL that Amazon Lex provided in the preceding step. One you type it, Slack will verify the URL.
  ![Complete Slack integration - step 5a](Images/complete-slack-integration-5a.png)

    * In the _Subscribe to Bot Events_ section, click on the _Add Bot User Event_ button and filter the list by typing `message.im`. This event will enable direct messaging between the end user and the Slack bot. Click on the _Save Changes_ button to continue.
    ![Complete Slack integration - step 5b](Images/complete-slack-integration-5b.png)

#### Step 6: Test the Integration Between Amazon Lex and Slack

Congratulate students on reaching this point, this is the final stage on getting Amazon Lex integrated with Slack, there are just some last final touches to refine. Continue on the Slack API Console as follows.

1. In the left menu, choose _Manage Distribution_ under the _Settings_ option. Click on the _Add to Slack_ button to install the application.

  ![Test integration - step 1](Images/test-slack-integration-1.png)

2. On the next page, you should authorize the bot to respond to messages on the Slack Team you created. Notice that a new user called `@crypto_converter_bot` will be added to your Slack Team. Click on the _Allow_ button to continue.

  ![Test integration - step 2](Images/test-slack-integration-2.png)

3. You are redirected to your Slack team. In the left menu, in the _Apps_ section, choose your bot and engage in a chat with your Slack application, which is linked to the `Crypto_Converter` Amazon Lex bot. Start with the `I want to invest in crypto` sample utterance to test the bot. You should see an dialog like the shown bellow.

  ![Demo crypto converter bot on Slack](Images/slack-crypto-converter-bot-test.gif)

**Note:** If you don't see your bot, choose the plus icon (+) next to _Apps_ section to search for it.

Ask your TAs to assist students to test their bots, answer any additional question before continue.
