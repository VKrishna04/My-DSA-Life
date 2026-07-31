# Median of Two Sorted Arrays

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-median-of-two-sorted-arrays` |
| Topics | Array, Binary Search, Divide and Conquer |
| Solved | 2026-05-15 |
| Solve Time | 36m 18s |
| Runtime | 4 ms (beats 28.7436%) |
| Memory | 19.5 MB (beats 41.48049999999999%) |

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
*   **Time:** $O((m+n) \log(m+n))$ due to the `sorted()` function on the combined list of length $m+n$.
*   **Space:** $O(m+n)$ to store the intermediate concatenated list `res`.

**2. Correctness**
The logic is mathematically sound and handles edge cases (like empty arrays or single-element arrays) correctly. However, it **fails the problem's specific constraint** requiring $O(\log(m+n))$ time complexity. For very large inputs, this approach will be significantly slower than the optimal solution.

**3. Concrete Optimization**
Instead of sorting the combined arrays, use a **Binary Search** approach to find the correct partition point between `nums1` and `nums2`. By ensuring the left half of the partition contains the same number of elements as the right half and that all elements on the left are less than or equal to those on the right, you can find the median in $O(\log(\min(m, n)))$ time without merging the arrays.

**4. Key Algorithmic Pattern**
Binary Search (specifically, searching on the partition index of the smaller array).
