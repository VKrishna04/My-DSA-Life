# Length of Last Word

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-length-of-last-word` |
| Topics | String |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Given a string `s` consisting of words and spaces, return _the length of the **last** word in the string._

A **word** is a maximal substring consisting of non-space characters only.

 

**Example 1:**

**Input:** s = "Hello World"
**Output:** 5
**Explanation:** The last word is "World" with length 5.

**Example 2:**

**Input:** s = "   fly me   to   the moon  "
**Output:** 4
**Explanation:** The last word is "moon" with length 4.

**Example 3:**

**Input:** s = "luffy is still joyboy"
**Output:** 6
**Explanation:** The last word is "joyboy" with length 6.

 

**Constraints:**

	- `1 <= s.length <= 104`

	- `s` consists of only English letters and spaces `' '`.

	- There will be at least one word in `s`.

## Solutions

### Alt approach (Python3) — imported

Submission #1627215692

```Python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

```

## AI Review

**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the length of the string. `strip()` and `split()` both traverse the string.
*   **Space:** $O(N)$. `split()` creates a list of all words, and `strip()` creates a new string.

**2. Correctness**
The logic is correct for the problem constraints. `strip()` handles trailing spaces, ensuring `s[-1]` is the actual last word. It handles single-word strings and strings with leading spaces correctly.

**3. Optimization**
To improve space complexity from **$O(N)$ to $O(1)$**, avoid creating a list of all words. Instead, iterate backward from the end of the string:
1. Skip trailing spaces.
2. Count characters until the next space or the start of the string is reached.

```python
# O(1) Space Example
count = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == ' ':
        if count > 0: return count
    else:
        count += 1
return count
```

**4. Key Algorithmic Pattern**
**String Manipulation.** Specifically, using built-in high-level functions versus manual pointer traversal to handle whitespace delimiters.
