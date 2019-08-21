### 6. Student Do: Understanding Lambdas (15 mins)

In this activity, students will inspect the code of a Lambda function to have a better understanding about how it works. Students will create their own Lambda function by importing the provided code and will build a new version of their bot. Be sure to slack out the [`lambda_function.py`](Activities/06-Stu_Understanding_Lambdas/Unsolved/lambda_function.py) code to students before starting the activity.

**Instructions:**

* [README.md](Activities/06-Stu_Understanding_Lambdas/README.md)

**Files:**

* [lambda_function.py](Activities/06-Stu_Understanding_Lambdas/Unsolved/lambda_function.py)

---

### 7. Instructor Do: Review Understanding Lambdas (10 mins)

**Files:**

* [lambda_function.py](Activities/06-Stu_Understanding_Lambdas/Solved/lambda_function.py)

* [Crypto_Converter export file](Activities/06-Stu_Understanding_Lambdas/Solved/Crypto_Converter_1_6dfe9e0e-82de-4d08-b33b-3bfd1d827672_Bot_LEX_V1.zip)

Open the Lambda function code in VSCode, conduct a facilitated discussion by asking students about their findings, insights or additional questions after reviewing the provided code. Start with some questions as follows.

* Does anyone has a different idea to organize the function's _building blocks_?

  **Sample Answer:** Maybe we can omit the `parse_float()`, `get_btcprice()` and `validate_data()` helper functions and embed all the functionality on the `convert_usd()` intent handler function.

  **Sample Answer:** We can drop the `dispatch()` function by adding the intents' name validation into the `lambda_handler()` function.

* Do you think we can avoid using the `parse_float()` function?

  **Sample Answer:** Yes, we can do that by simply using the `float()` function.

  **Sample Answer:** Yes, we can avoid defining the `parse_float()` function and use the `float()` function instead, however, having this function returning the value of `nan` for non numeric values is more secure and eases testing.

* Is there any other way to define the dialog helper functions?

  **Sample Answer:** We could define a function that receives all the data from the current intent and have some nested `if` controlling the kind of dialog and response.

  **Sample Answer:** I thinks this is a very efficient way to handle the different dialog types.

Slack out the following the following resources, encourage students to learn more about AWS Lambda and Lex.

* [Lambda Function Input Event and Response Format](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html#using-lambda-input-event-format)

* [Amazon Lex and AWS Lambda Blueprints](https://docs.aws.amazon.com/lex/latest/dg/lex-lambda-blueprints.html)

Be sure to answer any reminder question and move to the next activity.
