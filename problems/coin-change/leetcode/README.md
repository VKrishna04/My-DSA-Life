# Coin Change

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-coin-change` |
| Topics | Array, Dynamic Programming, Breadth-First Search |
| Solved | 2025-09-21 |
| Runtime | 1245 ms (beats 7.211500000000692%) |
| Memory | 18.1 MB (beats 100%) |

## Problem Statement

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

 

**Example 1:**

**Input:** coins = [1,2,5], amount = 11
**Output:** 3
**Explanation:** 11 = 5 + 5 + 1

**Example 2:**

**Input:** coins = [2], amount = 3
**Output:** -1

**Example 3:**

**Input:** coins = [1], amount = 0
**Output:** 0

 

**Constraints:**

	- `1 <= coins.length <= 12`

	- `1 <= coins[i] <= 231 - 1`

	- `0 <= amount <= 104`

## Solutions

```Python3
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for curr_amt in range(1,amount+1):
            for coin in coins:
                if curr_amt - coin >= 0 and dp[curr_amt - coin] != float('inf'):
                    dp[curr_amt] = min(dp[curr_amt], 1 + dp[curr_amt - coin])
        
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

        # if amount == 0:
        #     return 0
        # count = 0
        # coins.sort(reverse=True)

        # for i in coins:
        #     print(f"coin -> {i}")
        #     while i <= amount:
        #         count += 1
        #         print(f"  amount -> {amount}, new amount -> {amount - i}")
        #         amount -= i
        # if count == 0 or amount != 0:
        #     return -1
        # return count
```

## AI Review

### Review of Coin Change Solution

**1. Complexity**
*   **Time Complexity:** $O(S \cdot n)$, where $S$ is the `amount` and $n$ is the number of `coins`. We iterate through every amount up to $S$ for every coin.
*   **Space Complexity:** $O(S)$ to store the `dp` array.

**2. Correctness**
The implementation is **correct**. It properly initializes the base case (`dp[0] = 0`), handles unreachable amounts using `float('inf')`, and correctly returns `-1` if no solution exists. It avoids the "Greedy" pitfall (shown in your commented-out code) which fails on cases like `coins=[1, 3, 4], amount=6`.

**3. Optimization**
Swap the loop order and adjust the range to eliminate the conditional check:
```python
for coin in coins:
    for curr_amt in range(coin, amount + 1):
        dp[curr_amt] = min(dp[curr_amt], dp[curr_amt - coin] + 1)
```
This reduces the number of operations by starting the inner loop only where `curr_amt - coin` is valid and improves cache locality.

**4. Key Algorithmic Pattern**
**Dynamic Programming (Iterative, Bottom-Up)**. Specifically, this is a variation of the **Unbounded Knapsack Problem**, where items (coins) can be reused infinitely to reach a target value.
