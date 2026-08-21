# Number Of Coins

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-number-of-coins1824` |
| Topics | Dynamic Programming, Array, Sorting |
| Solved | 2026-06-24 |

## Problem Statement

You are given an array **coins[]**, where each element represents a coin of a **different** denomination, and a target value **sum**. You have an **unlimited** supply of each coin type. Your task is to determine the **minimum** number of coins needed to obtain the target **sum**. If it is **not** possible to form the sum using the given coins, return **-1**.

**Examples:**

**Input:** coins[] = [25, 10, 5], sum = 30
**Output:** 2
**Explanation:** Minimum 2 coins needed, 25 and 5  
**Input:** coins[] = [9, 6, 5, 1], sum = 19
**Output: **3
**Explanation:** 19 = 9 + 9 + 1
**Input:** coins[] = [5, 1], sum = 0
**Output: **0
**Explanation:** For 0 sum, we do not need a coin
**Input:** coins[] = [4, 6, 2], sum = 5
**Output: **-1
**Explanation:** Not possible to make the given sum.
**Constraints:**
1 &le; sum * coins.size() &le; 106
0 &le; sum &le; 104
1 &le; coins[i] &le; 104
1 &le; coins.size() &le; 103

## Solutions

```python3
class Solution:
    def minCoins(self, coins, sum):
        coins.sort()
        dp = [0] * (sum + 1)
        
        for i in range(1, sum+1):
            dp[i] = float('inf')
            
            for coin in coins:
                diff = i  - coin
                if diff < 0:
                    break
                dp[i] = min(dp[i], dp[diff] + 1)
        
        if dp[sum] != float('inf'):
            return dp[sum]
        return -1
```

## AI Review

1. **Complexity**:
*   **Time**: $O(S \cdot N + N \log N)$, where $S$ is the target sum and $N$ is the number of coin denominations.
*   **Space**: $O(S)$ for the DP array. This is the optimal space for this problem.

2. **Correctness**:
The logic is robust. It correctly handles the edge case of `sum = 0` (returns 0) and unreachable sums (returns -1). One minor vulnerability: if the `coins` list contains duplicates (e.g., `[1, 1, 2]`), the inner loop performs redundant calculations.

3. **Optimization**:
To improve performance, convert `coins` to a set before sorting: `coins = sorted(set(coins))`. This prevents the inner loop from re-processing the same denomination, which is a common bottleneck when the input array is messy.

4. **Key Pattern**:
**Bottom-up Dynamic Programming** (specifically the **Unbounded Knapsack** variation). You solve every sub-sum from 1 to `sum` and use those results to build the final answer.
