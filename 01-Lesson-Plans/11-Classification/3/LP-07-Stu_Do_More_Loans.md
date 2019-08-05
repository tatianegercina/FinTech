## 7. Students Do: Oversampling

In this activity, students will pratice using random and SMOTE oversampling in combination with logistic regression to predict whether or not someone is likely to default on their credit card loans in a given month given demographic information. 

**Files:**

[more_loans.ipynb](Activities/04-Stu_Do_More_Loans/Unsolved/more_loans.ipynb)

[README.md](Activities/04-Stu_Do_More_Loans/README.md)

**Dataset**

Yeh, I. C., & Lien, C. H. (2009). The comparisons of data mining techniques for the predictive accuracy of probability of default of credit card clients. Expert Systems with Applications, 36(2), 2473-2480. (https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients#)

Introduce students to the dataset they will be using for this activity. Each row represents a person with a credit card account. ln_balance_limit is the log of the maximum balance they can have on the card; 1 is female, 0 male for sex; the education is denoted: 1 = graduate school; 2 = university; 3 = high school; 4 = others; 1 is married and 0 single for marriage; default_next_month is whether the person defaults in the following month (1 yes, 0 no).