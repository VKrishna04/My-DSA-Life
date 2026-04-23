# Distinct Subsequences

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-distinct-subsequences` |
| Topics | String, Dynamic Programming |
| Solved | 2026-04-23 |
| Runtime | 413 ms (beats 57.34260000000058%) |
| Memory | 75.7 MB (beats 51.401700000000254%) |

## Problem Statement

Given two strings s and t, return _the number of distinct_ **_subsequences_**_ of _s_ which equals _t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

**Example 1:**

**Input:** s = "rabbbit", t = "rabbit"
**Output:** 3
**Explanation:**
As shown below, there are 3 ways you can generate "rabbit" from s.
`**rabb**b**it**`
`**ra**b**bbit**`
`**rab**b**bit**`

**Example 2:**

**Input:** s = "babgbag", t = "bag"
**Output:** 5
**Explanation:**
As shown below, there are 5 ways you can generate "bag" from s.
`**ba**b**g**bag`
`**ba**bgba**g**`
`**b**abgb**ag**`
`ba**b**gb**ag**`
`babg**bag**`

 

**Constraints:**

	- `1 <= s.length, t.length <= 1000`

	- `s` and `t` consist of English letters.

## Solutions

```Python3
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][0] = 1
        
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(M \times N)$, where $M = \text{len}(s)$ and $N = \text{len}(t)$, due to the nested loops filling the table.
*   **Space Complexity:** $O(M \times N)$ to store the 2D DP table.

### 2. Correctness
The logic is **correct**. It accurately implements the recurrence: 
*   If characters match, you can either include `s[i-1]` in the match or skip it.
*   If they don't match, you must skip `s[i-1]`. 
It correctly handles the base case where an empty `t` is a subsequence of any prefix of `s` exactly once.

### 3. Optimization
**Space Optimization:** Since `dp[i][j]` only depends on values from the previous row (`i-1`), you can reduce space complexity to **$O(N)$** using a 1D array. To avoid overwriting values needed for the same row, iterate backwards through `j`:
```python
dp = [1] + [0] * len(t)
for char_s in s:
    for j in range(len(t), 0, -1):
        if char_s == t[j-1]:
            dp[j] += dp[j-1]
```

### 4. Key Algorithmic Pattern
**Dynamic Programming (Bottom-Up)** using a 2D state transition table.
