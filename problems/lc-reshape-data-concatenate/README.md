# Reshape Data: Concatenate

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reshape-data-concatenate` |
| Topics | Data Manipulation, Pandas, Concatenation |
| Solved | 2024-10-25 |
| Runtime | 443 ms (beats 5%) |
| Memory | 69 MB (beats 6%) |

## Problem Statement

DataFrame `df1`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame `df2`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to concatenate these two DataFrames **vertically** into one DataFrame.

The result format is in the following example.

 

**Example 1:**

**Input:
df1**
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+
**df2
**+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+
**Output:**
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
+------------+---------+-----+
**Explanation:
**The two DataFramess are stacked vertically, and their rows are combined.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a built-in function in pandas library with the appropriate axis argument.

</details>

## Solutions

```Pandas
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)
```

## AI Review

### Review
1. **Complexity**:
   - **Time**: $O(N + M)$, where $N$ and $M$ are the total number of elements in `df1` and `df2`. Pandas must traverse and copy all data to a new memory block.
   - **Space**: $O(N + M)$ to allocate the resulting combined DataFrame.

2. **Correctness**:
   The solution is correct. However, if the dataframes have overlapping indices, the result will contain duplicate index labels. If columns do not align perfectly, Pandas will perform an outer join by default, introducing `NaN` values for missing columns.

3. **Optimization**:
   Add `ignore_index=True`. In most data reshaping tasks, the original row indices are not meaningful after concatenation. Using `ignore_index=True` ensures a clean, continuous integer index (0 to N+M-1) and can slightly improve downstream performance by avoiding index-related conflicts.
   ```python
   return pd.concat([df1, df2], axis=0, ignore_index=True)
   ```

4. **Key Pattern**:
   **Vertical Concatenation (Row Stacking)**: The standard approach for merging datasets with identical or similar schema.
