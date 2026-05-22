# Check if All Characters Have Equal Number of Occurrences

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-check-if-all-characters-have-equal-number-of-occurrences` |
| Topics | Hash Table, String, Counting |
| Solved | 2024-10-20 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

Given a string `s`, return `true`_ if _`s`_ is a **good** string, or _`false`_ otherwise_.

A string `s` is **good** if **all** the characters that appear in `s` have the **same** number of occurrences (i.e., the same frequency).

 

**Example 1:**

**Input:** s = "abacbc"
**Output:** true
**Explanation:** The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

**Example 2:**

**Input:** s = "aaabb"
**Output:** false
**Explanation:** The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Build a dictionary containing the frequency of each character appearing in s

</details>

<details>
<summary>Hint 2</summary>

Check if all values in the dictionary are the same.

</details>

## Solutions

```Python3
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        
        val = d[s[0]]
        for value in d.values():
            if value != val:
                return False
        return True
```

## AI Review

### 1. Complexity
*   **Time:** $O(N)$, where $N$ is the length of the string $s$. We traverse the string once to build the dictionary and once through the unique values (max 26 for lowercase English letters).
*   **Space:** $O(k)$, where $k$ is the number of unique characters. In the context of lowercase English letters, this is $O(1)$ as $k \le 26$.

### 2. Correctness
The code is correct for the problem constraints.
*   **Edge Cases:** For a single-character string (e.g., "a"), it correctly returns `True`.
*   **Potential Fail:** If the input string `s` is empty, `s[0]` will raise an `IndexError`. However, LeetCode constraints typically specify $1 \le s.length$.

### 3. Concrete Optimization
Use `collections.Counter` and a `set` to simplify the logic and improve readability:
```python
from collections import Counter
return len(set(Counter(s).values())) == 1
```
This reduces the manual loop and conditional checks to a single line.

### 4. Key Algorithmic Pattern
**Frequency Map (Counting):** Using a hash map (dictionary) to store the occurrences of elements and then verifying a property of those counts.
