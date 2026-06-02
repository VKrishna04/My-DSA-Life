# Filling Bookcase Shelves

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-filling-bookcase-shelves` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-05-07 |
| Solve Time | 485m 24s |
| Runtime | 3 ms (beats 57.2669%) |
| Memory | 19.4 MB (beats 94.7939%) |

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
*   **Time Complexity:** $O(n^2)$ in the worst case (where all books have width 1 and `shelfWidth` is $n$). More specifically, $O(n \cdot k)$ where $k$ is the maximum number of books that can fit on a single shelf.
*   **Space Complexity:** $O(n)$ to store the `dp` array.

### 2. Correctness
The logic is **correct**. It explores all valid partitions of books into shelves while maintaining the required order.
*   **Edge Cases:**
    *   **Single Book:** Handled; the loops execute once, returning that book's height.
    *   **Book width = `shelfWidth`:** Handled; the inner loop breaks correctly after processing the single book.
    *   **All books on one shelf:** Handled if total width $\leq$ `shelfWidth`.

### 3. Optimization
While $O(n^2)$ is the standard approach, a micro-optimization is to initialize `dp[i]` with a tighter upper bound: `dp[i-1] + books[i-1][1]` (putting the current book on a new shelf by itself). This avoids unnecessary comparisons with `float('inf')` and provides a slightly better starting point for the `min()` function.

### 4. Key Algorithmic Pattern
**Linear Dynamic Programming (Partitioning):** The problem is solved by breaking the sequence into optimal contiguous sub-segments (shelves), where the state `dp[i]` depends on finding the best "cut point" $j$ for the last shelf.
