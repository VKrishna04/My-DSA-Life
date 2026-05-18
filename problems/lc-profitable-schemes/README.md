# Profitable Schemes

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-profitable-schemes` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-02 |
| Runtime | 597 ms (beats 69.49100000000001%) |
| Memory | 19.7 MB (beats 79.661%) |

## Problem Statement

There is a group of `n` members, and a list of various crimes they could commit. The `ith` crime generates a `profit[i]` and requires `group[i]` members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a **profitable scheme** any subset of these crimes that generates at least `minProfit` profit, and the total number of members participating in that subset of crimes is at most `n`.

Return the number of schemes that can be chosen. Since the answer may be very large, **return it modulo** `109 + 7`.

 

**Example 1:**

**Input:** n = 5, minProfit = 3, group = [2,2], profit = [2,3]
**Output:** 2
**Explanation:** To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.

**Example 2:**

**Input:** n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
**Output:** 7
**Explanation:** To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).

 

**Constraints:**

	- `1 <= n <= 100`

	- `0 <= minProfit <= 100`

	- `1 <= group.length <= 100`

	- `1 <= group[i] <= 100`

	- `profit.length == group.length`

	- `0 <= profit[i] <= 100`

## Solutions

```Python3
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = (10 ** 9) + 7

        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        dp[0][0] = 1

        for k in range(len(group)):
            for i in range(n, group[k]-1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i-group[k]][max(0, j-profit[k])]) % m
        s = 0
        for i in range(n+1):
            s = (s + dp[i][minProfit]) % m
        return s
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(G \cdot N \cdot P)$, where $G$ is the number of available schemes (`len(group)`), $N$ is the member capacity (`n`), and $P$ is the `minProfit`.
*   **Space Complexity:** $O(N \cdot P)$. The code uses a 2D DP table. The third dimension (schemes) is optimized away by iterating backwards.

### 2. Correctness
The code is **correct**. It successfully handles the "at least $minProfit$" requirement by using `max(0, j - profit[k])`, which maps all profits exceeding `minProfit` into the `minProfit` index. It correctly avoids double-counting by iterating through $i$ and $j$ in reverse (standard 0/1 Knapsack optimization).

### 3. Concrete Optimisation
Redefine `dp[i][j]` to represent the number of schemes using **at most** $i$ members. By initializing the entire `dp[0...n][0]` column to 1 (representing the empty set), the transition `dp[i][j] = (dp[i][j] + dp[i-group[k]][max(0, j-profit[k])])` will automatically accumulate valid schemes. This allows you to return `dp[n][minProfit]` directly, removing the $O(N)$ summation loop at the end.

### 4. Key Algorithmic Pattern
**0/1 Knapsack (Dynamic Programming)** with multiple constraints (members and profit) and space optimization.
