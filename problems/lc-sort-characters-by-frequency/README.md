# Sort Characters By Frequency

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-sort-characters-by-frequency` |
| Topics | Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting |
| Solved | 2024-11-20 |
| Runtime | 6 ms (beats 83.8008%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

Return _the sorted string_. If there are multiple answers, return _any of them_.

 

**Example 1:**

**Input:** s = "tree"
**Output:** "eert"
**Explanation:** 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

**Example 2:**

**Input:** s = "cccaaa"
**Output:** "aaaccc"
**Explanation:** Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

**Example 3:**

**Input:** s = "Aabb"
**Output:** "bbAa"
**Explanation:** "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

 

**Constraints:**

	- `1 <= s.length <= 5 * 105`

	- `s` consists of uppercase and lowercase English letters and digits.

## Solutions

### Alt approach (Python3) — imported

Submission #1458513764

```Python3
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        result = ''.join([char * freq for char, freq in sorted_chars])

        return result

        # return ''.join([char * freq for char, freq in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)])
```

## AI Review

### 1. Complexity
*   **Time**: $O(N + K \log K)$, where $N$ is the string length and $K$ is the number of unique characters. $O(N)$ to count, $O(K \log K)$ to sort unique characters.
*   **Space**: $O(N + K)$ to store the frequency map and the final output string.

### 2. Correctness
**Correct.** It successfully handles:
*   **Case Sensitivity**: 'A' and 'a' are treated as distinct keys.
*   **Tie-breaking**: Characters with the same frequency can appear in any order (as per LeetCode requirements).
*   **Edge Cases**: Empty strings or strings with one character return correctly.

### 3. Optimization: Bucket Sort
Instead of sorting, use **Bucket Sort** to achieve **$O(N)$ time**.
Create a list of lists where `buckets[i]` stores characters appearing `i` times. Iterate from the highest index down to build the string. This avoids the $O(K \log K)$ sorting overhead.

### 4. Key Algorithmic Pattern
**Frequency Counting** (using a Hash Map/Counter) followed by **Greedy Sorting**.
