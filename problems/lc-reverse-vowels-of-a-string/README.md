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

### Review

**1. Complexity**
*   **Time Complexity:** $O(n)$, where $n$ is the length of the string. Each character is visited at most once.
*   **Space Complexity:** $O(n)$ to store the list of characters, as Python strings are immutable.

**2. Correctness**
The solution is **correct**. It properly handles:
*   **Mixed Case:** Using a set with both `'aeiouAEIOU'` ensures $O(1)$ lookups for all vowels.
*   **No/Single Vowels:** The `l < r` condition correctly terminates without unnecessary swaps.
*   **Non-alphabetic characters:** They are skipped by the `if/elif` logic.

**3. Optimization**
While the current logic is efficient, you can slightly improve readability and performance by using inner `while` loops to skip non-vowels. This avoids re-evaluating the outer `l < r` condition repeatedly:

```python
while l < r:
    while l < r and letters[l] not in vow:
        l += 1
    while l < r and letters[r] not in vow:
        r -= 1
    letters[l], letters[r] = letters[r], letters[l]
    l += 1
    r -= 1
```

**4. Key Algorithmic Pattern**
**Two Pointers:** Using two indices starting at opposite ends moving toward the center to perform in-place swaps (on the mutable list representation).
