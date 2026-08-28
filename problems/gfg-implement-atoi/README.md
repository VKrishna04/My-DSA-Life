# Implement Atoi

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-implement-atoi` |
| Topics | String, Design Pattern |
| Solved | 2026-06-24 |

## Problem Statement

Given a string **s**, convert it into a 32-bit signed integer (similar to the atoi() function) without using any built-in conversion functions.
The conversion follows these rules:

- **Ignore Leading Whitespaces:** Skip all leading whitespace characters.

- **Check Sign:** If the next character is either '+' or '-', take it as the sign of the number. If no sign is present, assume the number is positive.

- **Read Digits: **Read the digits and ignore any leading zeros. Stop reading when a non-digit character is encountered or the end of the string is reached. If no digits are found, return 0.

- **Handle Overflow: **If the number exceeds the range of a 32-bit signed integer:
Return 2&sup3;&sup1; &minus; 1 (i.e., 2147483647) if it is greater than the maximum value.
Return &minus;2&sup3;&sup1; (i.e., -2147483648) if it is smaller than the minimum value.

Return the final integer value.

**Examples:**

**Input: **s = "-123"
**Output: -**123
**Explanation: **It is possible to convert -123 into an integer so we returned in the form of an integer

**Input: **s = " -"
**Output: **0
**Explanation: **No digits are present, therefore the returned answer is 0.

**Input: **s = " 1231231231311133"
**Output: **2147483647
**Explanation: **The converted number will be greater than 231 &ndash; 1, therefore print 231 &ndash; 1 = 2147483647.

**Input: **s = "-999999999999"
**Output: -**2147483648
**Explanation: **The converted number is smaller than -231, therefore print -231 = -2147483648.
**Input: **s = "  -0012gfg4"
**Output: **-12**
Explanation: **Nothing is read after -12 as a non-digit character &lsquo;g&rsquo; was encountered.
**Constraints:**
1 &le; |s| &le; 15

## AI Review

### Analysis

1.  **Complexity**:
    *   **Time**: $O(N)$, where $N$ is the length of the string. We traverse the string once.
    *   **Space**: $O(N)$. Note your recurring **space complexity** flag: `s.strip()` creates a new string copy in Python. For a truly $O(1)$ extra space solution, you should manually skip whitespace using a pointer.

2.  **Correctness**: The logic is robust. It correctly handles leading whitespace, signs, non-digit characters, and 32-bit signed integer overflow. Python handles arbitrarily large integers, but your check `num > (INT_MAX - digit) // 10` correctly simulates the constraints of fixed-width integer environments.

3.  **Optimization**: Replace `s = s.strip()` with a pointer-based approach:
    ```python
    while i < len(s) and s[i] == ' ':
        i += 1
    ```
    This avoids the $O(N)$ memory allocation of a new string, bringing auxiliary space to $O(1)$.

4.  **Key Pattern**: **String Parsing/Simulation**. The problem requires careful handling of state transitions (whitespace → sign → digits → termination).
