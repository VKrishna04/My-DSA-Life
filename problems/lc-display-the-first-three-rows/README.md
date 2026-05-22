# Display the First Three Rows

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-display-the-first-three-rows` |
| Solved | 2024-10-23 |
| Solve Time | 19s |
| Runtime | 436 ms (beats 5.026599999999921%) |
| Memory | 68.9 MB (beats 11.630999999999998%) |

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

## Solutions

```Pandas
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
```

## AI Review

### Review of 'Display the First Three Rows'

**1. Complexity**
*   **Time Complexity:** $O(1)$. Since we are fetching a constant number of rows (3), the operation does not scale with the size of the input DataFrame $N$.
*   **Space Complexity:** $O(1)$. The result is a shallow copy/view of a fixed size, regardless of the original DataFrame's size.

**2. Correctness**
The solution is **correct** and handles edge cases gracefully:
*   **Empty DataFrame:** `head(3)` returns an empty DataFrame without error.
*   **Fewer than 3 rows:** If the DataFrame contains 1 or 2 rows, it returns all available rows, which is the expected behavior in Pandas.

**3. Optimization**
The current solution is already optimal. However, for internal performance in low-level selection, you could use:
```python
return employees.iloc[:3]
```
While `head(3)` is essentially a wrapper for `iloc[:3]`, `iloc` is the direct positional indexing method. In practice, the performance difference is negligible.

**4. Key Algorithmic Pattern**
**DataFrame Slicing:** This pattern involves selecting a specific subset of data based on row index positions (top-K selection).
