# Number of Dice Rolls With Target Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-number-of-dice-rolls-with-target-sum` |
| Topics | Dynamic Programming |
| Solved | 2026-05-03 |
| Runtime | 29 ms (beats 69.79129999999994%) |
| Memory | 56.6 MB (beats 74.99989999999998%) |

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

```JavaScript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
var numRollsToTarget = function(n, k, target) {
    const MOD = 1000000007;
    let dp = new Array(target + 1).fill(0);
    dp[0] = 1;

    for (let i = 1; i <= n; i++) {
        let nextDp = new Array(target + 1).fill(0);
        for (let j = 1; j <= target; j++) {
            for (let face = 1; face <= k; face++) {
                if (j >= face) {
                    nextDp[j] = (nextDp[j] + dp[j - face]) % MOD;
                }
            }
        }
        dp = nextDp;
    }

    return dp[target];
};
```

## AI Review

1. **Complexity**:
   * **Time**: $O(n \cdot target \cdot k)$ due to three nested loops.
   * **Space**: $O(target)$ as it only stores the current and previous DP states.

2. **Correctness**:
   The solution is correct and handles the $10^9+7$ modulo requirement. It correctly manages the base case ($dp[0]=1$ for 0 dice) and edge cases like `target > n * k` (returns 0) or `target < n` (returns 0).

3. **Optimization**:
   The innermost loop calculates a range sum: `nextDp[j] = sum(dp[j-k ... j-1])`. This can be optimized using a **Sliding Window** or **Prefix Sums**. Instead of re-summing $k$ elements, you can maintain a running sum of the previous `dp` array. This reduces the time complexity to **$O(n \cdot target)$**.

4. **Key Algorithmic Pattern**:
   **Dynamic Programming (Iterative)** with **Space Optimization** (Rolling Array/Two-Row DP). It builds the solution for $i$ dice based on the results of $i-1$ dice.
