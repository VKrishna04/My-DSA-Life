# Delete Duplicate Emails

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-delete-duplicate-emails` |
| Topics | Database |
| Solved | 2025-06-02 |
| Runtime | 962 ms (beats 16.175500000000074%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Person`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

 

Write a solution to** delete** all duplicate emails, keeping only one unique email with the smallest `id`.

For SQL users, please note that you are supposed to write a `DELETE` statement and not a `SELECT` one.

For Pandas users, please note that you are supposed to modify `Person` in place.

After running your script, the answer shown is the `Person` table. The driver will first compile and run your piece of code and then show the `Person` table. The final order of the `Person` table **does not matter**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
**Output:** 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
**Explanation:** john@example.com is repeated two times. We keep the row with the smallest Id = 1.

## Solutions

```MySQL
# Write your MySQL query statement below
delete p1
from Person p1
join Person p2
on p1.email = p2.email and p1.id > p2.id
```

## AI Review

### 1. Complexity
*   **Time Complexity**: **$O(N^2)$** in the worst case (where $N$ is the number of rows). Without an index, MySQL performs a nested loop join. With an index on `email`, this improves toward **$O(N \log N)$**.
*   **Space Complexity**: **$O(N)$** for the internal join buffer used to manage the cross-reference of IDs.

### 2. Correctness
*   **Status**: Fully correct for the problem constraints.
*   **Edge Cases**:
    *   **No duplicates**: The `p1.id > p2.id` condition will never be met; zero rows deleted (Correct).
    *   **All emails identical**: Only the record with the absolute minimum `id` will remain (Correct).
    *   **Multiple duplicates**: If three rows share an email (IDs 1, 2, 3), rows 2 and 3 will match the criteria and be deleted (Correct).

### 3. Concrete Optimization
**Add a Composite Index**: Create an index on `(email, id)`. This allows the database to locate duplicate groups and identify the minimum ID using an index scan rather than a full table scan, drastically reducing execution time for large datasets.

### 4. Key Algorithmic Pattern
**Self-Join**: Comparing a table to itself to identify relationships between rows (specifically a non-equi join on the `id` column).
