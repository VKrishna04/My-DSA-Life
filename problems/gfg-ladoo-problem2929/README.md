# Ladoo problem

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-ladoo-problem2929` |
| Topics | Hashing, Data Structures, Set |
| Solved | 2026-06-24 |

## Solutions

```Python3
class Solution:
    def divideLadoo(self, N, A):
        return len(set(A))
        
```

## AI Review

### Review

**Complexity:**
*   **Time Complexity:** $O(N)$, where $N$ is the number of elements in array $A$. Converting a list to a set requires a single pass to hash each element.
*   **Space Complexity:** $O(N)$ in the worst case (where all elements are unique) to store the set in memory.

**Correctness:**
The logic is correct for finding the number of distinct elements.
*   **Edge Cases:** It correctly handles an empty list (returns 0) and a list where all elements are the same (returns 1). 

**Optimization:**
The solution is already time-optimal ($O(N)$). If memory is a critical constraint and the input list can be modified, you could sort the array in-place ($O(N \log N)$ time) and iterate through it to count unique adjacent elements, reducing auxiliary space to $O(1)$. However, in Python, the current `set()` approach is the most idiomatic and fastest for general use.

**Key Algorithmic Pattern:**
Hashing (using a Set data structure to filter duplicates).
