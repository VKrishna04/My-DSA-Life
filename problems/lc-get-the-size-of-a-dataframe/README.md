# Get the Size of a DataFrame

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-get-the-size-of-a-dataframe` |
| Topics | Pandas, Data Science, Metadata Extraction |
| Solved | 2024-10-23 |
| Runtime | 356 ms (beats 5.158100000000085%) |
| Memory | 68.8 MB (beats 12.715000000000003%) |

## Problem Statement

DataFrame `players:`
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+

Write a solution to calculate and display the **number of rows and columns** of `players`.

Return the result as an array:

`[number of rows, number of columns]`

The result format is in the following example.

 

**Example 1:**

**Input:
**+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+**
Output:
**[10, 5]
**Explanation:**
This DataFrame contains 10 rows and 5 columns.

## Hints

<details>
<summary>Hint 1</summary>

Consider using a built-in function in pandas library to get the size of a DataFrame.

</details>

## Solutions

```Python
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
```

## AI Review

### Code Review

**1. Complexity**
*   **Time Complexity:** $O(1)$. Accessing the `.shape` attribute is a constant-time operation in Pandas as it is stored as metadata.
*   **Space Complexity:** $O(1)$. The function only allocates a fixed-size list containing two integers, regardless of the DataFrame's size.

**2. Correctness**
The solution is correct and idiomatic. 
*   **Edge Cases:** It correctly handles empty DataFrames (e.g., returning `[0, 0]` or `[0, n]`) and DataFrames with single rows or columns.
*   **Note:** In some environments, you might need to import `List` from `typing`, though modern Python (3.9+) and LeetCode's environment usually handle `list` or pre-imported `List` automatically.

**3. Optimization**
There are no performance optimizations possible as this is the most direct way to access DataFrame dimensions. Syntactically, using `list(players.shape)` is cleaner than manually indexing the tuple.

**4. Key Algorithmic Pattern**
**Metadata Retrieval**: This pattern involves accessing pre-calculated properties of a data structure rather than iterating through the elements to count them.
