# Minimum Sum of Mountain Triplets I

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-minimum-sum-of-mountain-triplets-i` |
| Topics | Array |
| Solved | 2024-10-27 |
| Runtime | 58 ms (beats 57.67659999999998%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

You are given a **0-indexed** array `nums` of integers.

A triplet of indices `(i, j, k)` is a **mountain** if:

	- `i < j < k`

	- `nums[i] < nums[j]` and `nums[k] < nums[j]`

Return _the **minimum possible sum** of a mountain triplet of_ `nums`. _If no such triplet exists, return_ `-1`.

 

**Example 1:**

**Input:** nums = [8,6,1,5,3]
**Output:** 9
**Explanation:** Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
- 2 < 3 < 4
- nums[2] < nums[3] and nums[4] < nums[3]
And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

**Example 2:**

**Input:** nums = [5,4,8,7,10,2]
**Output:** 13
**Explanation:** Triplet (1, 3, 5) is a mountain triplet of sum 13 since: 
- 1 < 3 < 5
- nums[1] < nums[3] and nums[5] < nums[3]
And the sum of this triplet is nums[1] + nums[3] + nums[5] = 13. It can be shown that there are no mountain triplets with a sum of less than 13.

**Example 3:**

**Input:** nums = [6,5,4,3,4,5]
**Output:** -1
**Explanation:** It can be shown that there are no mountain triplets in nums.

 

**Constraints:**

	- `3 <= nums.length <= 50`

	- `1 <= nums[i] <= 50`

## Hints

<details>
<summary>Hint 1</summary>

Bruteforce over all possible triplets.

</details>

## Solutions

```Python3
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        output = float('inf')
        for i in range(n - 2):
            for j in range(i+1, n-1):
                if nums[i] < nums[j]:
                    for k in range(j+1,n):
                        if nums[k] < nums[j]:
                            output = min(output, nums[i]+nums[j]+nums[k])
        return output if output != float('inf') else -1
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n^3)$ due to the triple nested loops iterating through all possible triplets $(i, j, k)$.
*   **Space Complexity:** $O(1)$ as only a few scalar variables are used.

### 2. Correctness
The code is **correct**. It exhaustivey checks all indices where $i < j < k$ and verifies the mountain condition ($nums[i] < nums[j]$ and $nums[k] < nums[j]$). It correctly handles cases where no triplet exists by returning `-1`.

### 3. Concrete Optimisation
The solution can be optimized to **$O(n)$ time** using **Prefix and Suffix Minimums**. 
Instead of searching for $i$ and $k$ repeatedly:
1.  Create an array `left_min` where `left_min[j]` is the minimum value in `nums[0...j-1]`.
2.  Create an array `right_min` where `right_min[j]` is the minimum value in `nums[j+1...n-1]`.
3.  Iterate through each index $j$ as a potential peak. If `left_min[j] < nums[j] > right_min[j]`, calculate the sum and update the result.

### 4. Key Algorithmic Pattern
*   **Current:** Brute Force / Triple Loop.
*   **Optimized:** Pre-computation (Prefix/Suffix Arrays).
