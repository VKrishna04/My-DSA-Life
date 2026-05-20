# House Robber

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-house-robber` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-10 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 61%) |

## Problem Statement

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

 

**Example 1:**

**Input:** nums = [1,2,3,1]
**Output:** 4
**Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

**Example 2:**

**Input:** nums = [2,7,9,3,1]
**Output:** 12
**Explanation:** Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 400`

## Solutions

```Python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            prev, curr = curr, max(curr, prev + nums[i])
        return curr

```

## AI Review

### Analysis of House Robber Solution

**1. Complexity**
*   **Time Complexity:** $O(n)$, where $n$ is the number of houses. We iterate through the list exactly once.
*   **Space Complexity:** $O(1)$. By using only two variables (`prev`, `curr`) instead of a DP array, the space usage remains constant regardless of input size.

**2. Correctness**
The logic is correct and follows the recurrence relation: $dp[i] = \max(dp[i-1], dp[i-2] + \text{nums}[i])$.
*   **Edge Cases:** It correctly handles $n=1$ and $n=2$. It assumes $n \geq 1$ (standard LeetCode constraint). If $n=0$ were possible, `nums[0]` would throw an `IndexError`.

**3. Optimization**
While the logic is optimal, the code can be **syntactically simplified** to remove conditional checks ($n=1, 2$). By initializing two pointers at zero, the loop naturally handles small arrays:

```python
def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0
    for n in nums:
        # rob1 is dp[i-2], rob2 is dp[i-1]
        rob1, rob2 = rob2, max(n + rob1, rob2)
    return rob2
```

**4. Key Algorithmic Pattern**
**Dynamic Programming** with **Space Optimization** (Iterative Bottom-Up). It reduces a potential $O(n)$ space complexity to $O(1)$ by only storing the results of the two most recent subproblems.
