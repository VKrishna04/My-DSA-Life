# Decode Ways

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-decode-ways` |
| Topics | String, Dynamic Programming |
| Solved | 2026-04-11 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.4 MB (beats 41.223299999999995%) |

## Problem Statement

You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

	- `"AAJF"` with the grouping `(1, 1, 10, 6)`

	- `"KJF"` with the grouping `(11, 10, 6)`

	- The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

 

**Example 1:**

**Input:** s = "12"

**Output:** 2

**Explanation:**

"12" could be decoded as "AB" (1 2) or "L" (12).

**Example 2:**

**Input:** s = "226"

**Output:** 3

**Explanation:**

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

**Example 3:**

**Input:** s = "06"

**Output:** 0

**Explanation:**

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` contains only digits and may contain leading zero(s).

## Solutions

```Python3
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        
        prev = 1
        curr = 1

        for i in range(2, n+1):
            temp = 0
            if int(s[i-1:i]) > 0:
                temp += curr
            if 10 <= int(s[i-2:i]) <= 26:
                temp += prev
            prev, curr = curr, temp
        return curr
```

## AI Review

**1. Complexity**
*   **Time:** $O(n)$, where $n$ is the length of the string. We iterate through the string once.
*   **Space:** $O(1)$, as it only stores two integer variables (`prev`, `curr`) regardless of input size.

**2. Correctness**
The logic is **correct**. It properly handles:
*   **Leading zeros:** Returns 0 if `s[0] == '0'`.
*   **Single digits:** Validates if the current digit is non-zero.
*   **Double digits:** Checks if the pair falls within the 10–26 range.
*   **Invalid sequences:** If a digit like "0" cannot be paired (e.g., "30"), `temp` becomes 0, correctly propagating the impossibility.

**3. Concrete Optimization**
Replace string slicing and `int()` conversion with direct character comparisons to avoid unnecessary memory allocation and overhead:
```python
# Instead of int(s[i-1:i]) > 0
if s[i-1] != '0':
    temp += curr
# Instead of 10 <= int(s[i-2:i]) <= 26
if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'):
    temp += prev
```

**4. Key Algorithmic Pattern**
**Dynamic Programming** (Iterative, bottom-up). It utilizes **State Compression** (similar to the Fibonacci sequence) to reduce space complexity from $O(n)$ to $O(1)$.
