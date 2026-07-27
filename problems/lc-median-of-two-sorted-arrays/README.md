# Median of Two Sorted Arrays

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-median-of-two-sorted-arrays` |
| Topics | Array, Binary Search, Divide and Conquer |
| Solved | 2026-05-15 |
| Solve Time | 15m 59s |
| Runtime | 4 ms (beats 28.809699999999992%) |
| Memory | 19.5 MB (beats 41.407999999999994%) |

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

### Alt approach (Python3)

Duplicate resolved — 11 Aug 2024

```Python3
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))
        # p1 = nums1
        # if num1 is not None or nums2 us not None:

```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O((m+n) \log(m+n))$ due to the `sorted()` call on the combined list.
*   **Space Complexity:** $O(m+n)$ to store the concatenated `res` list.

**2. Correctness**
The logic is **correct** for finding the median; it handles both even and odd total lengths correctly. It is robust against empty arrays (if at least one contains elements). However, it fails the problem's specific constraint of $O(\log(m+n))$ time complexity.

**3. Concrete Optimization**
Instead of re-sorting the combined list, use **Binary Search** on the partition of the smaller array. Since the input arrays are already sorted, you can find a partition point such that all elements on the left are smaller than those on the right. This reduces time complexity to **$O(\log(\min(m, n)))$** and space to **$O(1)$**.

**4. Key Algorithmic Pattern**
The current code uses **Brute Force (Concatenate & Sort)**. The optimal pattern required for this problem is **Binary Search** (specifically, binary search on the partition index).
