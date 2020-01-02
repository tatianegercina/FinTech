# Mastering Concatenation

Your county's Financial Leaders of America group has recently joined with the Investors Leadership Council. Eager to consolidate the dues and membership data, the treasurer has reached out to you––the group's FinTech guru––to create a master ledger containing financial data for both organizations.

## Instructions

Using the [starter file](Unsolved/mastering_concatenation.ipynb) and the data in the [Resources](Resources) folder, complete the following steps:

1. Load CSV data into Pandas using `read_csv` for each file.

2. Use the `concat` function to concat the `fin_leaders_dues` DataFrame with `investors_leadership_dues` by `axis='rows'` and `join='inner'`.

3. Use the `concat` function to concat DataFrames `fin_leaders_mbr_status` and `investors_leadership_mbr_status` by `axis='columns'` and `join='inner'`.

4. Use the `concat` function to concat the two DataFrames made in steps 2 and 3 using by `axis='columns'` and `join='inner'`.
---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
