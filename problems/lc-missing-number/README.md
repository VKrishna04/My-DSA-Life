# Missing Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-missing-number` |
| Topics | Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 18.6 MB (beats 100%) |

## Problem Statement

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return _the only number in the range that is missing from the array._

 

**Example 1:**

**Input:** nums = [3,0,1]

**Output:** 2

**Explanation:**

`n = 3` since there are 3 numbers, so all numbers are in the range `[0,3]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 2:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

`n = 2` since there are 2 numbers, so all numbers are in the range `[0,2]`. 2 is the missing number in the range since it does not appear in `nums`.

**Example 3:**

**Input:** nums = [9,6,4,2,3,5,7,0,1]

**Output:** 8

**Explanation:**

`n = 9` since there are 9 numbers, so all numbers are in the range `[0,9]`. 8 is the missing number in the range since it does not appear in `nums`.

 

 

 

 

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 104`

	- `0 <= nums[i] <= n`

	- All the numbers of `nums` are **unique**.

 

**Follow up:** Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## Solutions

```Python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        exs = s * ( s + 1) // 2
        return exs - sum ( nums )
```

## AI Review

### Review
**1. Complexity**
*   **Time:** $O(n)$ — Requires a single pass through the list to calculate the sum.
*   **Space:** $O(1)$ — Only stores a few integer variables regardless of input size.

**2. Correctness**
The solution is **correct**. It leverages Gauss' Summation Formula to find the expected sum of the first $n$ natural numbers.
*   **Edge Cases:** It correctly handles cases where the missing number is `0` or `n` (the boundaries). 
*   **Overflow:** While large sums can overflow 32-bit/64-bit integers in languages like C++ or Java, Python handles arbitrarily large integers, making this implementation robust.

**3. Optimization**
The current approach is already optimal for Python. However, in environments with fixed-width integers, you could use **Bitwise XOR** to prevent potential overflow:
```python
res = len(nums)
for i, num in enumerate(nums):
    res ^= i ^ num
return res
```
This performs the same logic without calculating large sums.

**4. Key Algorithmic Pattern**
**Mathematical/Summation Formula:** Using the property that the sum of a sequence $0 \dots n$ is $\frac{n(n+1)}{2}$.
