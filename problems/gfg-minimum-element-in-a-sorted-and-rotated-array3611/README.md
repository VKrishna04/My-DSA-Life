# Minimum Element In A Sorted And Rotated Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-minimum-element-in-a-sorted-and-rotated-array3611` |
| Topics | Searching, Array, Binary Search, Two Pointers |
| Solved | 2026-06-24 |

## Problem Statement

A sorted array** **of distinct elements **arr[]** is rotated at some unknown point, the task is to find the minimum element in it. 

**Examples:**

**Input: **arr[] = [5, 6, 1, 2, 3, 4]
**Output: **1
**Explanation:** 1 is the minimum element in the array.
**Input: **arr[] = [3, 1, 2]
**Output: **1
**Explanation:** Here 1 is the minimum element.

**Input: **arr[] = [4, 2, 3]
**Output: **2
**Explanation:** Here 2 is the minimum element.
**Constraints**:
1 &le; arr.size() &le; 106
1 &le; arr[i] &le; 109

## Solutions

```python3
class Solution:
    def findMin(self, arr):
        l, r = 0, len(arr)-1
        
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                r = mid
        
        return arr[l]
```

## AI Review

### Review
**1. Complexity**
*   **Time Complexity:** $O(\log N)$, where $N$ is the number of elements. The search space is halved in each iteration.
*   **Space Complexity:** $O(1)$, as it uses a constant amount of extra space.

**2. Correctness**
The solution is correct for arrays with **unique elements**. It successfully handles:
*   **Standard rotation:** (e.g., `[4, 5, 1, 2, 3]`).
*   **No rotation:** (e.g., `[1, 2, 3, 4]`) where it correctly returns the first element.
*   **Single element arrays.**

**Edge Case:** If the array contains **duplicate elements** (e.g., `[10, 1, 10, 10, 10]`), the logic `arr[mid] > arr[r]` fails to distinguish which half to discard.

**3. Optimization**
To make the algorithm robust against duplicates, add a check for equality:
```python
if arr[mid] > arr[r]:
    l = mid + 1
elif arr[mid] < arr[r]:
    r = mid
else:
    r -= 1 # Shrink search space linearly when values are equal
```

**4. Key Algorithmic Pattern**
**Binary Search**: Specifically, modified binary search to find the "inflection point" or pivot in a rotated sorted array.
