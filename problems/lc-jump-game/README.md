# Jump Game

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-jump-game` |
| Topics | Array, Dynamic Programming, Greedy |
| Solved | 2026-01-02 |
| Runtime | 44 ms (beats 16.32220000000003%) |
| Memory | 18.4 MB (beats 100%) |

## Problem Statement

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true`_ if you can reach the last index, or _`false`_ otherwise_.

 

**Example 1:**

**Input:** nums = [2,3,1,1,4]
**Output:** true
**Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

**Example 2:**

**Input:** nums = [3,2,1,0,4]
**Output:** false
**Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

**Constraints:**

	- `1 <= nums.length <= 104`

	- `0 <= nums[i] <= 105`

## Solutions

```Python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, nums[i]+i)
        return True
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. The list is traversed once.
*   **Space Complexity:** $O(1)$, as it only uses a single integer variable (`max_reach`).

### 2. Correctness
The solution is **correct** and robust. It effectively handles:
*   **Single-element arrays:** Returns `True` correctly.
*   **Arrays with zeros:** Correctly identifies if a zero blocks all progress (e.g., `[3, 2, 1, 0, 4]`).
*   **Large jumps:** Correctly updates the horizon.

### 3. Concrete Optimisation
**Early Exit:** You can terminate the loop early if the `max_reach` already meets or exceeds the last index. This avoids redundant iterations when the goal is already guaranteed.
```python3
if max_reach >= len(nums) - 1:
    return True
```
Place this inside the loop after updating `max_reach`.

### 4. Key Algorithmic Pattern
**Greedy Algorithm:** At each step, you make the locally optimal choice (maximizing the reachable distance) to achieve the global goal (reaching the end).
