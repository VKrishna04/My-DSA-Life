# Average Time of Process per Machine

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-average-time-of-process-per-machine` |
| Topics | Database |
| Solved | 2026-04-25 |
| Runtime | 243 ms (beats 65.0007%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Activity`

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM (category) of type ('start', 'end').
timestamp is a float representing the current time in seconds.
'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.

 

There is a factory website that has several machines each running the **same number of processes**. Write a solution to find the **average time** each machine takes to complete a process.

The time to complete a process is the `'end' timestamp` minus the `'start' timestamp`. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the `machine_id` along with the **average time** as `processing_time`, which should be **rounded to 3 decimal places**.

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+
**Output:** 
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+
**Explanation:** 
There are 3 machines running 2 processes each.
Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456

## Solutions

```MySQL
# Write your MySQL query statement below
select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time
from Activity as a1
left join Activity as a2
on a1.machine_id = a2.machine_id and a1.process_id=a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id
```

## AI Review

### Review: Average Time of Process per Machine

**1. Complexity**
*   **Time Complexity:** $O(N^2)$ in the worst case for a self-join without optimal indexing, though typically $O(N \log N)$ with indexes.
*   **Space Complexity:** $O(N)$ to store the intermediate joined table and grouping results.

**2. Correctness**
The logic is **correct**. By filtering `a1.activity_type='start'` and `a2.activity_type='end'` within the `ON` clause, you isolate the duration. Note: Using `LEFT JOIN` here includes rows where `a1` is 'end' (resulting in `NULL` processing times); while `AVG()` ignores `NULL`s, an `INNER JOIN` or `WHERE` clause is more standard to avoid processing redundant rows.

**3. Optimization**
Use **Conditional Aggregation** to calculate the result in a **single pass** ($O(N)$ time) without a self-join:
```sql
SELECT machine_id, 
    ROUND(SUM(CASE WHEN activity_type = 'end' THEN timestamp ELSE -timestamp END) / COUNT(DISTINCT process_id), 3) AS processing_time
FROM Activity
GROUP BY machine_id;
```
This avoids the overhead of duplicating data in memory.

**4. Key Algorithmic Pattern**
**Self-Join:** Joining a table to itself to compare or combine different rows (start vs. end events) belonging to the same entity (process/machine).
