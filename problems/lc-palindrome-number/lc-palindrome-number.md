# Palindrome Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-palindrome-number` |
| Topics | Math |
| Solved | 2024-08-10 |
| Runtime | 57 ms (beats 5.443899999999994%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

Given an integer `x`, return `true`_ if _`x`_ is a __**palindrome**__, and _`false`_ otherwise_.

 

**Example 1:**

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

 

**Constraints:**

	- `-231 <= x <= 231 - 1`

 

**Follow up:** Could you solve it without converting the integer to a string?

## Solutions

```Python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
```

## AI Review

### 1. Complexity
*   **Time Complexity:** **$O(d)$**, where $d$ is the number of digits in the integer ($\approx \log_{10}n$). String conversion and slicing both traverse the digits once.
*   **Space Complexity:** **$O(d)$**. Converting the integer to a string and creating its reverse requires memory proportional to the number of digits.

### 2. Correctness
The code is **correct**. 
*   **Edge Cases:** Negative numbers are handled (returns `False`). Single digits and zero are handled (returns `True`). Numbers ending in zero (e.g., 10) correctly return `False`.

### 3. Optimization
To achieve **$O(1)$ space**, avoid string conversion. Revert only the **half** of the integer mathematically.
*   **Logic:** Repeatedly use `x % 10` and `x // 10` to build a reversed number until the reversed part is greater than or equal to the remaining part. This also avoids potential integer overflow in languages other than Python.

### 4. Key Algorithmic Pattern
**String Manipulation / Reversal.** The solution relies on Python's slicing syntax (`[::-1]`) to perform a sequence reversal.
