# House Robber V

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-house-robber-v` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-08-18 |
| Runtime | N/A |
| Memory | N/A |

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed and is protected by a security system with a color code.

You are given two integer arrays `nums` and `colors`, both of length `n`, where `nums[i]` is the amount of money in the `ith` house and `colors[i]` is the color code of that house.

You **cannot rob two adjacent** houses if they share the **same color** code.

Return the **maximum** amount of money you can rob.

 

**Example 1:**

**Input:** nums = [1,4,3,5], colors = [1,1,2,2]

**Output:** 9

**Explanation:**

	- Choose houses `i = 1` with `nums[1] = 4` and `i = 3` with `nums[3] = 5` because they are non-adjacent.

	- Thus, the total amount robbed is `4 + 5 = 9`.

**Example 2:**

**Input:** nums = [3,1,2,4], colors = [2,3,2,2]

**Output:** 8

**Explanation:**

	- Choose houses `i = 0` with `nums[0] = 3`, `i = 1` with `nums[1] = 1`, and `i = 3` with `nums[3] = 4`.

	- This selection is valid because houses `i = 0` and `i = 1` have different colors, and house `i = 3` is non-adjacent to `i = 1`.

	- Thus, the total amount robbed is `3 + 1 + 4 = 8`.

**Example 3:**

**Input:** nums = [10,1,3,9], colors = [1,1,1,2]

**Output:** 22

**Explanation:**

	- Choose houses `i = 0` with `nums[0] = 10`, `i = 2` with `nums[2] = 3`, and `i = 3` with `nums[3] = 9`.

	- This selection is valid because houses `i = 0` and `i = 2` are non-adjacent, and houses `i = 2` and `i = 3` have different colors.

	- Thus, the total amount robbed is `10 + 3 + 9 = 22`.

 

**Constraints:**

	- `1 <= n == nums.length == colors.length <= 105`

	- `1 <= nums[i], colors[i] <= 105`

## Solutions

```Python3
class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n = len(nums)
        dp0 = 0
        dp1 = nums[0]
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                new1 = dp0 + nums[i]
                new0 = max(dp0, dp1)
            else:
                new0 = max(dp1, dp0)
                new1 = max(dp0, dp1) + nums[i]
            dp0 = new0
            dp1 = new1
        return max(dp0, dp1)
```

## AI Review

### Analysis

1.  **Complexity:**
    *   **Time Complexity:** $O(n)$, where $n$ is the number of houses. The solution performs a single linear pass through the arrays.
    *   **Space Complexity:** $O(1)$. It only maintains two variables (`dp0`, `dp1`) to track the previous state, regardless of input size.

2.  **Correctness:**
    *   **Edge Case:** The code will raise an `IndexError` if `nums` is empty (`nums[0]`). An explicit check `if not nums: return 0` is required.
    *   **Logic:** The code correctly implements a variation of the House Robber problem where adjacent houses can only be robbed if they have different colors. If colors match, it enforces the "no-adjacent" rule (`new1 = dp0 + nums[i]`).

3.  **Concrete Optimization:**
    The state update for `new0` is identical in both branches. You can simplify the loop using tuple unpacking to eliminate redundant assignments:
    ```python
    for i in range(1, n):
        prev_max = max(dp0, dp1)
        dp1 = (dp0 if colors[i] == colors[i-1] else prev_max) + nums[i]
        dp0 = prev_max
    ```

4.  **Key Algorithmic Pattern:**
    **Dynamic Programming (State Compression)** — The solution builds a global optimum using previous sub-problems while only storing the most recent states.
