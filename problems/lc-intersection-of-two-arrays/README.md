# Intersection of Two Arrays

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-intersection-of-two-arrays` |
| Topics | Array, Hash Table, Two Pointers, Binary Search, Sorting |
| Solved | 2026-01-03 |
| Runtime | 1 ms (beats 38.4239%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return _an array of their intersection_. Each element in the result must be **unique** and you may return the result in **any order**.

 

**Example 1:**

**Input:** nums1 = [1,2,2,1], nums2 = [2,2]
**Output:** [2]

**Example 2:**

**Input:** nums1 = [4,9,5], nums2 = [9,4,9,8,4]
**Output:** [9,4]
**Explanation:** [4,9] is also accepted.

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 1000`

	- `0 <= nums1[i], nums2[i] <= 1000`

## Solutions

```Python3
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for n in nums1:
            if n not in d:
                d[n] = True
        out = []
        for n in nums2:
            if n in d and d[n]:
                d[n] = False
                out.append(n)
        return out
```

## AI Review

**1. Complexity**
*   **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of `nums1` and `nums2`. Building the dictionary takes $O(n)$ and iterating through `nums2` takes $O(m)$.
*   **Space Complexity:** $O(n)$ to store the unique elements of `nums1` in the dictionary.

**2. Correctness**
The code is **correct**. It successfully handles duplicates in both arrays by using the dictionary as a frequency/existence tracker and immediately setting the value to `False` once an intersection is found, ensuring the output contains only unique elements. It handles empty inputs gracefully.

**3. Concrete Optimization**
Use Python’s built-in **set intersection**. It is more idiomatic and implemented in C, making it significantly faster for large inputs:
```python
return list(set(nums1) & set(nums2))
```
Alternatively, to save space, always convert the *smaller* array into a set.

**4. Key Algorithmic Pattern**
**Hashing (Hash Set/Hash Map)**. The solution uses a hash table to achieve $O(1)$ average-time lookups to determine if an element exists in the other array.
