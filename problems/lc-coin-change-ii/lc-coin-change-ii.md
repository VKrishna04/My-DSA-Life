# Coin Change II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-coin-change-ii` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-01 |
| Runtime | 247 ms (beats 64.87330000000003%) |
| Memory | 19.4 MB (beats 83.96980000000002%) |

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the number of combinations that make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.

 

**Example 1:**

**Input:** amount = 5, coins = [1,2,5]
**Output:** 4
**Explanation:** there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

**Example 2:**

**Input:** amount = 3, coins = [2]
**Output:** 0
**Explanation:** the amount of 3 cannot be made up just with coins of 2.

**Example 3:**

**Input:** amount = 10, coins = [10]
**Output:** 1

 

**Constraints:**

	- `1 <= coins.length <= 300`

	- `1 <= coins[i] <= 5000`

	- All the values of `coins` are **unique**.

	- `0 <= amount <= 5000`

## Solutions

```Python3
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] += dp[i-coin]
        return dp[-1]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \times A)$, where $N$ is the number of coins and $A$ is the target amount. We iterate through every coin for every possible amount.
*   **Space Complexity:** $O(A)$ to maintain the 1D `dp` array.

### 2. Correctness
The code is **correct** and handles standard edge cases well:
*   **Amount = 0:** Correctly returns `1` (one way to make zero: use no coins).
*   **Impossible Amount:** Correctly returns `0` if no combinations exist.
*   **Ordering:** By iterating through coins in the outer loop, it ensures we count **combinations** (e.g., `[1, 2]`) rather than permutations (e.g., `[1, 2]` and `[2, 1]`).

### 3. Concrete Optimisation
You can eliminate the conditional `if i >= coin` check inside the inner loop by starting the range at `coin` itself. This reduces unnecessary iterations and branching:
```python
for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] += dp[i - coin]
```

### 4. Key Algorithmic Pattern
**Dynamic Programming (Unbounded Knapsack variant).** This solution uses a space-optimized 1D array to track the number of ways to reach each sub-sum, building the solution bottom-up.
