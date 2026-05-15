# Median of Two Sorted Arrays

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-median-of-two-sorted-arrays::2004038057` |
| Topics | Array, Binary Search, Divide and Conquer |
| Solved | 2026-05-15 |
| Runtime | 4 ms (beats 30.1667%) |
| Memory | 19.5 MB (beats 42.92340000000001%) |

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

**Example 1:**

**Input:** nums1 = [1,3], nums2 = [2]
**Output:** 2.00000
**Explanation:** merged array = [1,2,3] and median is 2.

**Example 2:**

**Input:** nums1 = [1,2], nums2 = [3,4]
**Output:** 2.50000
**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

**Constraints:**

	- `nums1.length == m`

	- `nums2.length == n`

	- `0 <= m <= 1000`

	- `0 <= n <= 1000`

	- `1 <= m + n <= 2000`

	- `-106 <= nums1[i], nums2[i] <= 106`

## Solutions

```Python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        n = len(res)
        return (res[n//2] + res[(n-1)//2]) / 2
```

## AI Review

**1. Complexity**
*   **Time Complexity:** $O((m+n) \log(m+n))$ due to the `sorted()` function on the concatenated list.
*   **Space Complexity:** $O(m+n)$ to store the merged list `res`.

**2. Correctness**
The logic is functionally correct and handles all edge cases (empty arrays, single elements, even/odd total lengths) because it relies on Python’s robust built-in sorting. However, it fails the problem's specific constraint of **$O(\log(m+n))$** time complexity.

**3. Concrete Optimization**
Replace sorting with a **Binary Search** approach on the partition index of the smaller array. Instead of merging, find a partition such that all elements on the left side are less than or equal to all elements on the right side. This reduces time complexity to **$O(\log(\min(m, n)))$** and space to **$O(1)$**.

**4. Key Algorithmic Pattern**
*   **Current:** Sort and Index (Brute Force).
*   **Optimal:** Binary Search / Dual Pointer Partitioning.
