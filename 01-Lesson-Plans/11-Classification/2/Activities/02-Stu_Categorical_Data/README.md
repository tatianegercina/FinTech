# Students Do: Encoding Categorical Data for Machine Learning

In this activity, you are tasked to encode some categorical and text features of a fictional dataset that contains 100,000 credit card transactions. In forthcoming activities, you will use this dataset to predict fraudulent transactions.

## Dataset Description.

The data provided, is based on the [Synthetic Financial Datasets For Fraud Detection](https://www.kaggle.com/ntnu-testimon/paysim1) created by [Edgar Lopez-Rojas](http://bth.diva-portal.org/smash/person.jsf?pid=authority-person%3A44509&dswid=-31), at the Blekinge Institute of Technology (Sweden), in order to contribute to the research in the domain of fraud detection.

The dataset was originally generated using [the PaySim simulator](https://github.com/EdgarLopezPhD/PaySim), PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country. This dataset is distributed under the [Creative Commons (CC BY-SA 4.0) license](https://creativecommons.org/licenses/by-sa/4.0/), and it was adapted for Today's class.

The columns in the dataset are the following:

* `date`: Credit card transaction date.
* `dateMonthName`: Month name of transaction date.
* `dateWeekdayName`: Day name of transaction date.
* `dateQuarter`: Quarter of transaction date.
* `type`: Type of transactions (`CASH-IN`, `CASH-OUT`, `DEBIT`, `PAYMENT` and `TRANSFER`).
* `amount`: Amount of the transaction.
* `cardholder`: Credit card holder name.
* `gender`: Credit card holder gender.
* `cardNumber`: Credit card number.
* `oldbalanceOrig`: Credit card balance before the transaction.
* `newbalanceOrig`: Credit card balance after the transaction.
* `merchant`: The name of the merchant were the transactions has been made.
* `oldbalanceDest`: Merchant's account balance before the transaction.
* `newbalanceDest`: Merchant's account balance after the transaction.
* `isFraud`: This variable indicates if the transaction was fraudulent (`1`) or not (`0`).

## Instructions

### Loading the Data

Load the `credit_card_transactions.csv` data in a Pandas DataFame. Show the `head` to get familiar with the columns and data values.

### Data Preprocessing

#### Verify Data Types

In this section, you should verify that the data type for each colum is semantically correct, e.g. the `date` column data type should be `datetime`.

Perform all the data types conversion needed.

### Integer Encoding

#### Manual Integer Encoding

Perform a manual integer encoding of the `dateMonthName` and `dateWeekdayName` columns using [the Pandas `dt` accessor](https://pandas.pydata.org/pandas-docs/stable/reference/series.html#datetimelike-properties) and the `date` column.

#### Encoding Data using `LabelEncoder`

Use the `LabelEncoder` method from `sklearn` to perform an integer encoding of the `type` column.

#### Encoding Data using `get_dummies()`

Perform a binary encoding on the `gender` and `merchant` columns using the Pandas `get_dummies()` function.

### Removing Unnecessary Columns

In this section, you will drop those columns that would be unnecessary for a machine learning algorithm.

* The `date` column can be removed, since you already have its data encoded in the `dateMonthName`, `dateWeekdayName` and `dateQuarter` columns.

* There is only one credit card per card holder, so the `cardholder` column can be removed, since we can uniquely identify each person using the credit card number that is already a numerical feature.

* In order to have meaningful column names, rename the `dateMonthName` and `dateWeekdayName` columns as `dateMonth` and `dateWeekDay`.

### Save the Preprocessed File

Finally, save the preprocessed file as `transactions_data_encoded.csv` for forthcoming usage.

**Note:** This step will take between 3 up to 7 minutes depending on your computer's features.
