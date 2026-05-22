# Method Chaining

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-method-chaining` |
| Topics | Sorting, Data Filtering, Vectorization |
| Solved | 2024-10-26 |
| Runtime | 373 ms (beats 5%) |
| Memory | 70.3 MB (beats 9%) |

## Problem Statement

DataFrame `animals`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| species     | object |
| age         | int    |
| weight      | int    |
+-------------+--------+

Write a solution to list the names of animals that weigh **strictly more than** `100` kilograms.

Return the animals sorted by weight in **descending order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
DataFrame animals:
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+
**Output:** 
+----------+
| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
+----------+
**Explanation:** 
All animals weighing more than 100 should be included in the results table.
Tatiana's weight is 464, Jonathan's weight is 463, Tommy's weight is 349, and Alex's weight is 328.
The results should be sorted in descending order of weight.

 

In Pandas, **method chaining** enables us to perform operations on a DataFrame without breaking up each operation into a separate line or creating multiple temporary variables. 

Can you complete this task in just **one line **of code using method chaining?

## Solutions

```Pandas
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(N \log N)$, where $N$ is the number of rows in the DataFrame. Filtering takes $O(N)$, but sorting the filtered results dominates with $O(K \log K)$, where $K \le N$.
*   **Space Complexity:** $O(N)$. Pandas creates intermediate copies during filtering and sorting, requiring memory proportional to the input size.

**2. Correctness**
The code is correct and follows the problem requirements. It handles:
*   **Empty DataFrames:** Returns an empty DataFrame with the column `name`.
*   **No matches:** Returns an empty DataFrame if no weights > 100.
*   **Ties:** `sort_values` handles identical weights by their original index order (stable sort).

**3. Optimization**
If the input DataFrame contains many columns, select only the necessary columns (`name` and `weight`) **before** sorting. This reduces the memory footprint and the amount of data the sorting algorithm must shuffle.
```python
return animals.loc[animals['weight'] > 100, ['name', 'weight']].sort_values('weight', ascending=False)[['name']]
```

**4. Key Algorithmic Pattern**
**Vectorized Operations / Method Chaining:** Utilizing high-level, column-wise operations that are implemented in C/Cython within Pandas rather than explicit Python loops.
