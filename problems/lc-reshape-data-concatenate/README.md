# Reshape Data: Concatenate

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reshape-data-concatenate` |
| Topics | Data Manipulation, Pandas, Array Stacking |
| Solved | 2024-10-25 |
| Runtime | 443 ms (beats 5.043599999999942%) |
| Memory | 69 MB (beats 6.416300000000021%) |

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

```Python
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)
```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(C \times (R1 + R2))$, where $C$ is the number of columns and $R$ is the number of rows. Pandas must visit and copy every element into a new memory block.
*   **Space Complexity:** $O(C \times (R1 + R2))$. `pd.concat` creates a completely new DataFrame; it does not perform the operation in-place.

**2. Correctness**
The code is correct. It handles edge cases like empty DataFrames gracefully. Note that if `df1` and `df2` have different column names, Pandas will perform an "outer join" by default, filling missing columns with `NaN`.

**3. Optimization**
Use `ignore_index=True`:
```python
return pd.concat([df1, df2], axis=0, ignore_index=True)
```
This is a concrete optimization when the original index labels are not needed. It prevents Pandas from trying to preserve or align potentially conflicting indices, which reduces overhead and avoids duplicate index labels.

**4. Key Algorithmic Pattern**
Data Reshaping / Structural Transformation.
