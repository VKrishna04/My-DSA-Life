# Jump Game II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-jump-game-ii` |
| Topics | Array, Dynamic Programming, Greedy |
| Solved | 2026-05-10 |
| Runtime | 2 ms (beats 91.9027%) |
| Memory | 20 MB (beats 66.7333%) |

## Problem Statement

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at index 0.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at index `i`, you can jump to any index `(i + j)` where:

	- `0 <= j <= nums[i]` and

	- `i + j < n`

Return _the minimum number of jumps to reach index _`n - 1`. The test cases are generated such that you can reach index `n - 1`.

 

**Example 1:**

**Input:** nums = [2,3,1,1,4]
**Output:** 2
**Explanation:** The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Example 2:**

**Input:** nums = [2,3,0,1,4]
**Output:** 2

 

**Constraints:**

	- `1 <= nums.length <= 104`

	- `0 <= nums[i] <= 1000`

	- It's guaranteed that you can reach `nums[n - 1]`.

## Solutions

```Python3
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currjump = 0
        right = 0

        for i in range(len(nums) - 1):
            right = max(right, i + nums[i])

            if i == currjump:
                jumps += 1
                currjump = right
        
        return jumps
```

## AI Review

### Analysis of Jump Game II Solution

1.  **Complexity**: 
    *   **Time:** $O(n)$ — The array is traversed once.
    *   **Space:** $O(1)$ — Only a few integer variables are used regardless of input size.

2.  **Correctness**: 
    The logic is **correct**. It greedily tracks the farthest reachable point. 
    *   **Edge Cases:** For `len(nums) == 1`, the loop `range(0)` does not execute, returning `0` jumps correctly. It assumes the destination is always reachable per problem constraints.

3.  **Optimization**: 
    While the Big-O is optimal, you can implement an **early exit**. If `right` reaches or exceeds the last index before the loop finishes, you can return `jumps + 1` immediately to save iterations.
    ```python
    if right >= len(nums) - 1:
        return jumps + 1
    ```
    *(Note: This check must be placed carefully to handle the `len(nums) == 1` case).*

4.  **Key Algorithmic Pattern**: 
    **Greedy Strategy.** It functions similarly to a **Breadth-First Search (BFS)** where each "jump" represents a new level of nodes reachable from the current level, and `currjump` marks the end of the current level.
