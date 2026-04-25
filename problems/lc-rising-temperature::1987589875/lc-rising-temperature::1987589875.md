# Rising Temperature

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-rising-temperature::1987589875` |
| Topics | Database |
| Solved | 2026-04-25 |
| Runtime | 496 ms (beats 46.51449999999994%) |
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

```MySQL
# Write your MySQL query statement below
select w.id
from Weather as w, weather as v
where DATEDIFF(w.recordDate, v.recordDate) = 1 and w.temperature > v.temperature

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N^2)$ in the worst case. Without an explicit join condition or index, the database may perform a Cartesian product before filtering.
*   **Space Complexity:** $O(N)$ to store the result set.

### 2. Correctness
The solution is **correct**. `DATEDIFF(w.recordDate, v.recordDate) = 1` accurately identifies records exactly one day apart, even if the primary keys are not sequential or if there are gaps in the calendar. It correctly handles the requirement to compare "yesterday's" temperature.

### 3. Concrete Optimization
Use an **Explicit Inner Join** and ensure an **index** exists on `recordDate`. While modern optimizers might treat your comma-join similarly, an explicit join is clearer. For MySQL 8.0+, using `LAG()` is more efficient ($O(N \log N)$ due to sorting):

```sql
SELECT id FROM (
    SELECT id, temperature, recordDate,
    LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
    LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
) t
WHERE temperature > prev_temp AND DATEDIFF(recordDate, prev_date) = 1;
```

### 4. Key Algorithmic Pattern
**Self-Join:** The table is joined with itself to compare rows within the same dataset based on a relative offset (time).
