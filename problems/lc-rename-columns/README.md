# Rename Columns

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-rename-columns` |
| Topics | Data Manipulation, Pandas, Schema Mapping |
| Solved | 2024-10-25 |
| Runtime | 332 ms (beats 5.0908000000000335%) |
| Memory | 69.5 MB (beats 9.573200000000003%) |

## Problem Statement

DataFrame `students`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+

Write a solution to rename the columns as follows:

	- `id` to `student_id`

	- `first` to `first_name`

	- `last` to `last_name`

	- `age` to `age_in_years`

The result format is in the following example.

 

**Example 1:**
**Input:
**+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
**Output:**
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
**Explanation:** 
The column names are changed accordingly.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a build-in function in pandas library with a dictionary to rename the columns as specified.

</details>

## Solutions

```Python
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns = {'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})
```

## AI Review

### Review
**1. Complexity**
*   **Time Complexity:** $O(N \times M)$, where $N$ is the number of rows and $M$ is the number of columns. While renaming the header is $O(M)$, Pandas creates a full copy of the underlying data by default.
*   **Space Complexity:** $O(N \times M)$ because a new DataFrame is allocated to store the copied data.

**2. Correctness**
The solution is correct. The `rename` method is robust; if a key in the dictionary doesn't exist in the DataFrame, Pandas ignores it rather than raising an error. It handles empty DataFrames correctly.

**3. Optimization**
Use the `inplace=True` parameter:
```python
students.rename(columns={...}, inplace=True)
return students
```
This modifies the DataFrame directly, reducing auxiliary space complexity to $O(1)$ by avoiding a full data copy (though internal metadata updates still occur).

**4. Key Algorithmic Pattern**
**Schema Mapping:** Using a Hash Map (dictionary) to define a transformation between existing metadata keys and new labels.
