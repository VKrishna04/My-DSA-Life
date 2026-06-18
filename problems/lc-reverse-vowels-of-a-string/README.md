# Reverse Vowels of a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-vowels-of-a-string` |
| Topics | Two Pointers, String |
| Solved | 2026-06-18 |
| Runtime | 7 ms (beats 88.62%) |
| Memory | 20.7 MB (beats 15.378100000000009%) |

## Problem Statement

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

**Example 1:**

**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

**Input:** s = "leetcode"

**Output:** "leotcede"

 

**Constraints:**

	- `1 <= s.length <= 3 * 105`

	- `s` consist of **printable ASCII** characters.

## Solutions

```Python3
class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        l = 0
        r = len(letters)-1
        vow = set('aeiouAEIOU')

        while l < r:
            if not letters[l] in vow:
                l += 1
            elif not letters[r] in vow:
                r -= 1
            else:
                letters[l], letters[r] = letters[r], letters[l]
                l += 1
                r -= 1
                
        return ''.join(letters)
```

## AI Review

1.  **Time Complexity:** O(N), where N is the length of the string `s`. It involves one pass to convert to a list, one pass with two pointers, and one pass to join back.
    **Space Complexity:** O(N) due to converting the string `s` into a mutable `list`.

2.  **Correctness:** The solution is correct. It handles edge cases like empty strings, single-character strings, strings with no vowels, and strings consisting entirely of vowels. The two-pointer logic accurately finds and swaps the extreme vowels.

3.  **Optimisation:** For repeated calls to `reverseVowels`, the `vow` set could be created once outside the function (e.g., as a class attribute) to avoid redundant O(1) set construction on each call.

4.  **Key Algorithmic Pattern:** Two Pointers.
