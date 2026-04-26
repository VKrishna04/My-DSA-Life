# Stone Game VII

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-stone-game-vii` |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Solved | 2026-04-26 |
| Runtime | 1386 ms (beats 91.15609999999997%) |
| Memory | 42.9 MB (beats 62.58509999999998%) |

## Problem Statement

Alice and Bob take turns playing a game, with **Alice starting first**.

There are `n` stones arranged in a row. On each player's turn, they can **remove** either the leftmost stone or the rightmost stone from the row and receive points equal to the **sum** of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to **minimize the score's difference**. Alice's goal is to **maximize the difference** in the score.

Given an array of integers `stones` where `stones[i]` represents the value of the `ith` stone **from the left**, return _the **difference** in Alice and Bob's score if they both play **optimally**._

 

**Example 1:**

**Input:** stones = [5,3,1,4,2]
**Output:** 6
**Explanation:** 
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.

**Example 2:**

**Input:** stones = [7,90,5,1,100,10,10,2]
**Output:** 122

 

**Constraints:**

	- `n == stones.length`

	- `2 <= n <= 1000`

	- `1 <= stones[i] <= 1000`

## Solutions

```Python3
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        l = len(stones)
        dp = [[0]*(l) for _ in range(l)]
        psum = [0]
        for stone in stones:
            psum.append(psum[-1]+stone)
        for i in range(l-1, -1,-1):
            for j in range(i+1,l):
                dp[i][j] = max(psum[j+1]-psum[i+1]-dp[i+1][j], psum[j]-psum[i]-dp[i][j-1])
        return dp[0][-1]

```

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time Complexity**: $O(N^2)$, where $N$ is the number of stones. The nested loops iterate through all possible subarrays.
    *   **Space Complexity**: $O(N^2)$ to store the 2D `dp` table.

2.  **Correctness**: 
    The solution is correct. It effectively uses **Prefix Sums** to calculate subarray totals in $O(1)$ and a **Bottom-Up DP** to determine the maximum relative score difference. It handles the base case (single stone, score 0) implicitly and works for the constraint $N \le 1000$. No edge cases (like $N=2$) fail.

3.  **Optimization**: 
    **Space Optimization**: The current row `i` only depends on values from the same row and the row `i+1`. You can reduce space complexity to **$O(N)$** by using a 1D array and updating it in place:
    ```python
    dp = [0] * l
    for i in range(l - 1, -1, -1):
        for j in range(i + 1, l):
            dp[j] = max(psum[j+1] - psum[i+1] - dp[j], psum[j] - psum[i] - dp[j-1])
    ```

4.  **Key Algorithmic Pattern**: 
    **Interval Dynamic Programming** (commonly used for optimal play/minimax game theory problems).
