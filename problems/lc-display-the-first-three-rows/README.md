# Display the First Three Rows

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-display-the-first-three-rows` |
| Topics | Pandas, Data Manipulation, Slicing |
| Solved | 2024-10-23 |
| Runtime | 436 ms (beats 5.1431999999999904%) |
| Memory | 68.9 MB (beats 11.325499999999986%) |

## Problem Statement

DataFrame: `employees`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+

Write a solution to display the **first `3` **rows** **of this DataFrame.

 

**Example 1:**

**Input:
**DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
**Output:**
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
**Explanation:** 
Only the first 3 rows are displayed.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a built-in function in pandas library to retrieve the initial rows.

</details>

## Solutions

```Python
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
```

## AI Review

### Review of "Display the First Three Rows"

**1. Complexity**
*   **Time Complexity:** $O(1)$ relative to the total number of rows $N$. Since the number of rows to retrieve is fixed at $k=3$, the operation takes constant time regardless of the size of the input DataFrame.
*   **Space Complexity:** $O(1)$ auxiliary space. The returned object is a small view/copy of fixed size (3 rows).

**2. Correctness**
The solution is correct and robust.
*   **Edge Case (< 3 rows):** If the DataFrame contains 0, 1, or 2 rows, `head(3)` will return all available rows without throwing an error, which matches LeetCode's expected behavior.
*   **Edge Case (Empty DF):** Returns an empty DataFrame with the same schema.

**3. Optimization**
The solution is already optimal for readability and performance. An alternative is `employees.iloc[:3]`, which is functionally identical but `head()` is more idiomatic for this specific task.

**4. Key Algorithmic Pattern**
**Built-in API Utilization:** Leveraging high-level library functions (Pandas) for efficient data slicing and selection.
