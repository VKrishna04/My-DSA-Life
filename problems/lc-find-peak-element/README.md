# Find Peak Element

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-find-peak-element` |
| Topics | Array, Binary Search |
| Solved | 2025-12-31 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -&infin;`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

 

**Example 1:**

**Input:** nums = [1,2,3,1]
**Output:** 2
**Explanation:** 3 is a peak element and your function should return the index number 2.

**Example 2:**

**Input:** nums = [1,2,1,3,5,6,4]
**Output:** 5
**Explanation:** Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

 

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `-231 <= nums[i] <= 231 - 1`

	- `nums[i] != nums[i + 1]` for all valid `i`.

## Solutions

```Python3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Linear
        
        # for i in range(len(nums)):
        #     if (i==0 or (nums[i] > nums[i-1])) and (i == len(nums)-1 or (nums[i] > nums[i+1])):
        #         return i

        # O(log n) Binar Search

        n = len(nums)

        if n == 1 or nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return n-1

        low = 1
        high = n-2
        
        while low < high:
            mid = (low+high)//2

            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low
        
        
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(\log n)$ — The search space is halved in each iteration.
*   **Space Complexity:** $O(1)$ — Only a constant amount of extra space is used for pointers.

### 2. Correctness
The solution is **correct**. It properly handles:
*   **Single-element arrays:** Handled by the `n == 1` check.
*   **Boundary peaks:** Explicitly checks the first and last elements.
*   **Strictly increasing/decreasing arrays:** Handled by the boundary checks and the binary search logic.

### 3. Concrete Optimisation
You can simplify the code by removing the manual boundary checks and searching the full range $[0, n-1]$. This reduces "boilerplate" while maintaining $O(\log n)$ logic:

```python
low, high = 0, len(nums) - 1
while low < high:
    mid = (low + high) // 2
    if nums[mid] < nums[mid + 1]:
        low = mid + 1
    else:
        high = mid
return low
```

### 4. Key Algorithmic Pattern
**Binary Search on Answer (Slope Analysis):** Even though the array isn't sorted, we can use binary search because there is always a guaranteed peak in the direction of the "uphill" slope (where $nums[i] < nums[i+1]$).
