# 3Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-3sum` |
| Topics | Array, Two Pointers, Sorting |
| Solved | 2025-08-10 |
| Runtime | 539 ms (beats 81.44000000000004%) |
| Memory | 20.7 MB (beats 99.967%) |

## Problem Statement

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

**Example 1:**

**Input:** nums = [-1,0,1,2,-1,-4]
**Output:** [[-1,-1,2],[-1,0,1]]
**Explanation:** 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

**Example 2:**

**Input:** nums = [0,1,1]
**Output:** []
**Explanation:** The only possible triplet does not sum up to 0.

**Example 3:**

**Input:** nums = [0,0,0]
**Output:** [[0,0,0]]
**Explanation:** The only possible triplet sums up to 0.

 

**Constraints:**

	- `3 <= nums.length <= 3000`

	- `-105 <= nums[i] <= 105`

## Hints

<details>
<summary>Hint 1</summary>

So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!

</details>

<details>
<summary>Hint 2</summary>

For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?

</details>

<details>
<summary>Hint 3</summary>

The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

</details>

## Solutions

```Python3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for k in range(len(nums)-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            target = -nums[k]

            i = k+1
            j = len(nums) - 1

            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                
                elif nums[i] + nums[j] > target:
                    j -= 1
                
                else:
                    ans.append([nums[k], nums[i], nums[j]])

                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
        return ans
```

## AI Review

### Review of 3Sum Solution

**1. Complexity**
*   **Time Complexity:** $O(n^2)$. Sorting takes $O(n \log n)$, and the nested loops (outer loop with inner two-pointer scan) take $O(n^2)$.
*   **Space Complexity:** $O(1)$ to $O(n)$. Excluding the output list, space depends on the sorting implementation (Python’s Timsort uses $O(n)$).

**2. Correctness**
The solution is **correct**. It effectively avoids duplicate triplets by:
1.  Skipping identical `nums[k]` values in the outer loop.
2.  Skipping identical `nums[i]` and `nums[j]` values after finding a valid triplet.
It handles edge cases like empty arrays or arrays with fewer than three elements via the `range(len(nums)-2)` bound.

**3. Concrete Optimization**
**Early Exit:** Since the array is sorted, if `nums[k] > 0`, you can immediately `break` the loop. If the smallest number in the triplet is positive, the sum will never reach zero.
```python
if nums[k] > 0: break
```

**4. Key Algorithmic Pattern**
**Two Pointers** (applied on a **Sorted Array**). This reduces the search for the remaining two elements from $O(n^2)$ to $O(n)$.
