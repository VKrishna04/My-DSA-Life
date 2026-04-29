# Last Stone Weight II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-last-stone-weight-ii::1991232652` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-29 |
| Runtime | 3 ms (beats 95.90809999999999%) |
| Memory | 19.4 MB (beats 64.82410000000002%) |

## Problem Statement

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:

	- If `x == y`, both stones are destroyed, and

	- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is **at most one** stone left.

Return _the smallest possible weight of the left stone_. If there are no stones left, return `0`.

 

**Example 1:**

**Input:** stones = [2,7,4,1,8,1]
**Output:** 1
**Explanation:**
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

**Example 2:**

**Input:** stones = [31,26,33,21,40]
**Output:** 5

 

**Constraints:**

	- `1 <= stones.length <= 30`

	- `1 <= stones[i] <= 100`

## Solutions

```Python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totsum = sum(stones)
        target = totsum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for w in range(target, stone - 1, -1):
                if dp[w] or dp[w-stone]:
                    dp[w] = True
         
        for i in range(len(dp)-1,-1,-1):
            if dp[i]:
                return totsum - 2*i
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \times S)$, where $N$ is the number of stones and $S$ is the total sum of stones (specifically $S/2$).
*   **Space Complexity:** $O(S)$, using a 1D DP array of size `target + 1`.

### 2. Correctness
The code is **correct**. It treats the problem as a variation of the **Partition Problem**, seeking a subset sum closest to half the total weight.
*   **Edge Cases:** It correctly handles single-stone inputs (returns the stone's weight) and cases where an exact half-sum is impossible.
*   **Constraints:** Given LeetCode constraints ($N \le 30$, $\sum \text{stones} \le 3000$), $O(N \times S)$ easily passes within limits.

### 3. Concrete Optimization
Use **Bit Manipulation** (Python's arbitrary-precision integers) to replace the inner loop. This significantly improves performance by processing multiple sums in parallel:

```python
dp = 1  # Bitmask representing reachable sums
for stone in stones:
    dp |= (dp << stone)
# Then find the largest bit set below target
```
This reduces the constant factor of the $O(N \times S)$ time complexity.

### 4. Key Algorithmic Pattern
**0/1 Knapsack / Subset Sum.** 
The problem asks to minimize $|S_1 - S_2|$. Since $S_1 + S_2 = \text{Total}$, minimizing $|(Total - S_2) - S_2|$ is equivalent to maximizing $S_2 \le \text{Total}/2$.
