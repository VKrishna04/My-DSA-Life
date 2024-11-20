# Ransom Note

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-ransom-note` |
| Topics | Hash Table, String, Counting |
| Solved | 2025-05-05 |
| Runtime | 16 ms (beats 65.05100000000002%) |
| Memory | 18.1 MB (beats 100%) |

## Problem Statement

Given two strings `ransomNote` and `magazine`, return `true`_ if _`ransomNote`_ can be constructed by using the letters from _`magazine`_ and _`false`_ otherwise_.

Each letter in `magazine` can only be used once in `ransomNote`.

 

**Example 1:**

**Input:** ransomNote = "a", magazine = "b"
**Output:** false
**Example 2:**

**Input:** ransomNote = "aa", magazine = "ab"
**Output:** false
**Example 3:**

**Input:** ransomNote = "aa", magazine = "aab"
**Output:** true

 

**Constraints:**

	- `1 <= ransomNote.length, magazine.length <= 105`

	- `ransomNote` and `magazine` consist of lowercase English letters.

## Solutions

```Python3
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)
        if s1 & s2 == s1:
            return True
        return False
```

## AI Review

### 1. Complexity
*   **Time:** $O(m + n)$, where $m$ is the length of `ransomNote` and $n$ is the length of `magazine`. We iterate through both strings once.
*   **Space:** $O(k)$ or $O(1)$, where $k$ is the number of unique characters. Since the input is limited to 26 lowercase English letters, the space is effectively constant.

### 2. Correctness
The code is **correct**. The intersection operator (`&`) for `Counter` objects takes the minimum of matching counts. If `s1 & s2 == s1`, it confirms `magazine` contains at least as many of each character as `ransomNote`. It handles empty strings and insufficient character counts correctly.

### 3. Concrete Optimisation
**Early Exit:** Instead of creating two full counters, count the `magazine` first. Then, iterate through `ransomNote` and decrement the counts in the magazine map. If a count reaches -1, return `False` immediately.
```python
# One-liner version of the same logic:
return not (Counter(ransomNote) - Counter(magazine))
```

### 4. Key Algorithmic Pattern
**Hash Table (Frequency Map)**. Specifically, using a multiset/counter to track character availability.
