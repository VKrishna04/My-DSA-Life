# Reshape Data: Melt

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reshape-data-melt` |
| Topics | Data Manipulation, Matrix Reshaping, Pandas |
| Solved | 2024-10-26 |
| Runtime | 375 ms (beats 5%) |
| Memory | 69.6 MB (beats 5%) |

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

```Pandas
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars = 'product', value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter', value_name='sales')
```

## AI Review

1. **Complexity**: 
   - **Time Complexity**: $O(N \times M)$, where $N$ is the number of rows and $M$ is the number of columns being melted. Each element in the value columns must be visited once to populate the new long-format DataFrame.
   - **Space Complexity**: $O(N \times M)$ to store the resulting reshaped DataFrame.

2. **Correctness**: The solution is correct and follows the standard Pandas API. It handles missing values (NaNs) and duplicate identifier values correctly.

3. **Optimization**: Omit the `value_vars` parameter if all columns except the identifier are meant to be melted. Using `report.melt(id_vars='product', ...)` makes the code more robust to schema changes, such as adding extra quarters (e.g., `quarter_5`), without needing to update the column list manually.

4. **Key Pattern**: **Wide-to-Long Reshaping** (Unpivoting). This pattern transforms attribute columns into row values to normalize data for easier analysis or plotting.
