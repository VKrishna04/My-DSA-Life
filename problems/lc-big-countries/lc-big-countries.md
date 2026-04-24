# Big Countries

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-big-countries` |
| Topics | Database |
| Solved | 2026-04-24 |
| Runtime | 275 ms (beats 85.38039999999995%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `World`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

 

A country is **big** if:

	- it has an area of at least three million (i.e., `3000000 km2`), or

	- it has a population of at least twenty-five million (i.e., `25000000`).

Write a solution to find the name, population, and area of the **big countries**.

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
**Output:** 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+

## Solutions

```MySQL
# Write your MySQL query statement below
select name, population, area
from World
where area >= 3000000 or population >= 25000000
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows in the `World` table. Each row must be evaluated against the filter criteria.
*   **Space Complexity:** $O(1)$ auxiliary space (excluding the space required for the output).

### 2. Correctness
The code is **correct** and handles the logical "OR" requirement defined in the problem. 
*   **Edge Cases:** It correctly includes countries that meet *both* criteria simultaneously. Null values in `area` or `population` would result in a `FALSE` evaluation for that specific condition, which is standard behavior.

### 3. Concrete Optimization
Use **`UNION`** instead of `OR`. 
In many SQL engines, an `OR` condition can prevent the optimizer from using indexes efficiently, leading to a full table scan. `UNION` allows the engine to use separate indexes on `area` and `population` independently.

**Optimized Code:**
```sql
SELECT name, population, area FROM World WHERE area >= 3000000
UNION
SELECT name, population, area FROM World WHERE population >= 25000000;
```

### 4. Key Algorithmic Pattern
**Filtering (Selection):** Utilizing a declarative predicate (`WHERE` clause) to filter a dataset based on logical conditions.
