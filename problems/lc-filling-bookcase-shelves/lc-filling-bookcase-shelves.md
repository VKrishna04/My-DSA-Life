# Filling Bookcase Shelves

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-filling-bookcase-shelves` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-07 |
| Runtime | 3 ms (beats 54.1096%) |
| Memory | 19.4 MB (beats 95.43379999999999%) |

## Problem Statement

You are given an array `books` where `books[i] = [thicknessi, heighti]` indicates the thickness and height of the `ith` book. You are also given an integer `shelfWidth`.

We want to place these books in order onto bookcase shelves that have a total width `shelfWidth`.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to `shelfWidth`, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

	- For example, if we have an ordered list of `5` books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return _the minimum possible height that the total bookshelf can be after placing shelves in this manner_.

 

**Example 1:**

**Input:** books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
**Output:** 6
**Explanation:**
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

**Example 2:**

**Input:** books = [[1,3],[2,4],[3,2]], shelfWidth = 6
**Output:** 4

 

**Constraints:**

	- `1 <= books.length <= 1000`

	- `1 <= thicknessi <= shelfWidth <= 1000`

	- `1 <= heighti <= 1000`

## Solutions

```Python3
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [float('inf')] * n
        
        for i in range(1, n + 1):
            cur_width = 0
            max_height = 0
            for j in range(i - 1, -1, -1):
                cur_width += books[j][0]
                if cur_width > shelfWidth:
                    break
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
        
        return dp[n]
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n^2)$, where $n$ is the number of books. The nested loops iterate through each book and potentially check all preceding books for the current shelf.
*   **Space Complexity:** $O(n)$ to store the `dp` array of size $n+1$.

### 2. Correctness
The solution is correct and handles the problem's constraints well. 
*   **Edge Cases:** It correctly handles a single book, books that exactly fit the `shelfWidth`, and the case where every book requires its own shelf. 
*   **Constraint:** Since the problem guarantees $book\_width \le shelfWidth$, the inner loop will always execute at least once, preventing `dp[i]` from remaining `inf`.

### 3. Optimization
While $O(n^2)$ is optimal for $N=1000$, you could theoretically use a **Segment Tree** or a **Monotonic Queue** to optimize the range maximum height query if the shelf width were extremely large. However, a more practical Pythonic optimization is using `@cache` with a recursive top-down approach, which can sometimes be faster due to skipping unreachable states, though the Big-O remains the same.

### 4. Key Algorithmic Pattern
**Dynamic Programming (Linear/Partitioning DP):** The problem is solved by breaking it into subproblems where `dp[i]` represents the minimum height for the first `i` books by partitioning the array into contiguous subarrays (shelves).
