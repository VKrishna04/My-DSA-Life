# Container With Most Water

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-container-with-most-water` |
| Topics | Array, Two Pointers, Greedy |
| Solved | 2026-04-18 |
| Runtime | 66 ms (beats 12.777899999999992%) |
| Memory | 29.4 MB (beats 97.89119999999997%) |

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Notice** that you may not slant the container.

 

**Example 1:**

**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**

**Input:** height = [1,1]
**Output:** 1

 

**Constraints:**

	- `n == height.length`

	- `2 <= n <= 105`

	- `0 <= height[i] <= 104`

## Solutions

```Python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = float('-inf')
        while left < right:
            currArea = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, currArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of the `height` list. The pointers traverse the list once.
*   **Space Complexity:** $O(1)$, as only a few variables are stored regardless of input size.

### 2. Correctness
The solution is **correct** and handles standard edge cases (e.g., minimum list length of 2, identical heights, or strictly increasing/decreasing heights). Using `float('-inf')` is safe here since areas are non-negative, though `0` is more idiomatic.

### 3. Optimization
While the logic is optimal, you can slightly improve performance by **skipping redundant calculations**. After moving a pointer, you can continue moving it if the new height is less than or equal to the previously "limiting" height. This avoids expensive `min`/`max` calls for configurations that mathematically cannot yield a larger area.

### 4. Key Algorithmic Pattern
**Two-Pointer (Greedy Approach).** By starting at the widest possible interval and always moving the pointer pointing to the shorter line, the algorithm greedily searches for a taller line that might compensate for the shrinking width.
