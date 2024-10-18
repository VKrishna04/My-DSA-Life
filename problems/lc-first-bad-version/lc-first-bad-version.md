# First Bad Version

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-first-bad-version` |
| Topics | Binary Search, Interactive |
| Solved | 2024-10-18 |
| Runtime | 32 ms (beats 98.389%) |
| Memory | 16.6 MB (beats 100%) |

## Problem Statement

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

**Example 1:**

**Input:** n = 5, bad = 4
**Output:** 4
**Explanation:**
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

**Example 2:**

**Input:** n = 1, bad = 1
**Output:** 1

 

**Constraints:**

	- `1 <= bad <= n <= 231 - 1`

## Solutions

```Python3
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(\log n)$ — The search space is halved in each iteration of the binary search.
*   **Space Complexity:** $O(1)$ — Only a constant amount of extra space is used for pointers.

### 2. Correctness
The logic is **correct**. 
*   By setting `right = mid` when a bad version is found, the algorithm ensures it doesn't skip the first occurrence.
*   The `left < right` condition combined with `left = mid + 1` prevents infinite loops and correctly converges on the first `True` value.
*   **Edge cases:** Correctly handles $n=1$, cases where the first version is bad, and cases where only the last version is bad.

### 3. Concrete Optimization
While Python handles arbitrarily large integers, in most other languages, `(left + right) // 2` can cause **integer overflow**. A safer way to calculate the midpoint is:
```python
mid = left + (right - left) // 2
```
This ensures the sum never exceeds the maximum value of the integer type.

### 4. Key Algorithmic Pattern
**Binary Search on a Discrete Range.** 
Specifically, this is the "find the first element satisfying a condition" variant (lower bound search).
