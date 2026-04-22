# Uncrossed Lines

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-uncrossed-lines` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-22 |
| Runtime | 47 ms (beats 80.24530000000004%) |
| Memory | 19.5 MB (beats 83.15469999999999%) |

## Problem Statement

You are given two integer arrays `nums1` and `nums2`. We write the integers of `nums1` and `nums2` (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers `nums1[i]` and `nums2[j]` such that:

	- `nums1[i] == nums2[j]`, and

	- the line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return _the maximum number of connecting lines we can draw in this way_.

 

**Example 1:**

**Input:** nums1 = [1,4,2], nums2 = [1,2,4]
**Output:** 2
**Explanation:** We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

**Example 2:**

**Input:** nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
**Output:** 3

**Example 3:**

**Input:** nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
**Output:** 2

 

**Constraints:**

	- `1 <= nums1.length, nums2.length <= 500`

	- `1 <= nums1[i], nums2[j] <= 2000`

## Solutions

```Python3
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]
```

## AI Review

### Analysis

1.  **Complexity**
    *   **Time Complexity:** $O(N \times M)$, where $N$ and $M$ are the lengths of `nums1` and `nums2`. Every pair of indices is visited once.
    *   **Space Complexity:** $O(N \times M)$ to store the 2D `dp` table.

2.  **Correctness**
    *   The logic is **correct**. This problem is a direct application of the **Longest Common Subsequence (LCS)** algorithm. By definition, lines do not cross if the chosen elements maintain their relative order, which matches the LCS criteria.
    *   **Edge Cases:** It correctly handles empty lists (returns 0), lists with no common elements (returns 0), and lists of different lengths.

3.  **Optimization**
    *   **Space Reduction:** Since the current row `dp[i]` only depends on the previous row `dp[i-1]`, you can reduce space complexity to **$O(\min(N, M))$** using a 1D array. Update the 1D array in-place while keeping a variable to store the "top-left" (`dp[i-1][j-1]`) value.

4.  **Key Algorithmic Pattern**
    *   **Dynamic Programming (Longest Common Subsequence)**.
