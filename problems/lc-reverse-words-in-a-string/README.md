# Reverse Words in a String

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-reverse-words-in-a-string` |
| Topics | Two Pointers, String |
| Solved | 2026-06-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 11.088999999999995%) |

## Problem Statement

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return _a string of the words in reverse order concatenated by a single space._

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

**Example 1:**

**Input:** s = "the sky is blue"
**Output:** "blue is sky the"

**Example 2:**

**Input:** s = "  hello world  "
**Output:** "world hello"
**Explanation:** Your reversed string should not contain leading or trailing spaces.

**Example 3:**

**Input:** s = "a good   example"
**Output:** "example good a"
**Explanation:** You need to reduce multiple spaces between two words to a single space in the reversed string.

 

**Constraints:**

	- `1 <= s.length <= 104`

	- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.

	- There is **at least one** word in `s`.

 

**Follow-up: **If the string data type is mutable in your language, can you solve it **in-place** with `O(1)` extra space?

## Solutions

```Python3
class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.strip().split())
        words = [words[0]]+[word+' ' for word in words[1:]]
        return ''.join(words[::-1])
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the length of the string. `split()`, list comprehension, and `join()` each traverse the data linearly.
*   **Space:** $O(N)$ to store the list of words and the final joined string.

**2. Correctness**
*   **Critical Bug:** The code fails on empty or whitespace-only strings (e.g., `s = " "`). `s.strip().split()` returns an empty list, causing `words[0]` to raise an `IndexError`.
*   **Logic:** The manual addition of spaces (`word + ' '`) is brittle and creates an extra trailing space logic that is hard to maintain.

**3. Optimization**
Replace the manual space concatenation and slicing with Python’s idiomatic `join()` on the reversed list. This is cleaner and handles edge cases automatically:
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() # split() handles strip and multiple spaces automatically
        return " ".join(reversed(words))
```

**4. Key Algorithmic Pattern**
**Two-Pointer / String Manipulation:** While this solution uses high-level built-ins, the underlying problem tests your ability to parse substrings and reorder them (often solved in-place in languages with mutable strings using a "reverse the whole string, then reverse each word" strategy).
