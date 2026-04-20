# Frog Jump

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-frog-jump` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-20 |
| Runtime | 98 ms (beats 59.85990000000009%) |
| Memory | 21 MB (beats 80.89000000000003%) |

## Problem Statement

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of `stones` positions (in units) in sorted **ascending order**, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be `1` unit.

If the frog's last jump was `k` units, its next jump must be either `k - 1`, `k`, or `k + 1` units. The frog can only jump in the forward direction.

 

**Example 1:**

**Input:** stones = [0,1,3,5,6,8,12,17]
**Output:** true
**Explanation:** The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

**Example 2:**

**Input:** stones = [0,1,2,3,4,8,9,11]
**Output:** false
**Explanation:** There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

 

**Constraints:**

	- `2 <= stones.length <= 2000`

	- `0 <= stones[i] <= 231 - 1`

	- `stones[0] == 0`

	- `stones` is sorted in a strictly increasing order.

## Solutions

```Python3
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                for step in [k-1, k, k+1]:
                    if step > 0:
                        landing = stone + step
                        if landing in dp:
                            dp[landing].add(step)
        return len(dp[stones[-1]]) > 0
```

## AI Review

### Review of Frog Jump Solution

**1. Complexity**
*   **Time Complexity:** $O(N^2)$, where $N$ is the number of stones. In the worst case, each stone could store up to $N$ unique jump sizes in its set.
*   **Space Complexity:** $O(N^2)$ to store the dictionary mapping each stone to a set of possible incoming jump lengths.

**2. Correctness**
*   The logic is **correct**. It correctly handles the first jump constraint (must be 1) by initializing `dp[0]` with `0` and only allowing `step > 0`. 
*   **Edge Case:** If `stones[1] != 1`, the frog cannot leave the first stone. The code handles this because the only valid `step` from stone 0 is `1`; if `1` is not in `dp`, subsequent sets remain empty.

**3. Concrete Optimization**
*   **Early Exit:** Add `if dp[stones[-1]]: return True` inside the loops. If the last stone is reached at any point, there is no need to process the remaining stones.

**4. Key Algorithmic Pattern**
*   **Dynamic Programming (Tabulation):** It uses a hash map for state storage where `dp[stone]` represents all possible velocities (jump lengths) that can reach that position. It can also be viewed as a **Breadth-First Search (BFS)** on a state-space graph where nodes are `(position, last_step)`.
