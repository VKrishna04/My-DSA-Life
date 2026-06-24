# Ladoo problem

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-ladoo-problem2929` |
| Solved | 2026-06-24 |

## Solutions

```Python3
class Solution:
    def divideLadoo(self, N, A):
        return len(set(A))
        
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N)$, where $N$ is the size of the array $A$. Converting the list to a set requires a single pass over the elements.
*   **Space Complexity:** $O(N)$ in the worst case, as the set may store up to $N$ unique elements.

### 2. Correctness
The code correctly identifies the number of unique types of ladoos. 
*   **Edge Cases:** If $N=0$ or $A$ is empty, it returns `0`, which is correct. 
*   **Potential Issue:** In some variations of "Ladoo/Candy" problems, there is a constraint where one can only pick $N/2$ items. If such a constraint exists, this code will fail by returning a count higher than allowed. However, as a standalone unique-element counter, it is correct.

### 3. Optimization
If memory is a constraint and the input array $A$ is already sorted, you can achieve **$O(1)$ auxiliary space** by iterating through the list and counting transitions between different values (e.g., `if A[i] != A[i-1]`).

### 4. Key Algorithmic Pattern
**Hashing:** Using a Hash Set to track seen elements and eliminate duplicates efficiently.
