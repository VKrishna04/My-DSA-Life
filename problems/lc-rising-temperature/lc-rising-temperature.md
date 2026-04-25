# Rising Temperature

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-rising-temperature` |
| Topics | Database |
| Solved | 2026-04-25 |
| Runtime | 496 ms (beats 43.17960000000006%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Weather`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.

 

Write a solution to find all dates' `id` with higher temperatures compared to its previous dates (yesterday).

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
**Output:** 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
**Explanation:** 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

## Solutions

### Alt approach (MySQL)

Duplicate resolved — 2 Jun 2025

```MySQL
# Write your MySQL query statement below
select w1.id
from Weather w1
join Weather w2
on Datediff(w1.recordDate, w2.recordDate) = 1
where w1.temperature > w2.temperature
```

## AI Review

### 1. Complexity
*   **Time**: $O(N^2)$ in the worst case. The implicit cross-join (comma syntax) compares every row with every other row before the `WHERE` clause filters them.
*   **Space**: $O(N)$ for the result set, though internal temporary tables for the join may require more.

### 2. Correctness
The logic is **correct**. It accurately handles:
*   **Non-consecutive IDs**: By using `recordDate` instead of `id - 1`.
*   **Missing Dates**: `DATEDIFF(...) = 1` ensures records are only compared if they are exactly one day apart.
*   **Edge Cases**: It correctly ignores the first record (no prior day) and handles negative temperatures.

### 3. Optimization
Use a **Window Function** (`LAG`) available in MySQL 8.0+. This avoids the expensive self-join and processes the data in $O(N \log N)$ time (due to sorting).

```sql
SELECT id 
FROM (
    SELECT id, temperature, recordDate,
           LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
           LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
) t
WHERE temperature > prev_temp 
  AND DATEDIFF(recordDate, prev_date) = 1;
```

### 4. Key Pattern
**Self-Join**: Relating a table to itself to compare values across different rows based on a conditional offset.
