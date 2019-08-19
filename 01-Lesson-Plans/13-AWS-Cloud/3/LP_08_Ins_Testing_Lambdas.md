### 8. Instructor Do: Testing AWS Lambda Functions (10 mins)

In this activity, students will learn how to test AWS Lambda functions that validates Amazon Lex intents.

**Files:**

* [convertOkText.json](Activities/08-Ins_Testing_Lambdas/Solved/convertOkText.json)

* [convertErrAmount.json](Activities/08-Ins_Testing_Lambdas/Solved/convertErrAmount.json)

* [convertErrDate.json](Activities/08-Ins_Testing_Lambdas/Solved/convertErrDate.json)

Comment to students that one of the challenges working with AWS Lambda is dealing with errors, so it's important to know how to test a Lambda function on the AWS Lambda console. For this activity, three test cases are provided.

Explain to students that, in order to test a Lambda function, a `JSON` file should be created to send a testing event to Lambda, the structure of the event depends on the kind of service you are connecting to Lambda. This demo only will cover how to test Amazon Lex intents.

Open the `convertUSD` lambda function on the AWS Lambda console to show students how to create a test case. Click on the _Test_ button on the upper right corner, then choose the _Create new test event_ option and paste the code from the [`convertOkText.json` test case](Activities/08-Ins_Testing_Lambdas/Solved/convertOkText.json).

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
    "name": "ConvertUSD",
    "slots": {
      "birthday": "1978-12-16",
      "usdAmount": "10"
    },
    "confirmationStatus": "None"
  }
}
```

After pasting the test case code, highlight the following:

* On the `bot` key, the name of the Amazon Lex bot is defined, so students should be sure that this name matches with their bot's name.

* The `$LATEST` it's the default value to use for the `alias` and the `version` keys.

* Since this test event is passed as text, the value of the `outputDialogMode` key is `text`.

* Under the `currentIntent` key, the values of the bot's slots are given, students should be aware that those names match with their slots names.

* This is a test case where the `birthday` and `usdAmount` slots have valid data.

Continue the demo by naming the test `convertOkTest` and click on the _Create_ button to finish.

![Creating a test case](Images/lambda-text-case.png)

Now the name of the new test case appears on the dropdown list next to the _Test_ button, click on the _Test_ button and you can see the test results on the window bellow the Lambda function code.

![Test results](Images/lambda-test-ok.png)

Since this test case has valid data for both slots, comment to students that the test status is `Succeeded` and the execution results show a response with both slots fulfilled with the data passed on the test case.

Show students how to add a new text case, click on the test events dropdown list and choose the _Configure test events_ option.

![Add new test event](Images/lambda-add-new-test-evet.png)

By default you will see that the last used test case is selected, notice that the _Edit saved test events_ option is selected, so can edit the test event.

![Edit saved test event](Images/lambda-add-new-test-default-selection.png)

Choose the _Create new test event_ option, you will notice that the previous test event remains as template. Change the value of the `usdAmount` slot to zero to test the amount validation coded on the Lambda. Click on the _Create_ button to continue.

![Create a new test event to cast amount value](Images/lambda-add-convertErrAmount.png)

Select the `convertErrAmount` test on the _Test events_ dropdown list and click on the _Test_ button. Explain to students that the test ran successfully again, however, now Lambda responses with a `ElicitSlot` type of dialog where the message defined on the Lambda can be read. This test event is validating that the incorrect value is caught by the code at the Lambda and the appropriate new data elicitation is sent to the user via Amazon Lex.

![Running the convertErrAmount test event](Images/lambda-testing-convertErrAmount.png)

Create a final test event, but now to validate what happens when an invalid date of birth is given by the user. Repeat the same process described before to create a new test event. Introduce `2014-12-16` on the `birthday` slot and named the test event as `convertErrDate`.

![Adding the convertErrDate test event](Images/lambda-add-convertErrDate.png)

Execute the the `convertErrDate` test, comment to students that the date validation was successfully corroborated since the `ElicitSlot` dialog type is returned together with the message asking for a different age of birth.

Close the execution results window, now you will introduce a typo on the code to raise a runtime error. On the `parse_float()` function, delete the closing parenthesis on line 12. Click on the _Save_ button and run any of the testing events.

![Provoking a runtime error](Images/lambda-provoking-runtime-error.png)

After running the test event, explain to students that the test status is `Failed` and that the response contains the error description and the line where the error were detected.

![Runtime error](Images/lambda-runtime-error.png)

Comment to students that these type or errors are difficult to catch on Amazon Lex, that's why it's important to test Lambdas on the AWS Lambda console before linking the Lambda to the Amazon Lex bot.

Answer any remainder question and continue to the next activity.
