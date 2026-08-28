# Non Repeating Character

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-non-repeating-character-1587115620` |
| Topics | Hash Table, String |
| Solved | 2026-06-24 |

## Problem Statement

Given a string **s** consisting of **lowercase **English** **Letters. return the first non-repeating character in **s**. If there is no non-repeating character, return **'$'**.

**Examples:**

**Input: **s = "geeksforgeeks"
**Output: **'f'**
Explanation: **In the given string, 'f' is the first character in the string which does not repeat.
**Input: **s = "racecar"
**Output: **'e'
**Explanation: **In the given string, 'e' is the only character in the string which does not repeat.
**Input: **s = "aabbccc"
**Output: '$'**
**Explanation: **All the characters in the given string are repeating.
**Constraints:**
1 &le; s.size() &le; 105

## AI Review

Your solution is clean and achieves the optimal time complexity.

### 1. Complexity
*   **Time:** **O(N)**, where $N$ is the string length. You perform two linear passes: one to count and one to find the first character with a count of 1.
*   **Space:** **O(1)** (technically $O(K)$ where $K$ is the alphabet size). Since the input is limited to lowercase English letters, the hash map size is capped at 26, regardless of how large $N$ becomes.

### 2. Correctness
The logic is sound. By iterating through the original string `s` in the second loop (rather than the dictionary keys), you correctly identify the **first** non-repeating character. It handles cases with no unique characters (returning `$`) and single-character strings correctly.

### 3. Concrete Optimization
Use `collections.Counter`. In Python, `Counter` is implemented in C and is generally faster than manual `.get()` or `if/else` logic for frequency counting.

```python
from collections import Counter
counts = Counter(s)
for char in s:
    if counts[char] == 1:
        return char
```

### 4. Key Algorithmic Pattern
**Frequency Hashing (Two-Pass):** Using a hash map to store global state (counts) and re-scanning the original sequence to maintain order.
