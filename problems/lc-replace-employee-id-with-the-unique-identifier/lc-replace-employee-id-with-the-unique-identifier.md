# Replace Employee ID With The Unique Identifier

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-replace-employee-id-with-the-unique-identifier` |
| Topics | Database |
| Solved | 2026-04-25 |
| Runtime | 1229 ms (beats 40.64640000000008%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Employees`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

 

Table: `EmployeeUNI`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.

 

Write a solution to show the **unique ID **of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in **any** order.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
**Output:** 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
**Explanation:** 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.

## Solutions

```MySQL
# Write your MySQL query statement below
select u.unique_id, e.name
from Employees as e
left join EmployeeUNI as u
on e.id = u.id
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N + M)$ on average, where $N$ and $M$ are the number of rows in `Employees` and `EmployeeUNI`. Database engines typically use a Hash Join or Nested Loop Join with index lookups ($O(N \log M)$).
*   **Space Complexity:** $O(N)$ to store and return the result set.

### 2. Correctness
*   **Correct.** The use of `LEFT JOIN` is essential here. It ensures that every employee from the `Employees` table is represented in the output, even if they do not have a corresponding entry in `EmployeeUNI` (in which case `unique_id` correctly returns `NULL`).
*   **Edge Cases:** Handles employees with no unique ID perfectly. No issues with duplicate IDs as they are defined as Primary Keys in the schema.

### 3. Optimization
*   The query is already optimal for this schema. To ensure peak performance, verify that `EmployeeUNI.id` is indexed (which it is, as a Primary Key), allowing the join to perform a fast index seek rather than a full table scan.

### 4. Key Algorithmic Pattern
*   **Left Outer Join:** Used to combine rows from two tables while preserving all records from the "left" table, filling in missing matches from the "right" table with `NULL`.
