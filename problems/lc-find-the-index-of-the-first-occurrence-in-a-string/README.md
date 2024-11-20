# Find the Index of the First Occurrence in a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-the-index-of-the-first-occurrence-in-a-string` |
| Topics | Two Pointers, String, String Matching |
| Solved | 2025-09-16 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

 

**Example 1:**

**Input:** haystack = "sadbutsad", needle = "sad"
**Output:** 0
**Explanation:** "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

**Example 2:**

**Input:** haystack = "leetcode", needle = "leeto"
**Output:** -1
**Explanation:** "leeto" did not occur in "leetcode", so we return -1.

 

**Constraints:**

	- `1 <= haystack.length, needle.length <= 104`

	- `haystack` and `needle` consist of only lowercase English characters.

## Solutions

```Python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(N \cdot M)$, where $N$ is the length of `haystack` and $M$ is the length of `needle`. In each of the $N-M+1$ iterations, a string slice and comparison occur, both taking $O(M)$.
*   **Space Complexity:** $O(M)$ in many Python implementations because slicing `haystack[i:i+len(needle)]` creates a new string copy of length $M$.

**2. Correctness**
The solution is correct and handles key edge cases:
*   **Needle longer than haystack:** The `range` becomes empty or negative, correctly returning `-1`.
*   **Empty needle:** If $M=0$, the loop runs once at $i=0$, compares `"" == ""`, and returns `0` (matching standard `strstr` behavior).
*   **No match:** Returns `-1` after the loop completes.

**3. Optimization**
Use the **Knuth-Morris-Pratt (KMP) algorithm**. It improves time complexity to **$O(N + M)$** by using a "Partial Match" table (LPS array) to skip unnecessary comparisons, avoiding the $O(N \cdot M)$ worst-case scenario.

**4. Key Algorithmic Pattern**
**Sliding Window (Fixed Size)** / Brute Force String Matching.
