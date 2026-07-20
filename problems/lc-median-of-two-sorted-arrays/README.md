# Median of Two Sorted Arrays

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-median-of-two-sorted-arrays` |
| Topics | Array, Binary Search, Divide and Conquer |
| Solved | 2026-05-15 |
| Solve Time | 16s |
| Runtime | 4 ms (beats 29.0733%) |
| Memory | 19.5 MB (beats 41.6867%) |

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

### 1. Complexity
*   **Time Complexity:** $O((M+N) \log(M+N))$ due to the `sorted()` function on the combined list of size $M+N$.
*   **Space Complexity:** $O(M+N)$ to store the concatenated `res` list.

### 2. Correctness
*   **Logic:** The math for the median calculation `(res[n//2] + res[(n-1)//2]) / 2` is correct and handles both even and odd total lengths.
*   **Edge Cases:** Handles empty arrays or single-element arrays correctly.
*   **Requirement Gap:** While functionally correct, it fails the problem's explicit constraint of $O(\log(M+N))$ time complexity.

### 3. Concrete Optimization
Use **Binary Search** on the partition index of the smaller array. Instead of merging and sorting, find a partition point $i$ in `nums1` and $j$ in `nums2` such that all elements on the left are $\leq$ all elements on the right. This reduces time to $O(\log(\min(M, N)))$ and space to $O(1)$.

### 4. Key Algorithmic Pattern
*   **Current:** Brute Force / Sorting.
*   **Optimal:** Binary Search (Divide and Conquer).
