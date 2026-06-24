# Sort 0s, 1s and 2s

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-sort-an-array-of-0s-1s-and-2s4231` |
| Topics | Arrays, Sorting, Data Structures, Algorithms |
| Solved | 2026-06-24 |

## Solutions

```Python3
class Solution:
    def sort012(self, arr):
        l, m, h = 0, 0, len(arr) - 1
        while m <= h:
            if arr[m] == 0:
                arr[l], arr[m] = arr[m], arr[l]
                l += 1
                m += 1
            elif arr[m] == 1:
                m += 1
            else:
                arr[m], arr[h] = arr[h], arr[m]
                h -= 1
```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(n)$ – The array is traversed exactly once.
*   **Space Complexity:** $O(1)$ – Sorting is performed in-place with no extra data structures.

**2. Correctness**
The implementation is correct. It handles all standard edge cases, including:
*   Empty arrays or single-element arrays.
*   Arrays containing only one of the three digits (e.g., all 0s).
*   Already sorted or reverse-sorted arrays.
Note: It correctly avoids incrementing `m` after swapping with `h` because the new `arr[m]` value is unexamined.

**3. Optimization**
While the algorithm is asymptotically optimal, a minor **micro-optimization** can reduce unnecessary operations:
*   **Avoid Self-Swaps:** In the `arr[m] == 0` case, only perform the swap if `l != m`. When the array starts with zeros, `l` and `m` move together, making `arr[l], arr[m] = arr[m], arr[l]` redundant.

**4. Key Algorithmic Pattern**
**Dutch National Flag Algorithm** (Three-way partitioning). It uses three pointers to maintain invariant regions: `[0...l-1]` for 0s, `[l...m-1]` for 1s, and `[h+1...n-1]` for 2s.
