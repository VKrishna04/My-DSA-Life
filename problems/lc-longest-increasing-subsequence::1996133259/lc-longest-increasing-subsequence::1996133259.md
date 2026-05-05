# Longest Increasing Subsequence

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-longest-increasing-subsequence::1996133259` |
| Topics | Array, Binary Search, Dynamic Programming |
| Solved | 2026-05-05 |
| Runtime | 7 ms (beats 82.46050000000001%) |
| Memory | 19.5 MB (beats 59.8399%) |

## Problem Statement

Given an integer array `nums`, return _the length of the longest **strictly increasing **__**subsequence**_.

 

**Example 1:**

**Input:** nums = [10,9,2,5,3,7,101,18]
**Output:** 4
**Explanation:** The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

**Example 2:**

**Input:** nums = [0,1,0,3,2,3]
**Output:** 4

**Example 3:**

**Input:** nums = [7,7,7,7,7,7,7]
**Output:** 1

 

**Constraints:**

	- `1 <= nums.length <= 2500`

	- `-104 <= nums[i] <= 104`

 

**Follow up:** Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## Solutions

```Python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [] 

        for num in nums: 
            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                low = 0
                high = len(sub) - 1
                while low < high:
                    mid = (low + high) // 2
                    if sub[mid] >= num:
                        high = mid
                    else:
                        low = mid + 1
                
                sub[low] = num
                
        return len(sub)
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n \log n)$. The code iterates through $n$ elements, performing a binary search ($O(\log n)$) for each.
*   **Space Complexity:** $O(n)$ to store the `sub` array in the worst case (strictly increasing input).

### 2. Correctness
The logic is **correct**. 
*   **Duplicates:** The condition `sub[mid] >= num` correctly handles strictly increasing requirements by replacing the first element that is not smaller than `num`.
*   **Edge Cases:** It correctly handles a single-element list, empty list (returns 0), and already sorted/reverse-sorted lists.
*   **Note:** The `sub` array represents the smallest possible tail for all increasing subsequences of a given length, not the LIS itself.

### 3. Optimization
Replace the manual binary search with Python’s built-in **`bisect.bisect_left`** function. This reduces boilerplate and improves performance as the `bisect` module is implemented in C.

```python
import bisect
# Inside the loop:
idx = bisect.bisect_left(sub, num)
if idx == len(sub):
    sub.append(num)
else:
    sub[idx] = num
```

### 4. Key Algorithmic Pattern
**Patience Sorting** (or Greedy with Binary Search).
