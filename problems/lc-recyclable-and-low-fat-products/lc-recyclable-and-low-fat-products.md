# Recyclable and Low Fat Products

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-recyclable-and-low-fat-products` |
| Topics | Database |
| Solved | 2026-04-24 |
| Runtime | 627 ms (beats 13.064299999999964%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Products`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

 

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
**Output:** 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
**Explanation:** Only products 1 and 3 are both low fat and recyclable.

## Solutions

```MySQL
# Write your MySQL query statement below
select product_id
from Products as p
where p.low_fats = 'Y' and p.recyclable = 'Y';
```

## AI Review

### 1. Complexity
*   **Time Complexity:** **$O(N)$**, where $N$ is the number of rows in the table. Without an index, the engine must perform a full table scan.
*   **Space Complexity:** **$O(N)$** in the worst case to store and return the result set if every product meets the criteria.

### 2. Correctness
The logic is correct for the problem constraints.
*   **Edge Cases:** 
    *   **NULLs:** If either column contains `NULL`, that row is correctly excluded because `NULL = 'Y'` evaluates to `UNKNOWN`.
    *   **Case Sensitivity:** Depending on the database collation (e.g., `_bin` vs `_ci`), `'y'` might not match `'Y'`. Standard LeetCode environments are usually case-insensitive.

### 3. Optimization
Add a **composite index** on `(low_fats, recyclable)`. This allows the database to perform an index scan or seek instead of a full table scan, significantly improving performance on large datasets.

### 4. Key Algorithmic Pattern
**Selection (Filtering):** The primary pattern is the use of a predicate (`WHERE` clause) to filter rows from a relation based on logical conjunction (`AND`).
