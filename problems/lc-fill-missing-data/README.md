# Fill Missing Data

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-fill-missing-data` |
| Topics | Data Manipulation, Pandas |
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

## Hints

<details>
<summary>Hint 1</summary>

Consider using a build-in function in pandas library to fill the missing values of specified columns.

</details>

## Solutions

```Python
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(value = 0, inplace = True)
    return products
```

## AI Review

**1. Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows in the DataFrame. Pandas must iterate through the specific column once to identify and replace null values.
*   **Space Complexity:** $O(1)$ auxiliary space. Because `inplace=True` is used, the operation modifies the existing memory block of the column rather than creating a full copy.

**2. Correctness & Edge Cases**
*   **Correctness:** The solution is functionally correct for the problem requirements.
*   **Edge Cases:**
    *   **Empty DataFrame:** Handles correctly (no-op).
    *   **Data Types:** If `quantity` contains floats, `0` will be stored as `0.0`. If the column is an object type, the operation still succeeds.
    *   **Missing Column:** Will raise a `KeyError` if the "quantity" column does not exist (though usually guaranteed in LeetCode).

**3. Concrete Optimization**
Avoid using `inplace=True`. Modern Pandas is deprecating the `inplace` parameter across most methods because it often doesn't actually improve performance and can cause "SettingWithCopy" warnings. Use direct assignment:
`products['quantity'] = products['quantity'].fillna(0)`

**4. Key Algorithmic Pattern**
**Data Imputation** (Value substitution for missing data).
