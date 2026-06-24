# Kth Smallest

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-kth-smallest-element5635` |
| Topics | Arrays, Searching, Sorting, Data Structures, Algorithms |
| Solved | 2026-06-24 |

## Solutions

```Python3
class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k-1]

```

## AI Review

**1. Complexity**
*   **Time Complexity:** $O(N \log N)$ due to the built-in `sort()` function (Timsort).
*   **Space Complexity:** $O(N)$ in Python, as Timsort requires auxiliary space for merging.

**2. Correctness**
The solution is correct for standard inputs. It handles duplicates naturally and correctly identifies the $k$-th element using 0-based indexing (`k-1`). 
*   **Edge Case:** It assumes $1 \leq k \leq \text{len}(arr)$. If $k$ is out of bounds, it will raise an `IndexError`.

**3. Optimization**
Use **Quickselect** (Median of Medians) to achieve an average time complexity of **$O(N)$**. 
Alternatively, use a **Max-Heap** of size $k$ to solve it in **$O(N \log k)$** time and $O(k)$ space, which is more efficient when $k \ll N$.

**4. Key Algorithmic Pattern**
**Sorting**. (Specifically, the "Sort and Index" pattern for selection problems).
