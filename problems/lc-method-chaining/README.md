# Method Chaining

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-method-chaining` |
| Topics | Data Manipulation, Sorting, Pandas |
| Solved | 2024-10-26 |
| Runtime | 373 ms (beats 5.073700000000015%) |
| Memory | 70.3 MB (beats 8.823500000000028%) |

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

```Python
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
```

## AI Review

### Review
**1. Complexity**
*   **Time:** $O(N \log N)$, where $N$ is the number of rows. Filtering takes $O(N)$, but sorting the filtered results dominates the time complexity.
*   **Space:** $O(N)$. Pandas creates intermediate copies of the DataFrame during filtering and sorting operations.

**2. Correctness**
The solution is correct. It filters rows first, sorts the subset, and finally projects only the required `'name'` column. It handles cases where no animals meet the criteria (returning an empty DataFrame) correctly.

**3. Optimization**
While method chaining is readable, you can slightly improve memory efficiency by using `loc` to perform filtering and column selection in fewer steps, though `weight` must remain until after the sort:
```python
return animals.loc[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]
```
For extremely large datasets, using `sort_values(inplace=False)` is standard, but the current approach is idiomatic for LeetCode's pandas track.

**4. Key Algorithmic Pattern**
**Vectorized Operations / Method Chaining:** Utilizing high-level library functions to perform bulk operations on data structures without explicit loops.
