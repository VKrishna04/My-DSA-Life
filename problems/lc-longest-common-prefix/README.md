# Longest Common Prefix

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-longest-common-prefix` |
| Topics | Array, String, Trie |
| Solved | 2025-06-01 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

 

**Example 1:**

**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"

**Example 2:**

**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.

 

**Constraints:**

	- `1 <= strs.length <= 200`

	- `0 <= strs[i].length <= 200`

	- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Solutions

```Python3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lng = ""
        strs = sorted(strs)
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if (strs[0][i] != strs[-1][i]):
                return lng
            lng+=strs[0][i]
        
        return lng
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \cdot M \log N)$, where $N$ is the number of strings and $M$ is the maximum string length. Sorting strings involves $O(M)$ time for each comparison.
*   **Space Complexity:** $O(N \cdot M)$ to store the sorted copy of the input list.

### 2. Correctness
The logic is sound because, in a sorted list, the longest common prefix of the first and last elements is guaranteed to be the common prefix for the entire set. 
*   **Edge Case:** If `strs` is empty, `strs[0]` will raise an `IndexError`. (Note: LeetCode constraints usually specify `strs.length >= 1`).

### 3. Concrete Optimisation
Instead of sorting the entire list, simply find the lexicographical **minimum** and **maximum** strings in a single pass:
```python
first = min(strs)
last = max(strs)
```
This reduces time complexity to **$O(N \cdot M)$**, as you avoid the $O(\log N)$ sorting overhead.

### 4. Key Algorithmic Pattern
**Lexicographical Sorting / Extremes comparison.** By identifying the two most "distant" strings alphabetically, you define the boundary for any potential common prefix.
