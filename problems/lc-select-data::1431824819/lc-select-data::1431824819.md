# Select Data

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-select-data::1431824819` |
| Solved | 2024-10-23 |
| Runtime | 322 ms (beats 7.911199999999974%) |
| Memory | 70.2 MB (beats 8.32069999999998%) |

## Problem Statement

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with `student_id = 101`.

The result format is in the following example.

 

**Example 1:
Input:**
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
**Output:**
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
**Explanation:
**Student Ulysses has student_id = 101, we select the name and age.

## Solutions

```Python
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"]==101,["name","age"]]
```
