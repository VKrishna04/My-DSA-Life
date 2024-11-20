# Reverse Bits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-bits` |
| Topics | Divide and Conquer, Bit Manipulation |
| Solved | 2025-06-01 |
| Runtime | 46 ms (beats 57.6247%) |
| Memory | 17.7 MB (beats 100%) |

## Problem Statement

Reverse bits of a given 32 bits signed integer.

 

**Example 1:**

**Input:** n = 43261596

**Output:** 964176192

**Explanation:**

	
		
			Integer
			Binary
		
		
			43261596
			00000010100101000001111010011100
		
		
			964176192
			00111001011110000010100101000000
		
	

**Example 2:**

**Input:** n = 2147483644

**Output:** 1073741822

**Explanation:**

	
		
			Integer
			Binary
		
		
			2147483644
			01111111111111111111111111111100
		
		
			1073741822
			00111111111111111111111111111110
		
	

 

**Constraints:**

	- `0 <= n <= 231 - 2`

	- `n` is even.

 

**Follow up:** If this function is called many times, how would you optimize it?

## Solutions

```Python3
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
```

## AI Review

### Review of Reverse Bits Solution

1.  **Complexity:**
    *   **Time Complexity:** $O(1)$. The loop runs exactly 32 iterations, regardless of the input value.
    *   **Space Complexity:** $O(1)$. It uses a single integer variable `res` for the result.

2.  **Correctness:**
    The solution is **correct**. By iterating a fixed 32 times, it correctly handles trailing and leading zeros, ensuring the output is always treated as a 32-bit unsigned integer. No edge cases (like $n=0$ or $n=2^{32}-1$) fail.

3.  **Optimization:**
    **Divide and Conquer (Bit Masking):** Instead of bit-by-bit, reverse chunks of bits (16-bit, 8-bit, 4-bit, 2-bit, then 1-bit) using masks. This reduces the process to 5 steps:
    ```python
    n = (n >> 16) | (n << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    ```
    This is faster than a loop in high-performance or hardware-level scenarios.

4.  **Key Algorithmic Pattern:**
    **Bit Manipulation.** Specifically, bitwise construction using **shifts** (`<<`, `>>`) and **masks** (`&`, `|`).
