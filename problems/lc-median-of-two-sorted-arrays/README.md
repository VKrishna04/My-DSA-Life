# Median of Two Sorted Arrays

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-median-of-two-sorted-arrays` |
| Topics | Array, Binary Search, Divide and Conquer |
| Solved | 2026-05-15 |
| Runtime | 4 ms (beats 30.3379%) |
| Memory | 19.5 MB (beats 42.427699999999994%) |

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

### Review

**1. Complexity**
*   **Time:** $O((m+n) \log (m+n))$ due to the `sorted()` call on the combined list of length $m+n$.
*   **Space:** $O(m+n)$ to store the concatenated `res` list.

**2. Correctness**
*   **Logic:** Mathematically correct. Using `(res[n//2] + res[(n-1)//2]) / 2` elegantly handles both even and odd total lengths.
*   **Edge Cases:** Handles empty arrays or arrays of size 1 correctly.
*   **Constraint Violation:** While functionally correct, it fails the LeetCode requirement of $O(\log(m+n))$ time complexity.

**3. Concrete Optimization**
Implement **Binary Search on the partition index**. Instead of merging and sorting, partition the smaller array such that the left side of the partition contains half the total elements. Ensure that the maximum of the left elements is less than or equal to the minimum of the right elements. This reduces time complexity to $O(\log(\min(m, n)))$ and space to $O(1)$.

**4. Key Algorithmic Pattern**
The provided code uses **Sort and Index**. The optimal solution uses **Binary Search**.
