# The Thrill of the Case


* Change each animal's species to the correct species.

  ![../Images/case01.png](../Images/case01.png)

## Solution

```sql
UPDATE animals
SET species =
CASE species
    WHEN "duck" THEN "mouse"
    WHEN "mouse" THEN "duck"
END;
```
