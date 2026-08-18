# Assign Cookies

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-assign-cookies` |
| Topics | Sorting, Array, Greedy, Two Pointers |
| Solved | 2026-06-24 |

## Problem Statement

You are given an array **greed[]**, where **greed[i]** represents the minimum size of cookie required to satisfy the i-th child, and an array **cookie[]**,** **where **cookie[j] **represents the size of the j-th cookie. Each child can receive at most one cookie. A child i will be satisfied if they receive a cookie j such that **cookie[j] >= greed[i]**. Your task is to determine the **maximum** number of children that can be satisfied.

**Examples:**

**Input : **greed[] = [1, 10, 3], cookie = [1, 2, 3]
**Output: **2
**Explanation: **We can only assign cookie to the first and third child.
**Input : **greed[] = [10, 100], cookie = [1, 2]
**Output: **0
**Explanation: **We can not assign cookies to any child.
**Constraints:**
1 &le; greed.size() &le;  105
1 &le; cookie.size() &le;  105
1 &le; greed[i] , cookie[i] &le; 109

## Solutions

```python3
class Solution:
    def maxChildren(self, greed, cookie):
        l = 0
        r = 0
        greed.sort()
        cookie.sort()
        
        while r < len(greed) and l < len(cookie):
            if greed[r] <= cookie[l]:
                r += 1
            l += 1
        
        return r
```

## AI Review

### Analysis

1.  **Complexity:**
    *   **Time Complexity:** $O(G \log G + C \log C)$, where $G$ is the length of the `greed` array and $C$ is the length of the `cookie` array. This is dominated by the sorting step. The two-pointer traversal is $O(G + C)$.
    *   **Space Complexity:** $O(1)$ or $O(G + C)$ depending on the implementation of the sorting algorithm (Python's Timsort uses $O(N)$ auxiliary space).

2.  **Correctness:**
    The solution is correct. It successfully handles edge cases such as empty input arrays, more cookies than children, and scenarios where no cookie is large enough to satisfy any child.

3.  **Optimization:**
    While the algorithmic complexity is optimal, you can slightly improve readability and performance in Python by iterating directly over the `cookie` array using a `for` loop. This avoids manual index management for the cookie pointer.

4.  **Key Algorithmic Pattern:**
    **Greedy Algorithm** combined with **Two Pointers**. By sorting, we ensure that we satisfy the least greedy children with the smallest possible effective cookies, maximizing the total count.
