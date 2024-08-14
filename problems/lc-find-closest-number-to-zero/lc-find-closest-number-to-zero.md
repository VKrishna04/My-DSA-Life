# Find Closest Number to Zero

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-closest-number-to-zero` |
| Topics | Array |
| Solved | 2024-08-14 |
| Runtime | 123 ms (beats 5.2111000000000125%) |
| Memory | 16.8 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` of size `n`, return _the number with the value **closest** to _`0`_ in _`nums`. If there are multiple answers, return _the number with the **largest** value_.

 

**Example 1:**

**Input:** nums = [-4,-2,1,4,8]
**Output:** 1
**Explanation:**
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

**Example 2:**

**Input:** nums = [2,-1,1]
**Output:** 1
**Explanation:** 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

 

**Constraints:**

	- `1 <= n <= 1000`

	- `-105 <= nums[i] <= 105`

## Solutions

```Python3
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        negative_list = []
        positive_list = []

        for num in nums:
            if num < 0:
                negative_list.append(num)
            else:
                positive_list.append(num)

        negative_list.sort(reverse = True)
        positive_list.sort()
        if not negative_list:
            return positive_list[0]
        if not positive_list:
            return negative_list[0]

        if positive_list[0] == -negative_list[0]:
            return positive_list[0]
        return positive_list[0] if positive_list[0] < -negative_list[0] else negative_list[0]
```

## AI Review

### Analysis

1.  **Complexity**
    *   **Time:** $O(n \log n)$ due to the sorting of two lists.
    *   **Space:** $O(n)$ to store the partitioned `negative_list` and `positive_list`.

2.  **Correctness**
    *   The logic is **correct**. It correctly handles ties (e.g., -1 and 1) by returning the positive value and manages cases where one list is empty. No major edge cases fail, though it is inefficient for the problem's constraints.

3.  **Optimization**
    *   **Single-Pass Search:** Avoid sorting and extra lists. Iterate through `nums` once while maintaining a `closest` variable. This reduces time to **$O(n)$** and space to **$O(1)$**.
    ```python
    closest = nums[0]
    for n in nums:
        if abs(n) < abs(closest) or (abs(n) == abs(closest) and n > closest):
            closest = n
    return closest
    ```

4.  **Key Algorithmic Pattern**
    *   **Iterative Comparison:** The problem fundamentally requires finding a minimum value based on a custom comparison rule (absolute distance from zero, then value magnitude for ties).
