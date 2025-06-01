# Reverse Bits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-bits::1650957577` |
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
