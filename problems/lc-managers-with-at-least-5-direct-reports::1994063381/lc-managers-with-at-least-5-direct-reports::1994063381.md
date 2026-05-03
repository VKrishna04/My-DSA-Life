# Managers with at Least 5 Direct Reports

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-managers-with-at-least-5-direct-reports::1994063381` |
| Topics | Database |
| Solved | 2026-05-03 |
| Runtime | 341 ms (beats 68.10809999999995%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Employee`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.

 

Write a solution to find managers with at least **five direct reports**.

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
**Output:** 
+------+
| name |
+------+
| John |
+------+

## Solutions

```MySQL
# Write your MySQL query statement below
select m.name
from employee as m
inner join employee as e
on e.managerId = m.id
group by m.id
having count(e.id) >= 5
```

## AI Review

### 1. Complexity
*   **Time Complexity**: $O(N^2)$ in the worst case without indexes, as the self-join compares all rows. With an index on `managerId`, it improves to $O(N \log N)$ or $O(N)$.
*   **Space Complexity**: $O(N)$ to store the intermediate joined table and the hash map for grouping.

### 2. Correctness
*   **Edge Cases**: The solution is generally correct. It handles managers with the same name properly because it groups by the unique `m.id`. 
*   **SQL Standards**: Under `ONLY_FULL_GROUP_BY` mode (common in modern MySQL), this may fail because `m.name` is selected but not included in the `GROUP BY` clause. Adding `m.name` to the `GROUP BY` is safer.

### 3. Optimization
Use a **subquery** to filter IDs first. This avoids the overhead of joining full row data before counting:
```sql
SELECT name 
FROM Employee 
WHERE id IN (
    SELECT managerId 
    FROM Employee 
    GROUP BY managerId 
    HAVING COUNT(*) >= 5
);
```

### 4. Key Algorithmic Pattern
**Self-Join with Aggregation**: Using the table’s relationship with itself to transform a hierarchical link (manager-report) into a filterable group.
