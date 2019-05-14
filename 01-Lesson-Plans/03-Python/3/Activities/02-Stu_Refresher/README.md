# E-Mail Marketing

The Marketing department wants to begin understanding the differences in purchasing activity amongst the firm's customers, so as to create personalized e-mail newsletters for each customer.

Therefore, Harold has been asked from Marketing to categorize customers based on their sales revenue and assign a business tier: Platinum, Gold, Silver, or Bronze. Then, depending on the assigned business tier, he needs to generate different phrases for each customer.

Create a program to help Harold impress Marketing with his abilities.

## Instructions

* Create a function named `create_phrase` that takes in `name` and `revenue` as parameters and returns a dynamic greeting based on revenue conditionals:

  * Platinum = 3001+
  * Gold = 2001-3000
  * Silver = 1001-2000
  * Bronze = 0-1000

* Create a for loop that iterates through `customers` and prints out the constructed greeting for each customer
