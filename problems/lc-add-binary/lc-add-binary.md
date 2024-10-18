# Add Binary

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-add-binary` |
| Topics | Math, String, Bit Manipulation, Simulation |
| Solved | 2024-10-18 |
| Runtime | 4 ms (beats 14.163000000000004%) |
| Memory | 16.8 MB (beats 100%) |

## Problem Statement

Given two binary strings `a` and `b`, return _their sum as a binary string_.

 

**Example 1:**

**Input:** a = "11", b = "1"
**Output:** "100"
**Example 2:**

**Input:** a = "1010", b = "1011"
**Output:** "10101"

 

**Constraints:**

	- `1 <= a.length, b.length <= 104`

	- `a` and `b` consist only of `'0'` or `'1'` characters.

	- Each string does not contain leading zeros except for the zero itself.

## Solutions

```Python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
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
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append(str(carry))

        return "".join(result[::-1])
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(\max(N, M))$, where $N$ and $M$ are lengths of `a` and `b`. The code performs linear passes for reversing, iterating, and joining.
*   **Space:** $O(\max(N, M))$ to store reversed lists and the result array.

**2. Correctness**
The logic is correct. It handles varying string lengths via the swap/padding check and correctly processes the final carry.
*   **Edge Cases:** Handles "0" + "0", different lengths (e.g., "1" + "111"), and carry-out at the most significant bit (e.g., "11" + "1") successfully.

**3. Concrete Optimization**
Avoid the memory overhead of creating reversed lists (`list(a)[::-1]`). Instead, use **two pointers** to iterate backwards through the strings. This processes the bits in-place relative to their original strings.

**4. Key Algorithmic Pattern**
**Simulation (Elementary School Addition):** It mimics the column-by-column manual addition process, maintaining a carry bit while moving from the least significant to the most significant digit.
