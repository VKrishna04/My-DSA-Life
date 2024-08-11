# Median of Two Sorted Arrays

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-median-of-two-sorted-arrays` |
| Topics | Array, Binary Search, Divide and Conquer |
| Solved | 2024-08-11 |
| Runtime | 65 ms (beats 5.1033%) |
| Memory | 16.8 MB (beats 100%) |

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
        return median(sorted(nums1 + nums2))
        # p1 = nums1
        # if num1 is not None or nums2 us not None:

```

## AI Review

### 1. Complexity
*   **Time:** $O((m+n) \log(m+n))$ due to the `sorted()` function.
*   **Space:** $O(m+n)$ to create the concatenated list.

### 2. Correctness & Edge Cases
*   **Failed Requirements:** The problem explicitly requires $O(\log(m+n))$ time; this solution fails that constraint.
*   **NameError:** `median()` is not a built-in Python function. It requires `from statistics import median`.
*   **Edge Cases:** If both lists are empty, `statistics.median` raises a `StatisticsError`.

### 3. Concrete Optimization
Use **Binary Search** on the partition indices of the smaller array. Instead of merging/sorting, find a partition point $i$ in `nums1` and $j$ in `nums2` such that all elements on the left are less than or equal to all elements on the right. This achieves the required **$O(\log(\min(m, n)))$** time complexity.

### 4. Key Algorithmic Pattern
The provided code uses a **Brute Force (Sort and Find)** approach. The optimal solution uses **Binary Search** on the search space of the array indices.
