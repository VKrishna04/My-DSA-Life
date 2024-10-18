# Add Strings

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-add-strings` |
| Topics | Math, String, Simulation |
| Solved | 2024-10-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.3 MB (beats 100%) |

## Problem Statement

Given two non-negative integers, `num1` and `num2` represented as string, return _the sum of_ `num1` _and_ `num2` _as a string_.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`). You must also not convert the inputs to integers directly.

 

**Example 1:**

**Input:** num1 = "11", num2 = "123"
**Output:** "134"

**Example 2:**

**Input:** num1 = "456", num2 = "77"
**Output:** "533"

**Example 3:**

**Input:** num1 = "0", num2 = "0"
**Output:** "0"

 

**Constraints:**

	- `1 <= num1.length, num2.length <= 104`

	- `num1` and `num2` consist of only digits.

	- `num1` and `num2` don't have any leading zeros except for the zero itself.

## Solutions

```Python3
class Solution:
    def addStrings(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        
        carry = 0
        result = []
        a = list(a)[::-1]
        b = list(b)[::-1]

        for i in range(len(a)):
            bit_a = int(a[i])
            bit_b = int(b[i]) if i < len(b) else 0
            total = bit_a + bit_b + int(carry)
            result.append(str(total % 10))
            carry = total // 10

        if carry:
            result.append(str(carry))

        return "".join(result[::-1])
```

## AI Review

### 1. Complexity
*   **Time:** $O(\max(N, M))$, where $N$ and $M$ are the lengths of strings `a` and `b`. Each digit is processed exactly once.
*   **Space:** $O(\max(N, M))$ to store the intermediate reversed lists and the final result list.

### 2. Correctness
**Correct.** The logic successfully handles:
*   Numbers of different lengths (via the `i < len(b)` check).
*   Carries within the addition.
*   A final carry that increases the total digit count (e.g., "9" + "1").
*   Leading zeros (though the problem usually guarantees valid inputs).

### 3. Optimization
Instead of creating reversed list copies (`list(a)[::-1]`), use **two pointers** starting at the end of each string (`len(a) - 1` and `len(b) - 1`) and iterate backwards. This reduces the number of intermediate object allocations and overhead.

### 4. Key Algorithmic Pattern
**Simulation (Schoolbook Addition):** The algorithm mimics the manual process of adding numbers column-by-column from right to left, maintaining a carry.
