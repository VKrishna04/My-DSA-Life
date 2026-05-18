# Ones and Zeroes

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-ones-and-zeroes` |
| Topics | Array, String, Dynamic Programming |
| Solved | 2026-05-01 |
| Runtime | 1301 ms (beats 37.17580000000006%) |
| Memory | 19.5 MB (beats 51.2996%) |

## Problem Statement

You are given an array of binary strings `strs` and two integers `m` and `n`.

Return _the size of the largest subset of `strs` such that there are **at most** _`m`_ _`0`_'s and _`n`_ _`1`_'s in the subset_.

A set `x` is a **subset** of a set `y` if all elements of `x` are also elements of `y`.

 

**Example 1:**

**Input:** strs = ["10","0001","111001","1","0"], m = 5, n = 3
**Output:** 4
**Explanation:** The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

**Example 2:**

**Input:** strs = ["10","0","1"], m = 1, n = 1
**Output:** 2
**Explanation:** The largest subset is {"0", "1"}, so the answer is 2.

 

**Constraints:**

	- `1 <= strs.length <= 600`

	- `1 <= strs[i].length <= 100`

	- `strs[i]` consists only of digits `'0'` and `'1'`.

	- `1 <= m, n <= 100`

## Solutions

```Python3
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(len(strs)):
            strs[i] = [strs[i], strs[i].count('0'), strs[i].count('1')]

        for s in strs:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i < s[1] or j < s[2]:
                        continue
                    dp[i][j] = max(dp[i][j], dp[i-s[1]][j-s[2]] + 1)
        
        return dp[-1][-1]
```

## AI Review

1. **Complexity**
   * **Time:** $O(L \cdot (S + m \cdot n))$, where $L$ is the number of strings and $S$ is the average string length.
   * **Space:** $O(m \cdot n)$ to store the DP table.

2. **Correctness**
   The solution is correct. By iterating backwards through $m$ and $n$, it correctly implements the **0/1 Knapsack** logic, ensuring each string is used at most once per subset. It handles edge cases like $m=0, n=0$ or strings consisting entirely of one character.

3. **Optimization**
   Instead of iterating down to $0$ and using a `continue` check, set the loop boundaries to the counts of zeros (`z`) and ones (`o`) in the current string:
   ```python
   for i in range(m, z - 1, -1):
       for j in range(n, o - 1, -1):
           dp[i][j] = max(dp[i][j], dp[i - z][j - o] + 1)
   ```
   This eliminates unnecessary iterations where the string cannot fit, improving performance.

4. **Key Algorithmic Pattern**
   **2D 0/1 Knapsack (Dynamic Programming)** with space optimization (reducing a 3D DP state to 2D by iterating backwards).
