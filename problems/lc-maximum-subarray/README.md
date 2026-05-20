# Maximum Subarray

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-maximum-subarray` |
| Topics | Array, Divide and Conquer, Dynamic Programming |
| Solved | 2026-01-02 |
| Runtime | 94 ms (beats 5.176500000000063%) |
| Memory | 30 MB (beats 99.99520000000001%) |

## Problem Statement

Given an integer array `nums`, find the subarray with the largest sum, and return _its sum_.

 

**Example 1:**

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

**Example 2:**

**Input:** nums = [1]
**Output:** 1
**Explanation:** The subarray [1] has the largest sum 1.

**Example 3:**

**Input:** nums = [5,4,-1,7,8]
**Output:** 23
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `-104 <= nums[i] <= 104`

 

**Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Solutions

```Python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = ans = nums[0]

        for x in nums[1:]:
            curr = max(x, curr + x)
            ans = max(ans, curr)
        return ans
```

## AI Review

**1. Complexity**
*   **Time:** $O(n)$ — The algorithm performs a single pass through the array.
*   **Space:** $O(1)$ — Only two scalar variables (`curr`, `ans`) are maintained regardless of input size.

**2. Correctness**
The solution is **correct**. It properly handles:
*   **All-negative numbers:** By initializing with `nums[0]` and comparing `x` vs `curr + x`, it correctly identifies the "least negative" single element as the maximum.
*   **Single-element arrays:** The loop is skipped, and `nums[0]` is returned.
*   **Note:** It assumes `len(nums) >= 1` (standard LeetCode constraint).

**3. Concrete Optimization**
While the Big-O is optimal, you can reduce constant-time overhead by replacing the `max()` function calls with an `if` statement. Function calls in Python are relatively expensive:
```python
for x in nums[1:]:
    curr = x if curr < 0 else curr + x
    if curr > ans: ans = curr
```
This avoids the overhead of the `max` built-in and is generally faster in Python performance benchmarks.

**4. Key Algorithmic Pattern**
**Kadane’s Algorithm** (a specialized form of Dynamic Programming/Greedy). It makes a local optimal choice at each step to determine the global maximum.
