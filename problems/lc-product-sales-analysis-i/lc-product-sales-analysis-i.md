# Product Sales Analysis I

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-product-sales-analysis-i` |
| Topics | Database |
| Solved | 2026-04-25 |
| Runtime | 1254 ms (beats 46.85979999999998%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Sales`

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to `Product` table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.

 

Table: `Product`

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.

 

Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.

Return the resulting table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
**Output:** 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
**Explanation:** 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.

## Solutions

```MySQL
# Write your MySQL query statement below
select p.product_name, s.year, s.price
from sales as s
left join product as p
on s.product_id = p.product_id

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \log M)$ on average, where $N$ is the number of rows in the `Sales` table and $M$ is the number of rows in the `Product` table, assuming an index exists on `Product.product_id`.
*   **Space Complexity:** $O(N)$ to store and return the result set.

### 2. Correctness
The solution is **correct**. It accurately retrieves the required columns.
*   **Edge Case:** If a `product_id` exists in `Sales` but is missing from the `Product` table, `LEFT JOIN` will return the sale with a `NULL` product name. Given the problem constraints, every `product_id` typically exists, but `LEFT JOIN` is the safer approach for data integrity.

### 3. Optimization
Use **`INNER JOIN`** instead of `LEFT JOIN`. 
Since the schema implies every sale must be associated with a valid product, an `INNER JOIN` is generally more performant. It allows the database optimizer more flexibility in choosing the join order and avoids processing potential `NULL` matches.

### 4. Key Algorithmic Pattern
**Relational Join (Equi-join):** This pattern combines rows from two tables based on a matching column value (`product_id`) to aggregate attributes from disparate entities into a single flat result.
