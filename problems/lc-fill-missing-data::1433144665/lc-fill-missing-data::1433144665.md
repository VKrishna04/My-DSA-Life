# Fill Missing Data

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-fill-missing-data::1433144665` |
| Solved | 2024-10-25 |
| Runtime | 379 ms (beats 5.124400000000005%) |
| Memory | 69.1 MB (beats 13.329500000000003%) |

## Problem Statement

DataFrame `products`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+

Write a solution to fill in the missing value as `**0**` in the `quantity` column.

The result format is in the following example.

 

**Example 1:**
**Input:**+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | None     | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
**Output:
**+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 0        | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 779      | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
**Explanation:** 
The quantity for Wristwatch and WirelessEarbuds are filled by 0.

## Solutions

```Python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(value = 0, inplace = True)
    return products
```
