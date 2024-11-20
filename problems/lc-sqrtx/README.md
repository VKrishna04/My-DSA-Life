# Sqrt(x)

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-sqrtx` |
| Topics | Math, Binary Search |
| Solved | 2025-08-13 |
| Runtime | 3 ms (beats 67.64080000000001%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Given a non-negative integer `x`, return _the square root of _`x`_ rounded down to the nearest integer_. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

	- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

 

**Example 1:**

**Input:** x = 4
**Output:** 2
**Explanation:** The square root of 4 is 2, so we return 2.

**Example 2:**

**Input:** x = 8
**Output:** 2
**Explanation:** The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

**Constraints:**

	- `0 <= x <= 231 - 1`

## Hints

<details>
<summary>Hint 1</summary>

Try exploring all integers. (Credits: @annujoshi)

</details>

<details>
<summary>Hint 2</summary>

Use the sorted property of integers to reduced the search space. (Credits: @annujoshi)

</details>

## Solutions

```Python3
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1
        return right

```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(\log x)$. The search space is halved in each iteration.
*   **Space Complexity:** $O(1)$. It uses a constant amount of extra space.

**2. Correctness**
The logic is robust.
*   **Edge Cases:** $x=0$ and $x=1$ are handled by the initial condition. For $x=2$ or $x=3$, the loop correctly converges to `right = 1`. 
*   **Overflow:** Using `mid == x // mid` instead of `mid * mid == x` prevents potential integer overflow in languages with fixed-width integers, though Python handles arbitrary precision.

**3. Optimization**
Set the initial `right` boundary to `x // 2` for $x \ge 4$. Since $\sqrt{x} \le x/2$ for all $x \ge 4$, this halves the initial search space.
```python
if x < 2: return x
left, right = 2, x // 2
```

**4. Key Algorithmic Pattern**
**Binary Search on Answer Space.** Instead of searching through an array, the algorithm performs a binary search over the range of possible integer results $[1, x]$.
