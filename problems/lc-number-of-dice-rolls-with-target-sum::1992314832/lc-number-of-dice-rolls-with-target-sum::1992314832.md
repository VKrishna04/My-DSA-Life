# Number of Dice Rolls With Target Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-number-of-dice-rolls-with-target-sum::1992314832` |
| Topics | Dynamic Programming |
| Solved | 2026-05-01 |
| Runtime | 97 ms (beats 87.0608%) |
| Memory | 19.7 MB (beats 69.4553%) |

## Problem Statement

You have `n` dice, and each dice has `k` faces numbered from `1` to `k`.

Given three integers `n`, `k`, and `target`, return _the number of possible ways (out of the _`kn`_ total ways) __to roll the dice, so the sum of the face-up numbers equals _`target`. Since the answer may be too large, return it **modulo** `109 + 7`.

 

**Example 1:**

**Input:** n = 1, k = 6, target = 3
**Output:** 1
**Explanation:** You throw one die with 6 faces.
There is only one way to get a sum of 3.

**Example 2:**

**Input:** n = 2, k = 6, target = 7
**Output:** 6
**Explanation:** You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

**Example 3:**

**Input:** n = 30, k = 30, target = 500
**Output:** 222616187
**Explanation:** The answer must be returned modulo 109 + 7.

 

**Constraints:**

	- `1 <= n, k <= 30`

	- `1 <= target <= 1000`

## Solutions

```Python3
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        m = (10 ** 9) + 7
        if n*k < target:
            return 0
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(1, target+1):
                for f in range(1, k+1):
                    if j - f < 0:
                        continue
                    dp[i][j] = (dp[i-1][j-f] + dp[i][j]) % m
        return dp[-1][-1]
```

## AI Review

### 1. Complexity
*   **Time:** $O(n \cdot k \cdot \text{target})$ — Three nested loops iterating through dice, target sum, and face values.
*   **Space:** $O(n \cdot \text{target})$ — To store the 2D DP table.

### 2. Correctness
The logic is correct. It properly handles the modulo requirement and includes a pruning condition (`n * k < target`). It correctly builds the solution using the subproblems of previous dice rolls.

### 3. Concrete Optimisation
*   **Space:** Since `dp[i]` only depends on `dp[i-1]`, you can reduce space to **$O(\text{target})$** using a 1D rolling array.
*   **Time:** You can optimize the inner loop to **$O(1)$** using a **sliding window sum** (or prefix sums). Instead of re-summing $k$ elements, calculate $dp[i][j]$ by adding $dp[i-1][j-1]$ and subtracting the oldest element $dp[i-1][j-k-1]$ from a running total. This reduces total time complexity to **$O(n \cdot \text{target})$**.

### 4. Key Algorithmic Pattern
**Dynamic Programming** (specifically the "Bounded Knapsack" or "Ways to Sum" variation).
