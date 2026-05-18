# String to Integer (atoi)

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-string-to-integer-atoi` |
| Topics | String |
| Solved | 2024-08-11 |
| Runtime | 39 ms (beats 5.010099999999995%) |
| Memory | 16.7 MB (beats 100%) |

## Problem Statement

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

	- **Whitespace**: Ignore any leading whitespace (`" "`).

	- **Signedness**: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.

	- **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.

	- **Rounding**: If the integer is out of the 32-bit signed integer range `[-231, 231 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-231` should be rounded to `-231`, and integers greater than `231 - 1` should be rounded to `231 - 1`.

Return the integer as the final result.

 

**Example 1:**

**Input:** s = "42"

**Output:** 42

**Explanation:**

The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^

**Example 2:**

**Input:** s = " -042"

**Output:** -42

**Explanation:**

Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
               ^

**Example 3:**

**Input:** s = "1337c0d3"

**Output:** 1337

**Explanation:**

Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^

**Example 4:**

**Input:** s = "0-1"

**Output:** 0

**Explanation:**

Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^

**Example 5:**

**Input:** s = "words and 987"

**Output:** 0

**Explanation:**

Reading stops at the first non-digit character 'w'.

 

**Constraints:**

	- `0 <= s.length <= 200`

	- `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, and `'.'`.

## Solutions

```Python3
class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        num = 0
        if not s:
            return 0
        s = s.lstrip()
        if not s:
            return 0
        if s[0] is '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if not s:
            return 0
        for i in range(len(s)):
            if s[i] != '0':
                s = s[i:]
                if not s:
                    return 0
                break
            
        for i, c in enumerate(s):
            if '0' <= c <= '9':
                num = num * 10 + (ord(c) - ord('0'))
            
            else:
                break
        

        if neg:
            num = -num
        
        if num > (2**31 -1):
            num = 2**31 -1
        elif num < -2**31:
            num = -2**31
        
        return num
            
            
```

## AI Review

### 1. Complexity
*   **Time:** $O(n)$, where $n$ is the length of the string. The string is traversed a few times (strip, sign check, zero check, and digit conversion).
*   **Space:** $O(n)$. In Python, `s.lstrip()` and slicing (`s[1:]`) create new string objects, consuming linear space relative to the input length.

### 2. Correctness
*   **`is` vs `==`**: The code uses `s[0] is '-'`. In Python, `is` checks for identity, not equality. While it may work for interned characters, it is a bug-prone practice; `==` should be used.
*   **Redundancy**: The manual loop to strip leading zeros is unnecessary. The conversion logic `num = num * 10 + digit` inherently handles leading zeros.
*   **Empty Checks**: Repeated `if not s` checks are correct but make the code verbose.

### 3. Optimization
**Avoid String Slicing**: Instead of creating new string copies with `lstrip()` and `s[1:]`, use a single **pointer/index** to traverse the string. This reduces auxiliary space complexity from **$O(n)$ to $O(1)$**.

### 4. Key Algorithmic Pattern
**Linear Scanning / Simulation**: The problem is solved by sequentially simulating the rules provided (trimming, sign detection, digit processing, and clamping).
