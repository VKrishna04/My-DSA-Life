# Find Greatest Common Divisor of Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-greatest-common-divisor-of-array` |
| Topics | Array, Math, Number Theory |
| Solved | 2026-04-03 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 80.2024%) |

## Problem Statement

Given an integer array `nums`, return** **_the **greatest common divisor** of the smallest number and largest number in _`nums`.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

 

**Example 1:**

**Input:** nums = [2,5,6,9,10]
**Output:** 2
**Explanation:**
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

**Example 2:**

**Input:** nums = [7,5,6,8,3]
**Output:** 1
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

**Example 3:**

**Input:** nums = [3,3]
**Output:** 3
**Explanation:**
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

 

**Constraints:**

	- `2 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

## Hints

<details>
<summary>Hint 1</summary>

Find the minimum and maximum in one iteration. Let them be mn and mx.

</details>

<details>
<summary>Hint 2</summary>

Try all the numbers in the range [1, mn] and check the largest number which divides both of them.

</details>

## Solutions

```Python3
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        l = max(nums)

        while (l != 0):
            s, l = l, s % l
        return s

        # Using built in functions
        # from math import gcd
        # return gcd(min(nums), max(nums))

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n + \log(\min(s, l)))$, where $n$ is the length of `nums`. Finding the min and max takes $O(n)$, and the Euclidean algorithm takes logarithmic time relative to the magnitude of the numbers.
*   **Space Complexity:** $O(1)$, as only two integer variables are stored regardless of input size.

### 2. Correctness
The logic is **correct**. It successfully identifies the smallest and largest elements and applies the Euclidean algorithm. 
*   **Edge Cases:** The constraints for this problem ($2 \le nums.length$ and $1 \le nums[i]$) ensure the array is never empty and numbers are positive, preventing division-by-zero errors.

### 3. Optimization
While your manual implementation is correct, using the built-in **`math.gcd()`** function is the primary optimization. It is implemented in C, making it significantly faster than a Python `while` loop. Additionally, you can find `min` and `max` in a single pass to reduce constant time, though $O(n)$ remains the same.

### 4. Key Algorithmic Pattern
**Euclidean Algorithm:** An efficient method for computing the greatest common divisor of two integers by repeatedly replacing the larger number with the remainder of its division by the smaller number.
