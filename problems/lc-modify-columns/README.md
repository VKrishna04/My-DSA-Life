# Modify Columns

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-modify-columns` |
| Topics | Vectorization, Data Manipulation, Pandas |
| Solved | 2024-10-25 |
| Runtime | 377 ms (beats 5.096900000000014%) |
| Memory | 69.2 MB (beats 5.848499999999994%) |

## Problem Statement

DataFrame `employees`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+

A company intends to give its employees a pay rise.

Write a solution to **modify** the `salary` column by multiplying each salary by 2.

The result format is in the following example.

 

**Example 1:**

**Input:
**DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
**Output:
**+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
**Explanation:
**Every salary has been doubled.

## Hints

<details>
<summary>Hint 1</summary>

Considering multiplying each salary value by 2, using a simple assignment operation. The calculation of the value is done column-wise.

</details>

## Solutions

```Python
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(n)$, where $n$ is the number of rows. Pandas uses vectorized operations to iterate through the series.
*   **Space:** $O(1)$ auxiliary space. The operation modifies the existing column in-place without creating a new DataFrame structure.

**2. Correctness**
*   **Empty DataFrame:** Handles correctly (no rows to process).
*   **Data Types:** If the `salary` column contains strings, `* 2` will result in string replication (e.g., "500" becomes "500500"). It assumes the column is numeric.
*   **Nulls:** `NaN` values remain `NaN` after multiplication, which is standard behavior for salary updates.

**3. Optimization**
The current code is already highly efficient due to vectorization. For extremely large datasets, you could ensure the `salary` column is stored as a specific numeric subtype (e.g., `float32` instead of `float64`) to reduce the memory footprint before processing.

**4. Key Algorithmic Pattern**
**Vectorization:** Applying a single operation across an entire array/series at once, leveraging optimized C-level loops instead of Python-level `for` loops.
