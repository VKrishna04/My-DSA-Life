# Create a DataFrame from List

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-create-a-dataframe-from-list` |
| Topics | Data Structures, Array, Matrix |
| Solved | 2024-10-23 |
| Runtime | 390 ms (beats 5%) |
| Memory | 68.5 MB (beats 6%) |

## Problem Statement

Write a solution to **create** a DataFrame from a 2D list called `student_data`. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, `student_id` and `age`, and be in the same order as the original 2D list.

The result format is in the following example.

 

**Example 1:**

**Input:
**student_data:**
**`[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]`
**Output:**
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
**Explanation:**
A DataFrame was created on top of student_data, with two columns named `student_id` and `age`.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a built-in function in pandas library and specifying the column names within it.

</details>

## Solutions

```Pandas
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ["student_id", "age"])
```

## AI Review

### Review
**1. Complexity**
*   **Time:** $O(N \times M)$, where $N$ is the number of students and $M$ is the number of columns (2). Pandas must iterate through the nested list to populate the underlying NumPy arrays.
*   **Space:** $O(N \times M)$ to store the resulting DataFrame in memory.

**2. Correctness**
The solution is correct and idiomatic for the problem description.
*   **Edge Cases:** An empty list `[]` correctly produces an empty DataFrame with the specified column headers. If the inner lists vary in length, Pandas may introduce `None`/`NaN` or raise a `ValueError`, but per the LeetCode constraints, the input is a consistent 2D list.

**3. Optimization**
For very large datasets, providing the `dtype` explicitly (e.g., `dtype=int`) can prevent Pandas from performing unnecessary type inference during construction, slightly improving performance.

**4. Key Pattern**
**Constructor Injection/Data Marshalling:** This pattern involves passing raw, structured data (list of lists) into a higher-level object constructor (`pd.DataFrame`) that handles internal memory allocation and schema mapping.
