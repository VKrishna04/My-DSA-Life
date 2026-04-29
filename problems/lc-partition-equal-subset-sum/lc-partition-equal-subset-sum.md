# Partition Equal Subset Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-partition-equal-subset-sum` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-29 |
| Runtime | 585 ms (beats 75.80049999999925%) |
| Memory | 19.3 MB (beats 84.88389999999998%) |

## Problem Statement

Given an integer array `nums`, return `true` _if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or _`false`_ otherwise_.

 

**Example 1:**

**Input:** nums = [1,5,11,5]
**Output:** true
**Explanation:** The array can be partitioned as [1, 5, 5] and [11].

**Example 2:**

**Input:** nums = [1,2,3,5]
**Output:** false
**Explanation:** The array cannot be partitioned into equal sum subsets.

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 100`

## Solutions

```Python3
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totsum = sum(nums)
        if totsum % 2 != 0:
            return False
        
        target = totsum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for w in range(target, num-1, -1):
                if dp[w] or dp[w-num]:
                    dp[w] = True
        return dp[-1]
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(n \times S)$, where $n$ is the number of elements and $S$ is the target sum ($\text{total sum} / 2$).
*   **Space:** $O(S)$ for the 1D DP array.

**2. Correctness**
The solution is correct. By iterating backwards through the `range(target, num-1, -1)`, it correctly prevents using the same element multiple times (0/1 Knapsack property). It handles the odd-sum edge case correctly.

**3. Concrete Optimisation**
Use **Bit Manipulation**. Since you only care if a sum is possible (boolean), you can treat the DP table as a large integer (bitset). This leverages Python's arbitrary-precision integers for a massive speedup:
```python
bits = 1
for num in nums:
    bits |= (bits << num)
return bool(bits & (1 << target))
```
This reduces the internal loop to a hardware-level bitwise operation, significantly improving performance.

**4. Key Algorithmic Pattern**
**Dynamic Programming** (specifically the **0/1 Knapsack / Subset Sum** variation with space optimization).
