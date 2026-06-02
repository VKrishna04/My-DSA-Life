# Add Digits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-add-digits` |
| Topics | Math, Simulation, Number Theory |
| Solved | 2024-10-20 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.6 MB (beats 100%) |

## Problem Statement

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

 

**Example 1:**

**Input:** num = 38
**Output:** 2
**Explanation:** The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

**Example 2:**

**Input:** num = 0
**Output:** 0

 

**Constraints:**

	- `0 <= num <= 231 - 1`

 

**Follow up:** Could you do it without any loop/recursion in `O(1)` runtime?

## Hints

<details>
<summary>Hint 1</summary>

A naive implementation of the above process is trivial. Could you come up with other methods?

</details>

<details>
<summary>Hint 2</summary>

What are all the possible results?

</details>

<details>
<summary>Hint 3</summary>

How do they occur, periodically or randomly?

</details>

<details>
<summary>Hint 4</summary>

You may find this Wikipedia article useful.

</details>

## Solutions

```Python3
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = sum(int(_) for _ in str(num))

        # while num > 9: num = sum(int(d) for d in str(num))
        return num
```

## AI Review

### Analysis of "Add Digits" Solution

**1. Complexity**
*   **Time Complexity:** $O(\log n)$. The number of digits in $n$ is $\lfloor\log_{10} n\rfloor + 1$. While the outer loop runs very few times (the sum of digits drops drastically), the inner string conversion and summation scale with the number of digits.
*   **Space Complexity:** $O(\log n)$ to store the string representation of the number during iteration.

**2. Correctness**
*   The logic is **correct**. It handles the smallest input ($0$) correctly because `len("0") == 1`, exiting the loop immediately. It correctly reduces any positive integer to a single digit.

**3. Optimization**
The problem can be solved in **$O(1)$ time and space** using the **Digital Root** mathematical formula:
```python
return 1 + (num - 1) % 9 if num > 0 else 0
```
This avoids string conversions and loops entirely by leveraging the property that a number is congruent to the sum of its digits modulo 9.

**4. Key Algorithmic Pattern**
*   **Simulation / Iterative Reduction:** The code repeatedly applies a transformation (summing digits) until a specific termination condition (single digit) is met.
