# Reverse Integer

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-reverse-integer` |
| Topics | Math |
| Solved | 2024-08-31 |
| Runtime | 36 ms (beats 95.86259999999999%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

Given a signed 32-bit integer `x`, return `x`_ with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

 

**Example 1:**

**Input:** x = 123
**Output:** 321

**Example 2:**

**Input:** x = -123
**Output:** -321

**Example 3:**

**Input:** x = 120
**Output:** 21

 

**Constraints:**

	- `-231 <= x <= 231 - 1`

## Solutions

```Python3
class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x=-x
            neg = True

        I = int(str(x)[::-1])
        if I <= -2**31 or I >= 2**31 - 1:
            return 0
        return I if neg == False else -I
        
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(\log_{10} N)$, where $N$ is the value of `x`. Converting an integer to a string and reversing it both take time proportional to the number of digits.
*   **Space Complexity:** $O(\log_{10} N)$ to store the string representation of the integer.

### 2. Correctness
The code is **correct** and handles the 32-bit signed integer range constraint ($[-2^{31}, 2^{31} - 1]$).
*   **Edge Case:** If `x = -2147483648`, `x = -x` works in Python (due to arbitrary precision), and the resulting reversed value is checked against the limit, correctly returning `0`.
*   **Minor Note:** The check `I <= -2**31` is redundant because `I` is always positive at that point.

### 3. Optimization
**Eliminate string conversion.** Use mathematical operations (modulo and integer division) to reverse the number. This reduces space complexity to **$O(1)$** and avoids the overhead of object allocation involved in string/list slicing.

### 4. Key Algorithmic Pattern
**String Manipulation** (Type casting and Slicing). Note that in many interview settings, the "Mathematical Digit Extraction" pattern is preferred.
