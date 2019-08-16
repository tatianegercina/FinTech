### 8. Instructor Do: Testing AWS Lambda Functions (10 mins)

In this activity, students will learn how to test lambda functions to validate Amazon Lex intents.

**Files:**

* [solution.py](Activities/01-Ins_Really_Important/Solved/solution.py)

Show students how to create a test case, test cases should have a valid event data format. Click on the _Test_ button, then choose the _Create new test event_ option and paste the code from the [provided test case](Activities/05-Ins_Intro_Lambda/Solved/convert_test_case.json). Call the test `convertOkText` and click on the _Create_ button to finish.

![Creating a test case](Images/lambda-text-case.png)

Now the name of the new test case appears on the dropdown list next to the _Test_ button, click on it and you can see the test results on the window bellow the Lambda function code.

![Test resutls](Images/lambda-test-ok.png)
