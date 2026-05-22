# Reshape Data: Melt

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reshape-data-melt` |
| Topics | Data Manipulation, Pandas, Array Reshaping |
| Solved | 2024-10-26 |
| Runtime | 375 ms (beats 5.097300000000021%) |
| Memory | 69.6 MB (beats 5.357100000000006%) |

## Problem Statement

DataFrame `report`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+

Write a solution to **reshape** the data so that each row represents sales data for a product in a specific quarter.

The result format is in the following example.

 

**Example 1:**

**Input:
**+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
**Output:**
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
**Explanation:**
The DataFrame is reshaped from wide to long format. Each row represents the sales of a product in a quarter.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a built-in function in pandas library to transform the data

</details>

## Solutions

```Python
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars = 'product', value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter', value_name='sales')
```

## AI Review

### Review
**1. Complexity**
*   **Time Complexity:** $O(N \times K)$, where $N$ is the number of rows and $K$ is the number of `value_vars` (in this case, 4). The algorithm must iterate over every cell in the specified columns to transform them into rows.
*   **Space Complexity:** $O(N \times K)$. A new DataFrame is created to store the reshaped data, containing $N \times K$ rows.

**2. Correctness**
The solution is correct and follows the Pandas API precisely. It handles potential edge cases such as empty DataFrames or missing values (`NaN`) within the quarters correctly by preserving them in the long format.

**3. Optimisation**
If the DataFrame only contains the `product` column and the four quarter columns, you can omit the `value_vars` parameter. Pandas will automatically treat all columns not listed in `id_vars` as `value_vars`. This simplifies the code without changing performance.

**4. Key Algorithmic Pattern**
**Data Reshaping (Unpivoting):** This pattern transforms data from a "wide" format (multiple columns per observation) to a "long" format (multiple rows per observation), facilitating easier aggregation and analysis.
