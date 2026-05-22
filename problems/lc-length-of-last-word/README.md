# Length of Last Word

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-length-of-last-word` |
| Topics | String |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.7 MB (beats 100%) |

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

```Python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

```

## AI Review

### 1. Complexity
*   **Time:** $O(n)$, where $n$ is the length of the string. Both `strip()` and `split()` require a full pass over the input.
*   **Space:** $O(n)$. `split()` creates a list of all words, which can occupy up to $O(n)$ space in memory.

### 2. Correctness
The code is **correct**. 
*   `strip()` handles trailing spaces (e.g., `"a "`), ensuring the last element of the split isn't an empty string.
*   It correctly returns `0` for empty strings or strings containing only spaces.
*   *Note:* Using `split()` (without arguments) is generally more robust in Python as it handles any whitespace length automatically, but `strip().split(" ")` works here.

### 3. Optimization
**Reduce space to $O(1)$:** Instead of creating a list, iterate through the string **backwards**. 
1.  Skip trailing spaces using a pointer.
2.  Count characters until the next space or the start of the string is reached.
This avoids the memory overhead of storing intermediate substrings.

### 4. Key Algorithmic Pattern
**String Manipulation** using built-in high-level functions (alternatively, the **Two-Pointer** or **Backward Iteration** pattern for the optimized version).
