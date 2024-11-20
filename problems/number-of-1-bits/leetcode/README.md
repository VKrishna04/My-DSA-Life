# Number of 1 Bits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-number-of-1-bits` |
| Topics | Divide and Conquer, Bit Manipulation |
| Solved | 2025-06-01 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

 

**Example 1:**

**Input:** n = 11

**Output:** 3

**Explanation:**

The input binary string **1011** has a total of three set bits.

**Example 2:**

**Input:** n = 128

**Output:** 1

**Explanation:**

The input binary string **10000000** has a total of one set bit.

**Example 3:**

**Input:** n = 2147483645

**Output:** 30

**Explanation:**

The input binary string **1111111111111111111111111111101** has a total of thirty set bits.

 

**Constraints:**

	- `1 <= n <= 231 - 1`

 

**Follow up:** If this function is called many times, how would you optimize it?

## Solutions

```Python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(k)$, where $k$ is the number of bits in $n$ (for a 32-bit integer, this is effectively $O(1)$). Converting to a string and iterating through it both take linear time relative to the bit length.
*   **Space Complexity:** $O(k)$ to store the intermediate binary string representation.

**2. Correctness**
*   **Edge Cases:** The solution is correct for non-negative integers. If $n=0$, it returns `0`. 
*   **Note:** In Python, `bin(-1)` returns `'-0b1'`. If the problem expects a 32-bit two's complement representation for negative numbers, this approach would fail. However, LeetCode defines $n$ as a positive integer for this problem.

**3. Optimization**
Use **Brian Kernighan’s Algorithm** to avoid string conversion and improve performance when set bits are sparse:
```python
count = 0
while n:
    n &= (n - 1)  # Flips the least significant set bit to 0
    count += 1
return count
```
This runs in $O(\text{set bits})$ time and $O(1)$ space.

**4. Key Algorithmic Pattern**
*   **Bit Manipulation** (via built-in string formatting/parsing).
