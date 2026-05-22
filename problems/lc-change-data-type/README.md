# Change Data Type

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-change-data-type` |
| Topics | Data Manipulation, Pandas, Schema Transformation |
| Solved | 2024-10-25 |
| Runtime | 474 ms (beats 5.150499999999987%) |
| Memory | 68.9 MB (beats 9.87120000000001%) |

## Problem Statement

DataFrame `students`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+

Write a solution to correct the errors:

The `grade` column is stored as floats, convert it to integers.

The result format is in the following example.

 

**Example 1:**
**Input:
**DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
**Output:
**+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
**Explanation:** 
The data types of the column grade is converted to int.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a build-in function in pandas library with a dictionary to convert the datatype of columns as specified.

</details>

## Solutions

```Python
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade':int})
```

## AI Review

**Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows in the DataFrame. Pandas must iterate through the column to perform the type conversion.
*   **Space Complexity:** $O(N)$ in the worst case, as `astype` creates a copy of the column/DataFrame by default.

**Correctness**
The solution is correct for standard inputs. However, it will fail in these edge cases:
*   **Missing Data:** If the `grade` column contains `NaN` or `None`, converting to `int` will raise a `ValueError` because standard Python integers in Pandas do not support NaNs.
*   **Non-numeric Strings:** If a string cannot be parsed as an integer (e.g., "A+"), it will raise a `ValueError`.

**Optimization**
To handle missing values without crashing, use the nullable integer type `Int64` (note the capital 'I'):
```python
students['grade'] = students['grade'].astype('Int64')
```
Alternatively, use `copy=False` within `astype` to minimize memory overhead if the transformation allows for a view, though this is rarely guaranteed for type casts.

**Key Algorithmic Pattern**
**Vectorized Data Transformation:** Leveraging Pandas' underlying NumPy arrays to apply operations across an entire column simultaneously rather than using manual loops.
