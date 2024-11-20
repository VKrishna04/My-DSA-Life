# Smallest Missing Integer Greater Than Sequential Prefix Sum

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-smallest-missing-integer-greater-than-sequential-prefix-sum` |
| Topics | Array, Hash Table, Sorting |
| Solved | 2025-06-01 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.7 MB (beats 100%) |

## Problem Statement

You are given a **0-indexed** array of integers `nums`.

A prefix `nums[0..i]` is **sequential** if, for all `1 <= j <= i`, `nums[j] = nums[j - 1] + 1`. In particular, the prefix consisting only of `nums[0]` is **sequential**.

Return _the **smallest** integer_ `x` _missing from_ `nums` _such that_ `x` _is greater than or equal to the sum of the **longest** sequential prefix._

 

**Example 1:**

**Input:** nums = [1,2,3,2,5]
**Output:** 6
**Explanation:** The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

**Example 2:**

**Input:** nums = [3,4,5,1,12,14,13]
**Output:** 15
**Explanation:** The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

 

**Constraints:**

	- `1 <= nums.length <= 50`

	- `1 <= nums[i] <= 50`

## Hints

<details>
<summary>Hint 1</summary>

To find the longest sequential prefix, iterate from left to right. For a fixed `i`, if `nums[i] != nums[i - 1] + 1` then the longest sequential prefix ends at `i - 1`.

</details>

## Solutions

```Python3
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                sum += nums[i]
            else:
                break
        while sum in nums:
            sum += 1

        return sum

```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N^2)$, where $N$ is the length of `nums`. The prefix sum calculation is $O(N)$, but the `while sum in nums` loop performs a linear search ($O(N)$) up to $N$ times in the worst case (e.g., when many integers following the sum are present in the list).
*   **Space:** $O(1)$, as it only stores a few integer variables.

**2. Correctness**
The logic is **correct**. It accurately identifies the longest sequential prefix starting from index 0 and iteratively finds the smallest missing integer $\ge$ sum. It handles single-element arrays and cases where the sum is already absent correctly.

**3. Optimization**
Convert `nums` into a **set** before the `while` loop. This reduces the lookup time from $O(N)$ to $O(1)$, bringing the overall time complexity down to **$O(N)$**.
```python
num_set = set(nums)
while sum in num_set:
    sum += 1
```

**4. Key Algorithmic Pattern**
*   **Prefix Traversal:** Iterating until a condition is broken.
*   **Hash Set Lookup:** (Optimized version) Using a set for efficient existence checks.
