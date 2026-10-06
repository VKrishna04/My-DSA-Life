# 2 Sum Find A Pair With Given Sum

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-2-sum-find-a-pair-with-given-sum` |
| Topics | Sorting, Two Pointers, Array, Hash Table |
| Solved | 2026-06-24 |

## Problem Statement

Given an array arr[] and an integer target, return the pair of elements whose sum equals target. An element cannot be used twice unless it appears multiple times in the array.

**Note:**  If no pair exist, return an empty array.

**Examples:**

**Input: **arr[] = [2, 9, 10, 4, 15], target = 12
**Output: **[2, 10]**
Explanation: **Pair with sum equal to 12 is (2, 10).
**Input: **arr[] = [3, 2, 4], target = 8
**Output: **[]**
Explanation: **No pair exists with sum equal to 8.
**Input: **arr[] = [1, 4, 5, 6, 1], target = 2
**Output: **[1, 1]**
Explanation: **Pair with sum equal to 2 is (1, 1).
**Constraints:
**1 &le; arr.size() &le; 105**
**0 &le; arr[i] &le; 104
1 &le; target &le; 104

## Solutions

```python3
#User function Template for python3
class Solution:
    # Complete the below function
    def twoSum(self,arr, target):
        seen = {}
        
        for i , x in enumerate(arr):
            if target - x in seen:
                return [x, target - x]
            seen[x] = i
        return []
```

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time Complexity**: $O(n)$, where $n$ is the number of elements in the array. We perform a single pass, and hash map lookups/insertions are $O(1)$ on average.
    *   **Space Complexity**: $O(n)$ to store elements in the dictionary in the worst case (when no pair is found).

2.  **Correctness**: 
    The solution is correct. By checking for the complement (`target - x`) *before* adding the current element `x` to the dictionary, it gracefully handles the edge case where `target` is exactly double an element (e.g., `target = 6, arr = [3]`), ensuring the same index isn't used twice.

3.  **Optimization**:
    Use a **set** instead of a dictionary. The current code stores indices (`seen[x] = i`) but never utilizes them. A `set` reduces memory overhead by only storing the keys.

4.  **Key Algorithmic Pattern**:
    **Hash Table / Complement Lookup**: Using a hash-based structure to transform a potential $O(n^2)$ nested search into an $O(1)$ lookup.
