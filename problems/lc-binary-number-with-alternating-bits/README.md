# Binary Number with Alternating Bits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-binary-number-with-alternating-bits` |
| Topics | Bit Manipulation |
| Solved | 2025-06-02 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

**Example 1:**

**Input:** n = 5
**Output:** true
**Explanation:** The binary representation of 5 is: 101

**Example 2:**

**Input:** n = 7
**Output:** false
**Explanation:** The binary representation of 7 is: 111.

**Example 3:**

**Input:** n = 11
**Output:** false
**Explanation:** The binary representation of 11 is: 1011.

 

**Constraints:**

	- `1 <= n <= 231 - 1`

## Solutions

```Python3
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x+1)) == 0
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(1)$. Bitwise operations on fixed-width integers (32-bit for most LeetCode cases) are constant time.
*   **Space Complexity:** $O(1)$. No additional data structures are used.

### 2. Correctness
The logic is sound. 
*   If bits alternate (e.g., `1010`), shifting by one and XORing results in a block of ones (`1111`).
*   The expression `(x & (x + 1)) == 0` is a classic bitwise trick to check if a number consists entirely of set bits (all ones).
*   **Edge Cases:** For $n=1$ (binary `1`), it returns `True`. For $n=0$ (if applicable), it returns `True`. Large integers are handled by Python's arbitrary-precision arithmetic.

### 3. Optimization
This solution is already **mathematically optimal**. It avoids loops and string conversions, making it faster than iterative $O(\log n)$ approaches. No further optimizations are required.

### 4. Key Algorithmic Pattern
**Bit Manipulation:** Specifically, using the **XOR shift** property to identify patterns and the **power-of-two/all-ones** check (`x & (x+1)`) to validate the resulting bitmask.
