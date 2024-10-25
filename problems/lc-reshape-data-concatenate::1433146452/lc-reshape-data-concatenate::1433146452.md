# Reshape Data: Concatenate

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reshape-data-concatenate::1433146452` |
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

## Solutions

```Python
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)
```
