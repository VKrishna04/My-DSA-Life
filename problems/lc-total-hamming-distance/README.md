# Total Hamming Distance

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-total-hamming-distance` |
| Topics | Array, Math, Bit Manipulation |
| Solved | 2025-06-02 |
| Runtime | 114 ms (beats 91.95130000000006%) |
| Memory | 20.1 MB (beats 100%) |

## Problem Statement

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given an integer array `nums`, return _the sum of **Hamming distances** between all the pairs of the integers in_ `nums`.

 

**Example 1:**

**Input:** nums = [4,14,2]
**Output:** 6
**Explanation:** In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).
The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

**Example 2:**

**Input:** nums = [4,14,4]
**Output:** 4

 

**Constraints:**

	- `1 <= nums.length <= 104`

	- `0 <= nums[i] <= 109`

	- The answer for the given input will fit in a **32-bit** integer.

## Solutions

```Python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        return  sum(i.count('1') * i.count('0') for i in zip(*map('{:032b}'.format,nums)))

```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(N \cdot K)$, where $N$ is the number of elements and $K$ is the bit-length (32). Each number is processed for each bit.
*   **Space:** $O(N \cdot K)$. The `map` and `zip(*...)` construct creates $N$ strings and a transposed structure of $32 \times N$ characters in memory.

**2. Correctness**
*   **Correct.** The logic relies on the fact that the total Hamming distance is the sum of distances at each bit position. For a specific bit, the distance is the number of pairs $(0, 1)$, which equals `(count of 0s) * (count of 1s)`.
*   **Edge cases:** Works for empty lists (returns 0) or lists with identical numbers.

**3. Optimization**
*   **Bitwise Operations:** String formatting is computationally expensive. Use bitwise shifts to count bits in $O(1)$ auxiliary space:
    ```python
    total = 0
    for i in range(32):
        ones = sum((n >> i) & 1 for n in nums)
        total += ones * (len(nums) - ones)
    return total
    ```
    This avoids $O(N)$ string allocations.

**4. Key Algorithmic Pattern**
*   **Bit Manipulation (Contribution of Each Bit):** Instead of comparing $O(N^2)$ pairs, calculate how much each bit position contributes to the total sum independently.
