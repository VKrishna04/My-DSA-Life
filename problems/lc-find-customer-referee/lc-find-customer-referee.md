# Find Customer Referee

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-customer-referee` |
| Topics | Database |
| Solved | 2026-04-24 |
| Runtime | 485 ms (beats 45.880900000000054%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Customer`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

 

Find the names of the customer that are either:

	- **referred by** any customer with `id != 2`.

	- **not referred by** any customer.

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
**Output:** 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

## Solutions

```MySQL
# Write your MySQL query statement below
select name
from Customer
where referee_id!=2 or referee_id is NULL
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows in the `Customer` table. The database must perform a full table scan to evaluate each row against the predicate.
*   **Space Complexity:** $O(N)$ in the worst case for the result set, though no additional intermediate data structures are created.

### 2. Correctness
The solution is **correct**. 
*   **Edge Case:** In SQL, `NULL` represents an unknown value. Comparisons like `referee_id != 2` result in `UNKNOWN` rather than `TRUE` for `NULL` entries. 
*   By explicitly adding `OR referee_id IS NULL`, you correctly capture customers who have no referee, which is the primary pitfall of this problem.

### 3. Optimization
Use **`IFNULL`** or **`COALESCE`** for cleaner syntax:
```sql
SELECT name FROM Customer WHERE IFNULL(referee_id, 0) != 2;
```
*Note: While cleaner, the original `OR` syntax is often more "SARGable" (Search Argumentable), allowing the optimizer to use indexes more effectively than when wrapping columns in functions.*

### 4. Key Algorithmic Pattern
**Three-Valued Logic Handling:** This pattern addresses SQL’s logic system (True, False, Unknown) specifically regarding `NULL` values in filtering predicates.
