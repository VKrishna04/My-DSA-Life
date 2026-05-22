# Fill Missing Data

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-fill-missing-data` |
| Topics | Data Manipulation, Data Imputation, Pandas API |
| Solved | 2024-10-25 |
| Runtime | 351 ms (beats 5%) |
| Memory | 68.1 MB (beats 13%) |

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

## Hints

<details>
<summary>Hint 1</summary>

Consider using a build-in function in pandas library to fill the missing values of specified columns.

</details>

## Solutions

```Pandas
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(value = 0, inplace = True)
    return products
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows in the DataFrame. Pandas must traverse the specified column once to identify and replace null values.
*   **Space Complexity:** $O(1)$ auxiliary space. While the DataFrame itself occupies $O(N \times M)$ space, `inplace=True` modifies the existing object without creating a full structural copy.

**2. Correctness**
*   The solution is correct for the problem constraints.
*   **Edge Cases:** If the `quantity` column is missing from the input, it will raise a `KeyError`. If the column contains non-numeric data types that are incompatible with integer `0`, Pandas will generally cast the column to `object` type, which is functional but inefficient.

**3. Optimization**
Modern Pandas (2.0+) is moving away from the `inplace` parameter. To future-proof the code and support **Copy-on-Write** optimizations, use assignment:
```python
products['quantity'] = products['quantity'].fillna(0)
```
Alternatively, for multiple columns, use:
```python
products.fillna({'quantity': 0}, inplace=True)
```

**4. Key Algorithmic Pattern**
Data Imputation (Handling missing values).
