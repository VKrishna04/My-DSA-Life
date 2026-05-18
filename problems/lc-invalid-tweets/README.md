# Invalid Tweets

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-invalid-tweets` |
| Topics | Database |
| Solved | 2026-04-24 |
| Runtime | 826 ms (beats 6.892700000000084%) |
| Memory | 0B (beats 100%) |

## Problem Statement

Table: `Tweets`

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.

 

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is **strictly greater** than `15`.

Return the result table in **any order**.

The result format is in the following example.

 

**Example 1:**

**Input:** 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
**Output:** 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
**Explanation:** 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.

## Solutions

```MySQL
# Write your MySQL query statement below
select tweet_id
from Tweets
where char_length(content) > 15
```

## AI Review

### Review of "Invalid Tweets" Solution

**1. Complexity**
*   **Time Complexity:** $O(N)$, where $N$ is the number of rows in the `Tweets` table. Each row must be scanned once to calculate the string length.
*   **Space Complexity:** $O(N)$ in the worst case to store/return the result set; $O(1)$ auxiliary space.

**2. Correctness**
The solution is **correct**. 
*   It uses `char_length()`, which counts characters rather than bytes. This is crucial for multi-byte characters (e.g., emojis or non-English scripts) where `length()` would return a higher byte count and potentially produce incorrect results.
*   **Edge Cases:** Handles empty strings ($0 > 15$ is false) and strings of exactly 15 characters ($15 > 15$ is false) correctly.

**3. Optimisation**
For large datasets, functions in `WHERE` clauses prevent the use of standard indexes (SARGability). 
*   **Concrete Optimisation:** Add a **Generated Column** that stores the character length and index it:
    ```sql
    ALTER TABLE Tweets ADD content_len INT AS (CHAR_LENGTH(content)) VIRTUAL;
    CREATE INDEX idx_len ON Tweets(content_len);
    ```
    Then query: `WHERE content_len > 15;`

**4. Key Algorithmic Pattern**
*   **Filtering (Selection):** Utilizing a predicate logic to filter rows based on a computed property of a column.
