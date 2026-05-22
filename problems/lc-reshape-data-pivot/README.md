# Reshape Data: Pivot

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reshape-data-pivot` |
| Topics | Data Reshaping, Matrix Transformation |
| Solved | 2024-10-25 |
| Runtime | 464 ms (beats 5.044500000000023%) |
| Memory | 70.1 MB (beats 5.826000000000004%) |

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

```Python
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index = 'month', columns = 'city', values = 'temperature')
```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows in the DataFrame. Pandas must iterate through the data to re-index and map values to the new shape.
*   **Space Complexity:** $O(N)$, as the pivoted DataFrame stores the same number of data points in a different structure.

**2. Correctness**
*   **Duplicate Entries:** The `pivot` method will raise a `ValueError` if there are multiple entries for the same `month` and `city` combination. In LeetCode contexts, the input is usually guaranteed to be unique; otherwise, `pivot_table` (which aggregates) would be required.
*   **Missing Data:** If a city is missing a temperature for a specific month, Pandas correctly fills that cell with `NaN`.

**3. Optimization**
If memory usage is a concern for large datasets, convert the `city` and `month` columns to the `category` dtype before pivoting. This reduces the memory footprint of the index and column headers.

**4. Key Algorithmic Pattern**
**Data Reshaping:** This utilizes a long-to-wide transformation, reorganizing row-wise observations into a columnar matrix format.
