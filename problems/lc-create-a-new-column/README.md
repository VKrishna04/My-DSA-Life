# Create a New Column

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-create-a-new-column` |
| Topics | Pandas, Vectorization, Data Manipulation |
| Solved | 2024-10-23 |
| Runtime | 342 ms (beats 5.015899999999971%) |
| Memory | 68.6 MB (beats 6.484%) |

## Problem Statement

DataFrame `employees`
+-------------+--------+
| Column Name | Type.  |
+-------------+--------+
| name        | object |
| salary      | int.   |
+-------------+--------+

A company plans to provide its employees with a bonus.

Write a solution to create a new column name `bonus` that contains the **doubled values** of the `salary` column.

The result format is in the following example.

 

**Example 1:**

**Input:**
DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+
**Output:**
+---------+--------+--------+
| name    | salary | bonus  |
+---------+--------+--------+
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  | 6593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |
+---------+--------+--------+
**Explanation:** 
A new column bonus is created by doubling the value in the column salary.

## Hints

<details>
<summary>Hint 1</summary>

Consider using the `[]` brackets with the new column name at the left side of the assignment. The calculation of the value is done element-wise.

</details>

## Solutions

```Python
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees['salary']*2
    return employees
```

## AI Review

### Review of "Create a New Column" Solution

**1. Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows. Pandas performs a vectorized operation across the entire "salary" series.
*   **Space Complexity:** $O(N)$ to store the additional "bonus" column in memory.

**2. Correctness**
The solution is correct and idiomatic for Pandas.
*   **Edge Cases:** 
    *   **Empty DataFrame:** Handles correctly (returns an empty column).
    *   **Null Salaries:** If `salary` contains `NaN`, the `bonus` will also be `NaN`, which is standard behavior.
    *   **Data Types:** If `salary` contains non-numeric types (e.g., strings), the multiplication will either replicate the string or raise a `TypeError`.

**3. Optimization**
The current solution is already optimal due to **Vectorization**. For memory efficiency in very large datasets, you could use `employees['salary'].mul(2)` to ensure the operation stays within optimized C-level routines, though the syntax used is functionally identical. If memory is a concern, ensure the `salary` column is a smaller numeric subtype (e.g., `int32` instead of `int64`).

**4. Key Algorithmic Pattern**
**Vectorization (Broadcasting):** Instead of looping through rows manually, Pandas applies the scalar operation (`* 2`) across the entire Series simultaneously using low-level optimizations.
