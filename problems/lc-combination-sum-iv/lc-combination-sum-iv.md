# Combination Sum IV

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-combination-sum-iv` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-01 |
| Runtime | 40 ms (beats 96.41529999999997%) |
| Memory | 19.2 MB (beats 67.07320000000001%) |

## Problem Statement

Given an array of **distinct** integers `nums` and a target integer `target`, return _the number of possible combinations that add up to_ `target`.

The test cases are generated so that the answer can fit in a **32-bit** integer.

 

**Example 1:**

**Input:** nums = [1,2,3], target = 4
**Output:** 7
**Explanation:**
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

**Example 2:**

**Input:** nums = [9], target = 3
**Output:** 0

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 1000`

	- All the elements of `nums` are **unique**.

	- `1 <= target <= 1000`

 

**Follow up:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

## Solutions

```Python3
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        m = 2 * 32

        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i < num:
                    continue
                dp[i] += dp[i-num]
        return dp[-1]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(T \times N)$, where $T$ is the `target` value and $N$ is the number of elements in `nums`. We iterate through the DP table of size $T$, and for each entry, we iterate through $N$ numbers.
*   **Space Complexity:** $O(T)$ to store the `dp` array.

### 2. Correctness
The solution is **correct** for the problem constraints. It effectively counts permutations because it treats the same set of numbers in different orders as distinct paths to the sum.
*   **Edge Cases:** It correctly handles cases where `target` is 0 (returns 1) or where no combination exists (returns 0). 
*   **Minor Note:** The line `m = 2 * 32` is dead code and should be removed.

### 3. Optimization
**Sort `nums` initially.** If the input array is sorted, you can replace the `continue` statement with a `break`.
```python
nums.sort()
# ... inside the loop ...
for num in nums:
    if i < num:
        break # No need to check larger numbers
    dp[i] += dp[i-num]
```
This significantly reduces unnecessary iterations when `i` is small.

### 4. Key Algorithmic Pattern
**Bottom-up Dynamic Programming.** Specifically, it is a variation of the **Unbounded Knapsack / Combination Sum** pattern focused on counting permutations.
