# Reshape Data: Pivot

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reshape-data-pivot` |
| Topics | Data Reshaping, Pivot Table |
| Solved | 2024-10-25 |
| Runtime | 464 ms (beats 5%) |
| Memory | 70.1 MB (beats 6%) |

## Problem Statement

DataFrame `weather`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+

Write a solution to **pivot** the data so that each row represents temperatures for a specific month, and each city is a separate column.

The result format is in the following example.

 

**Example 1:**
**Input:**
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
**Output:**`
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+`
**Explanation:
**The table is pivoted, each column represents a city, and each row represents a specific month.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a built-in function in pandas library to transform the data

</details>

## Solutions

```Pandas
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index = 'month', columns = 'city', values = 'temperature')
```

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time Complexity**: $O(N)$, where $N$ is the number of rows in the DataFrame. Pandas must scan the data once to map indices and columns to the new structure.
    *   **Space Complexity**: $O(N)$, as the resulting pivoted DataFrame stores the same data points, though organized differently.

2.  **Correctness**: 
    The solution is correct for the standard LeetCode constraints. However, `df.pivot()` will raise a `ValueError` if there are **duplicate entries** for the same `(month, city)` pair. If duplicates were possible, `df.pivot_table()` would be required.

3.  **Optimization**: 
    To improve performance on massive datasets with many repeated strings, convert the `city` column to the `category` dtype before pivoting. This reduces memory usage and speeds up the internal grouping logic.
    ```python
    weather['city'] = weather['city'].astype('category')
    ```

4.  **Algorithmic Pattern**: 
    Data Reshaping (Long-to-Wide transformation).
