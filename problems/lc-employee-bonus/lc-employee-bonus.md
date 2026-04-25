# Employee Bonus

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-employee-bonus` |
| Topics | Database |
| Solved | 2026-04-25 |
| Runtime | 878 ms (beats 90.43090000000005%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Employee`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.

 

Table: `Bonus`

+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.

 

Write a solution to report the name and bonus amount of each employee who satisfies either of the following:

	- The employee has a bonus **less than** `1000`.

	- The employee did not get any bonus.

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
**Output:** 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+

## Solutions

```MySQL
# Write your MySQL query statement below
select e.name, b.bonus
from employee as e
left join bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is Null
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N + M)$, where $N$ is the number of employees and $M$ is the number of bonus records. This assumes an index exists on `empId`.
*   **Space:** $O(N)$ to store and return the result set.

**2. Correctness**
The solution is **correct**. It properly uses a `LEFT JOIN` to include employees missing from the `Bonus` table and uses the `OR b.bonus IS NULL` condition to capture them, satisfying the requirement for bonuses less than 1000 or no bonus at all.

**3. Optimization**
Ensure there is an **index** on `empId` in both tables. From a syntax perspective, using `COALESCE` can make the logic more concise:
```sql
WHERE COALESCE(b.bonus, 0) < 1000
```
*Note: In some SQL engines, `OR` is generally more index-friendly than `COALESCE`, so the current implementation is already highly efficient for standard execution.*

**4. Key Algorithmic Pattern**
**Left Outer Join with Null Handling**: Using a left join to preserve all rows from the "left" table and filtering for `NULL` values to handle missing relationships.
