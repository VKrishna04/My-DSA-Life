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

1.  **Time Complexity**: O(N), where N is the length of the input string `s`. `strip()`, `split()`, list creation/manipulation, and `join()` all scale linearly with string length or total word length.
    **Space Complexity**: O(N), as several intermediate lists and strings are created (stripped string, list of words, modified list of words, reversed list of words, final joined string).

2.  **Correctness**: The solution is surprisingly correct for the standard "Reverse Words in a String" problem. The quirky `words = [words[0]]+[word+' ' for word in words[1:]]` logic effectively adds a trailing space to all words *except* the first (which becomes the last in the reversed output). When these are joined by an empty string `''`, these trailing spaces act as separators. The final word (original first) has no trailing space, preventing an unwanted trailing space in the result. It correctly handles multiple spaces, leading/trailing spaces, and single/empty string inputs.

3.  **One concrete optimisation**: The most idiomatic and often more efficient way to join reversed words is `return ' '.join(words[::-1])`. This avoids the complex and less readable intermediate step of modifying individual words to include spaces.

4.  **Key Algorithmic Pattern**: String Tokenization (splitting into words), List Manipulation (reversing the order of elements), and String Reconstruction (joining elements with a separator).
