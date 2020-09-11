# Market Capitalization

In this activity, you will create a dictionary, and then update, remove, and extract values in/from the dictionary.

## Background

Sam wants to categorize banks by their market capitalizations, which is the total dollar market value of a company's outstanding shares. Because she wants to know the relationship between a certain bank and its market capitalization, Sam uses a dictionary to index bank names to the value of its market cap.

Sam needs to make a few changes to her dictionary of bank market caps because she noticed a few errors and omissions. Help Sam fix her dictionary of bank market caps, and even better, help her group the banks by their corresponding market capitalization tier.

## Instructions

Using the [starter file](Unsolved/Core/market_cap_core.py), complete the following:

- Initialize the dictionary of `banks`. Add the following key-value pairs:

  - National Bank of Canada: 327
  - Toronto-Dominion Bank: 302
  - Royal Bank of Canada: 173
  - Wells Fargo: 273
  - Goldman Sachs: 87
  - Morgan Stanley: 72
  - Canadian Imperial Bank of Commerce: 83
  - TD Bank: 108
  - Bank of Montreal: 67
  - Capital One: 47
  - FNB Corporation: 4
  - Laurentian Bank of Canada: 3
  - Ally Financial: 12
  - Montreal Trust Company: 145
  - Canadian Western Bank: .97

- Change the market cap for `Royal Bank of Canada` to `170`.

- Add a new bank `Scotiabank` to the dictionary and set the market cap to `33`.

- Delete `Montreal Trust Company` from the dictionary, as it is a depreciated bank acquired by Scotiabank in 1994.

## Challenge

Group banks by their corresponding market capitalization tier.

- Iterate over the key-value pairs in the `banks` dictionary and calculate the following:

  - Total market capitalization
  - Total number of banks
  - Average market capitalization
  - Largest bank
  - Smallest bank

- Use an if-else statement and lists to compare and group banks by their corresponding market capitalization: `mega-cap`, `large-cap`, `mid-cap`, and `small-cap`.

  - `mega-caps`: Market capitalization greater than or equal to `$300 billion`.

  - `large-caps`: Market capitalization greater than or equal to `$10 billion` and less than `$300 billion`.

  - `mid-caps`: Market capitalization greater than or equal to `$2 billion` and less than `$10 billion`.

  - `small-caps`: Market capitalization greater than or equal to `$300 million` and less than `$2 billion`.

## Hint

Your results should look similar to the following:

```text
Total Market Capitalization: 1588
Total Number of Banks: 15
Average Market Capitalization: 105.87
Largest Bank: National Bank of Canada
Smallest Bank: Canadian Western Bank
------------------------------------------------
Mega Cap Banks: ['National Bank of Canada', 'Toronto-Dominion Bank']
Large Cap Banks: ['Royal Bank of Canada', 'Wells Fargo', 'Goldman Sachs', 'Morgan Stanley', 'Canadian Imperial Bank of Commerce', 'TD Bank', 'Bank of Montreal', 'Capital One', 'Ally Financial', 'Scotiabank']
Mid Cap Banks: ['FNB Corporation', 'Laurentian Bank of Canada']
Small Cap Banks: ['Canadian Western Bank']
```

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
