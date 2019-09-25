# Students Do: Encoding Categorical Data for Machine Learning

In this activity, you are tasked to encode some categorical and text features of a dataset that contains `2097` loans applications. In forthcoming activities, you will use this dataset to predict fraudulent transactions.

## Dataset Description.

The data provided, is based on the dataset used in the research paper entitled [_“Should This Loan be Approved or Denied?”: A Large Dataset with Class Assignment Guidelines_](https://doi.org/10.1080/10691898.2018.1434342) published by Min Li, Amy Mickel & Stanley Taylor from the California State University on the Journal of Statistics Education.

This dataset contains information about loans applications managed by the U.S. Small Business Administration (SBA), it was adapted for Today's class. The dataset is distributed under the [Creative Commons (CC BY-SA 4.0) license](https://creativecommons.org/licenses/by-sa/4.0/).

The columns in the dataset are the following:

* `Year`: The fiscal year of the loan application.
* `Month`: Month of the fiscal year.
* `Amount`: The loan amount issued.
* `Term`: Loan's term in months
* `Bank`: Name of the bank that issued the loan.
* `State`: Borrower state.
* `City`: Borrower city.
* `Zip`: Borrower zipcode.
* `CreateJob`: Number of jobs created using the loan.
* `NoEmp`: Number of business employees.
* `RealEstate`: Define if loan is backed by real estate.
* `RevLineCr`: Indicates if it's a revolving line of credit.
* `UrbanRural`: Location type of the borrower.
* `Default`: Indicates if the loan was defaulted (`1`) or not (`0`).

## Instructions

### Loading the Data

Load the `sba_loans.csv` data in a Pandas DataFame. Show the `head` to get familiar with the columns and data values.

### Integer Encoding

#### Manual Integer Encoding

Perform a manual integer encoding of the `Month` column, use a dictionary to map months names with their corresponding numerical value.

#### Encoding Data using `LabelEncoder`

Use the `LabelEncoder` method from `sklearn` to perform an integer encoding of the `RealEstate`, `RevLineCr` and `UrbanRural` columns.

#### Encoding Data using `get_dummies()`

Perform a binary encoding on the `Bank`, `State` and `City` columns using the Pandas `get_dummies()` function.

### Save the Preprocessed File

Finally, save the preprocessed file as `sba_loans_encoded.csv` for forthcoming usage.

## Hints

You can use the Python's [`calendar` module](https://docs.python.org/3/library/calendar.html) to create the months dictionary for the manual integer encoding of the `month` column, as it's explained [here](https://stackoverflow.com/a/31796820/4325668).
