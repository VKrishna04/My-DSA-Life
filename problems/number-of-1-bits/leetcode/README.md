# Number of 1 Bits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-number-of-1-bits` |
| Topics | Divide and Conquer, Bit Manipulation |
| Solved | 2025-06-02 |
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

### 1. Complexity
*   **Time Complexity:** $O(k)$, where $k$ is the number of bits in $n$ (for a 32-bit integer, this is effectively $O(1)$). Converting an integer to a string takes time proportional to the number of bits.
*   **Space Complexity:** $O(k)$ to store the intermediate binary string representation.

### 2. Correctness
The code is **correct** for all valid inputs, including the edge case $n = 0$. Since Python integers have arbitrary precision, it handles values beyond 32 bits gracefully.

### 3. Concrete Optimisation
Use **Brian Kernighan’s Algorithm**. Instead of converting to a string, use bitwise operations to clear the least significant set bit in each iteration. This performs exactly as many iterations as there are set bits ($h$):

```python
count = 0
while n:
    n &= (n - 1)  # Flips the least significant '1' to '0'
    count += 1
return count
```
This is more memory-efficient as it avoids string allocation.

### 4. Key Algorithmic Pattern
**String Manipulation / Built-in Primitives.** This approach leverages Python's high-level abstractions to solve a low-level bit manipulation problem.
