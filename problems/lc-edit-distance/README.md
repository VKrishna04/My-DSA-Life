# Edit Distance

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-edit-distance` |
| Topics | String, Dynamic Programming |
| Solved | 2026-04-23 |
| Runtime | 44 ms (beats 68.51529999999998%) |
| Memory | 22.7 MB (beats 49.20859999999996%) |

## Problem Statement

Given two strings `word1` and `word2`, return _the minimum number of operations required to convert `word1` to `word2`_.

You have the following three operations permitted on a word:

	- Insert a character

	- Delete a character

	- Replace a character

 

**Example 1:**

**Input:** word1 = "horse", word2 = "ros"
**Output:** 3
**Explanation:** 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

**Example 2:**

**Input:** word1 = "intention", word2 = "execution"
**Output:** 5
**Explanation:** 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

 

**Constraints:**

	- `0 <= word1.length, word2.length <= 500`

	- `word1` and `word2` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(1,len(word1)+1):
            dp[i][0] = i
        
        for j in range(1, len(word2)+1):
            dp[0][j] = j

        for i in range(1,len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        return dp[-1][-1]
```

## AI Review

### 1. Complexity
*   **Time:** $O(M \times N)$, where $M$ and $N$ are the lengths of `word1` and `word2`. We iterate through every cell in the $(M+1) \times (N+1)$ matrix.
*   **Space:** $O(M \times N)$ to store the 2D DP table.

### 2. Correctness
The code is **correct**. It accurately implements the Levenshtein distance algorithm.
*   **Edge Cases:** It correctly handles empty strings (e.g., if `word1` is empty, it returns `len(word2)` via the base case initialization).
*   **Logic:** The transitions for insertion, deletion, and substitution are correctly handled in the `else` block.

### 3. Optimization
**Space Complexity:** The current row `dp[i]` only depends on the previous row `dp[i-1]` and the current row's previous element. You can optimize space to **$O(\min(M, N))$** by using a single 1D array (and one variable to store the "top-left" diagonal value) instead of a full 2D matrix.

### 4. Key Algorithmic Pattern
**Dynamic Programming (Bottom-Up):** It solves the global problem by building up solutions to subproblems (prefixes of the strings) and storing them in a table to avoid redundant computations.
