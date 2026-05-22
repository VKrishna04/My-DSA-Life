# Create a DataFrame from List

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-create-a-dataframe-from-list` |
| Topics | Data Manipulation, Pandas |
| Solved | 2024-10-23 |
| Runtime | 390 ms (beats 5%) |
| Memory | 68.5 MB (beats 5%) |

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
*   **Time Complexity:** $O(N \times M)$, where $N$ is the number of rows and $M$ is the number of columns (here $M=2$, so $O(N)$). Pandas must iterate through the nested list to populate its internal storage.
*   **Space Complexity:** $O(N \times M)$, as a new DataFrame object is created to store the data in memory.

**2. Correctness**
The solution is correct. 
*   **Edge Case:** If `student_data` is an empty list `[]`, Pandas correctly returns an empty DataFrame with the specified column headers.
*   **Data Types:** The function assumes the input lists contain integers. Pandas will infer these types correctly.

**3. Optimization**
While efficient for standard use, for extremely large datasets, you can provide an explicit `dtype` to the constructor (e.g., `dtype=int`) to bypass the overhead of type inference.

**4. Key Algorithmic Pattern**
**Object Instantiation / Data Structure Conversion**: Utilizing a library-specific constructor to transform a native Python data structure (nested list) into a specialized tabular structure (DataFrame).
