# Article Views I

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-article-views-i` |
| Topics | Database |
| Solved | 2026-04-24 |
| Runtime | 404 ms (beats 67.95760000000003%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Views`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

 

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
**Output:** 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+

## Solutions

```MySQL
# Write your MySQL query statement below
select distinct author_id as id
from Views
where author_id = viewer_id
order by id ASC
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \log N)$, where $N$ is the number of rows in the `Views` table. While filtering is $O(N)$, the `DISTINCT` and `ORDER BY` operations require sorting or hashing the result set.
*   **Space Complexity:** $O(N)$ in the worst case to store unique IDs before returning the result.

### 2. Correctness
The solution is **correct**. It accurately filters rows where authors view their own work and ensures results are unique and sorted as per the requirements.
*   **Edge Cases:** Handled correctly. Multiple self-views by the same author are collapsed by `DISTINCT`. If the table is empty, it returns an empty result set.

### 3. Concrete Optimization
Add a **composite index** on `(author_id, viewer_id)`.
This allows the database to perform an **index-only scan**. The engine can identify matching rows directly from the index tree without fetching the full rows from the disk, significantly improving performance on large datasets.

### 4. Key Algorithmic Pattern
**Filtering and Deduplication**: The query uses a predicate (`WHERE`) to subset the data followed by a set-based operation (`DISTINCT`) to ensure element uniqueness.
