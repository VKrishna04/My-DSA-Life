# Merge Strings Alternately

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-merge-strings-alternately` |
| Topics | Two Pointers, String |
| Solved | 2026-03-24 |
| Runtime | 56 ms (beats 5.666599999999969%) |
| Memory | 19.4 MB (beats 17.745299999999993%) |

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.



Return _the merged string._



 


**Example 1:**




**Input:** word1 = "abc", word2 = "pqr"
**Output:** "apbqcr"
**Explanation:** The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


**Example 2:**




**Input:** word1 = "ab", word2 = "pqrs"
**Output:** "apbqrs"
**Explanation:** Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


**Example 3:**




**Input:** word1 = "abcd", word2 = "pq"
**Output:** "apbqcd"
**Explanation:** Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d


 


**Constraints:**




	- `1 <= word1.length, word2.length <= 100`

	- `word1` and `word2` consist of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.

</details>

## Solutions

```Python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i += 1
        return result
```

## AI Review

1. **Complexity**: 
   - **Time**: **$O((n+m)^2)$**, where $n$ and $m$ are the lengths of `word1` and `word2`. In Python, strings are immutable; using `+=` inside a loop creates a new copy of the string each time, leading to quadratic time.
   - **Space**: **$O(n+m)$** to store the result.

2. **Correctness**: 
   - **Correct**. The logic successfully handles strings of different lengths and ensures all characters are appended in the correct order.

3. **Optimisation**: 
   - Use a **list** to collect characters and `"".join()` at the end. 
   ```python
   result = []
   # ... result.append(word1[i]) ...
   return "".join(result)
   ```
   This reduces time complexity to **$O(n+m)$** because list appending is $O(1)$ amortized, avoiding the expensive re-allocation of strings.

4. **Key Algorithmic Pattern**: 
   - **Two Pointers / Parallel Iteration**: You are traversing two sequences simultaneously using index pointers to merge them.
