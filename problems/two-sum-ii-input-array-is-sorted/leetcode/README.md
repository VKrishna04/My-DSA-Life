# Two Sum II - Input Array Is Sorted

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-two-sum-ii-input-array-is-sorted` |
| Topics | Array, Two Pointers, Binary Search |
| Solved | 2026-09-15 |
| Runtime | 6 ms (beats 33.56719999999999%) |
| Memory | 22.6 MB (beats 5.100300000000012%) |

## Problem Statement

Given a **1-indexed** array of integers `numbers` that is already **_sorted in non-decreasing order_**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return_ the indices of the two numbers _`index1`_ and _`index2`_, **each incremented by one,** as an integer array _`[index1, index2]`_ of length 2._

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

 

**Example 1:**

**Input:** numbers = [2,7,11,15], target = 9
**Output:** [1,2]
**Explanation:** The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

**Example 2:**

**Input:** numbers = [2,3,4], target = 6
**Output:** [1,3]
**Explanation:** The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

**Example 3:**

**Input:** numbers = [-1,0], target = -1
**Output:** [1,2]
**Explanation:** The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

 

**Constraints:**

	- `2 <= numbers.length <= 3 * 104`

	- `-1000 <= numbers[i] <= 1000`

	- `numbers` is sorted in **non-decreasing order**.

	- `-1000 <= target <= 1000`

	- The tests are generated such that there is **exactly one solution**.

## Solutions

```Python3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                break
        return [l+1, r+1]
```

## AI Review

### Review

1. **Complexity**: 
   - **Time Complexity:** $O(n)$ where $n$ is the length of `numbers`, as we traverse the array at most once.
   - **Space Complexity:** $O(1)$ auxiliary space as we only use two pointer variables.

2. **Correctness**: 
   The code is fully correct. Since the problem guarantees exactly one solution and the input array is sorted, the two-pointer approach will always find the correct 1-indexed pair without running out of bounds.

3. **Concrete Optimisation**: 
   Instead of using `break` and returning outside the loop, return the 1-indexed list `[l + 1, r + 1]` directly inside the `else` branch. This eliminates the post-loop execution overhead.

4. **Key Algorithmic Pattern**: 
   Two Pointers (converging pointers from opposite ends).
