# Sort Characters By Frequency

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-sort-characters-by-frequency::1458513764` |
| Topics | Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting |
| Solved | 2024-11-20 |
| Runtime | 6 ms (beats 83.8008%) |
| Memory | 17.8 MB (beats 100%) |

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
