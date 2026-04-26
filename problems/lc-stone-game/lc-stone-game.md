# Stone Game

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-stone-game` |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Solved | 2026-04-26 |
| Runtime | 131 ms (beats 34.77599999999993%) |
| Memory | 25.3 MB (beats 36.44449999999997%) |

## Problem Statement

Alice and Bob play a game with piles of stones. There are an **even** number of piles arranged in a row, and each pile has a **positive** integer number of stones `piles[i]`.

The objective of the game is to end with the most stones. The **total** number of stones across all the piles is **odd**, so there are no ties.

Alice and Bob take turns, with **Alice starting first**. Each turn, a player takes the entire pile of stones either from the **beginning** or from the **end** of the row. This continues until there are no more piles left, at which point the person with the **most stones wins**.

Assuming Alice and Bob play optimally, return `true`_ if Alice wins the game, or _`false`_ if Bob wins_.

 

**Example 1:**

**Input:** piles = [5,3,4,5]
**Output:** true
**Explanation:** 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

**Example 2:**

**Input:** piles = [3,7,2,3]
**Output:** true

 

**Constraints:**

	- `2 <= piles.length <= 500`

	- `piles.length` is **even**.

	- `1 <= piles[i] <= 500`

	- `sum(piles[i])` is **odd**.

## Solutions

```Python3
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[0]*(l) for _ in range(l)]

        psum = [0]
        for pile in piles:
            psum.append(psum[-1]+pile)

        for i in range(l-1, -1, -1):
            for j in range(i+1, l):
                dp[i][j] = max(psum[j+1]-psum[i+1] - dp[i+1][j], psum[j]-psum[i] - dp[i][j-1])
        return True if dp[0][-1] > 0 else False
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(N^2)$ where $N$ is the number of piles, due to the nested loops filling the DP table.
*   **Space:** $O(N^2)$ to store the 2D DP table (the prefix sum array is $O(N)$).

**2. Correctness**
The logic is **correct**. It correctly calculates the maximum relative score for the current player using a bottom-up interval DP approach. Since the problem guarantees an even number of piles and an odd total sum, a tie is impossible, and the first player always has a winning strategy.

**3. Optimization**
*   **Mathematical:** Return `True`. Because the number of piles is even, the first player can force a win by comparing the sum of all even-indexed piles vs. odd-indexed piles and choosing the larger set. This reduces complexity to **$O(1)$ time and space**.
*   **Space (DP):** If restricted to DP, you can reduce space to **$O(N)$** by observing that each state `dp[i][j]` only depends on values from the previous iteration (layer).

**4. Key Algorithmic Pattern**
**Interval Dynamic Programming** (also known as Minimax DP). It builds solutions for smaller subarrays (intervals) to eventually solve for the full array.
