# Drop Duplicate Rows

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-drop-duplicate-rows` |
| Topics | Data Manipulation, Hashing |
| Solved | 2024-10-24 |
| Runtime | 547 ms (beats 5.2954999999999695%) |
| Memory | 69.5 MB (beats 10.938799999999988%) |

## Problem Statement

DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+

There are some duplicate rows in the DataFrame based on the `email` column.

Write a solution to remove these duplicate rows and keep only the **first** occurrence.

The result format is in the following example.

 

**Example 1:**
**Input:**
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
**Output: ** 
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
**Explanation:**
Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a build-in function in pandas library to remove the duplicate rows based on specified data.

</details>

## Solutions

```Python
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = "email")
```

## AI Review

### Review

**1. Time and Space Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows. Pandas uses a hash table internally to identify duplicates in a single pass.
*   **Space Complexity:** $O(N)$ in the worst case. By default, `drop_duplicates` creates a new DataFrame copy. The internal hash set also scales with the number of unique entries.

**2. Correctness**
The solution is correct for standard inputs.
*   **Edge Cases:**
    *   **Empty DataFrame:** Correctly returns an empty result.
    *   **Nulls:** Pandas treats `NaN` as a value; it will keep the first null email and drop subsequent ones.
    *   **Case Sensitivity:** It treats `User@a.com` and `user@a.com` as different. If the problem implies case-insensitivity, a `.str.lower()` preprocessing step would be needed.
    *   **Keep Logic:** It defaults to keeping the *first* occurrence.

**3. Optimization**
To improve memory efficiency, use the `inplace=True` parameter to modify the existing DataFrame rather than creating a copy:
`customers.drop_duplicates(subset="email", inplace=True)`
`return customers`

**4. Key Algorithmic Pattern**
**Hashing:** The underlying implementation relies on a hash table to track previously encountered values in the specified subset.
