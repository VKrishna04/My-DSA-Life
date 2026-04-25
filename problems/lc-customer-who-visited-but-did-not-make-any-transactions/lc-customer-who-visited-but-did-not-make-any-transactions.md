# Customer Who Visited but Did Not Make Any Transactions

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-customer-who-visited-but-did-not-make-any-transactions` |
| Topics | Database |
| Solved | 2026-04-25 |
| Runtime | 1440 ms (beats 30.05969999999979%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Visits`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| visit_id    | int     |
| customer_id | int     |
+-------------+---------+
visit_id is the column with unique values for this table.
This table contains information about the customers who visited the mall.

 

Table: `Transactions`

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| transaction_id | int     |
| visit_id       | int     |
| amount         | int     |
+----------------+---------+
transaction_id is column with unique values for this table.
This table contains information about the transactions made during the visit_id.

 

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the result table sorted in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Visits
+----------+-------------+
| visit_id | customer_id |
+----------+-------------+
| 1        | 23          |
| 2        | 9           |
| 4        | 30          |
| 5        | 54          |
| 6        | 96          |
| 7        | 54          |
| 8        | 54          |
+----------+-------------+
Transactions
+----------------+----------+--------+
| transaction_id | visit_id | amount |
+----------------+----------+--------+
| 2              | 5        | 310    |
| 3              | 5        | 300    |
| 9              | 5        | 200    |
| 12             | 1        | 910    |
| 13             | 2        | 970    |
+----------------+----------+--------+
**Output:** 
+-------------+----------------+
| customer_id | count_no_trans |
+-------------+----------------+
| 54          | 2              |
| 30          | 1              |
| 96          | 1              |
+-------------+----------------+
**Explanation:** 
Customer with id = 23 visited the mall once and made one transaction during the visit with id = 12.
Customer with id = 9 visited the mall once and made one transaction during the visit with id = 13.
Customer with id = 30 visited the mall once and did not make any transactions.
Customer with id = 54 visited the mall three times. During 2 visits they did not make any transactions, and during one visit they made 3 transactions.
Customer with id = 96 visited the mall once and did not make any transactions.
As we can see, users with IDs 30 and 96 visited the mall one time without making any transactions. Also, user 54 visited the mall twice and did not make any transactions.

## Solutions

```MySQL
# Write your MySQL query statement below
select v.customer_id, COUNT(v.visit_id) as count_no_trans
from visits as v
left join transactions as t
on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(V + T)$ where $V$ is the number of visits and $T$ is the number of transactions, assuming an index exists on `visit_id`. Without indices, it defaults to $O(V \times T)$ for a nested-loop join.
*   **Space:** $O(V)$ to store intermediate join results and the hash map for grouping.

**2. Correctness**
The solution is **correct**. It properly identifies visits without corresponding transactions using the "Left Join where Null" logic.
*   **Edge Cases:** Multiple transactions for the same visit are correctly excluded. Customers with only successful transactions are correctly omitted.

**3. Optimization**
Use `NOT IN` or `NOT EXISTS` instead of a `LEFT JOIN`. In many SQL engines, `NOT EXISTS` is more efficient for anti-joins because it can "short-circuit" (stop searching as soon as one matching transaction is found) and avoids the overhead of constructing a large intermediate joined table.

```sql
SELECT customer_id, COUNT(*) as count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;
```

**4. Key Algorithmic Pattern**
**Anti-Join:** A technique used to return rows from the first table that have no matches in the second table.
