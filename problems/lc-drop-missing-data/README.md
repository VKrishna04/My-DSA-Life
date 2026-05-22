# Drop Missing Data

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-drop-missing-data` |
| Topics | Data Manipulation, Pandas, Data Cleaning |
| Solved | 2024-10-25 |
| Runtime | 393 ms (beats 5.153500000000024%) |
| Memory | 70.1 MB (beats 6.277400000000027%) |

## Problem Statement

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

There are some rows having missing values in the `name` column.

Write a solution to remove the rows with missing values.

The result format is in the following example.

 

**Example 1:**

**Input:
**+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 217        | None    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+
**Output:
**+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 779        | Georgia | 20  | 
| 849        | Willow  | 14  | 
+------------+---------+-----+
**Explanation:** 
Student with id 217 havs empty value in the name column, so it will be removed.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a build-in function in pandas library to remove the rows with missing values based on specified data.

</details>

## Solutions

```Python
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset = 'name')
```

## AI Review

### Review
**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the number of rows in the DataFrame. Pandas must iterate through the 'name' column once to identify null values.
*   **Space:** $O(N \times M)$, where $M$ is the number of columns. By default, `dropna` creates a new copy of the DataFrame containing the filtered results.

**2. Correctness**
The solution is correct for the problem's scope.
*   **Edge Case:** It only removes rows where 'name' is `None` or `NaN`. It will **not** remove rows where 'name' is an empty string (`""`) or whitespace, as Pandas does not treat these as null by default.

**3. Optimization**
If memory usage is a concern and the original DataFrame is no longer needed, use `inplace=True`:
```python
students.dropna(subset=['name'], inplace=True)
return students
```
This modifies the DataFrame in place rather than allocating memory for a full copy.

**4. Key Algorithmic Pattern**
**Data Filtering/Wrangling:** Using built-in library functions to perform vectorized row elimination based on schema constraints.
