# Select Data

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-select-data` |
| Topics | Data Manipulation, Pandas, Vectorization |
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

## Hints

<details>
<summary>Hint 1</summary>

Consider applying both row and column filtering to select the desired data.

</details>

## Solutions

```Python
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"]==101,["name","age"]]
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the number of rows in the DataFrame. Pandas performs a linear scan to evaluate the boolean condition.
*   **Space:** $O(N)$ in the worst case to store the result if all rows match the criteria (though typically $O(K)$ where $K$ is the number of matches).

**2. Correctness**
The solution is correct and follows idiomatic Pandas patterns.
*   **Edge Cases:** 
    *   **Empty DataFrame:** Correctly returns an empty DataFrame with the specified columns.
    *   **No matches:** Correctly returns an empty DataFrame.
    *   **Multiple matches:** Correctly returns all rows where the ID is 101.
    *   **Data Types:** If `student_id` contains `NaN` or is stored as a string, the comparison might fail, though LeetCode's schema usually prevents this.

**3. Optimization**
The current `.loc` implementation is highly efficient. For massive datasets, ensuring `student_id` is set as an **index** would allow $O(1)$ or $O(\log N)$ lookup using `students.loc[101, ["name", "age"]]`. However, for standard filtering, no further optimization is needed.

**4. Key Pattern**
**Boolean Indexing** (Vectorized filtering).
