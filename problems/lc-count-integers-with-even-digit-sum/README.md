# Count Integers With Even Digit Sum

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-count-integers-with-even-digit-sum` |
| Topics | Math, Simulation |
| Solved | 2024-10-20 |
| Runtime | 11 ms (beats 28%) |
| Memory | 16.7 MB (beats 100%) |

## Problem Statement

Given a positive integer `num`, return _the number of positive integers **less than or equal to**_ `num` _whose digit sums are **even**_.

The **digit sum** of a positive integer is the sum of all its digits.

 

**Example 1:**

**Input:** num = 4
**Output:** 2
**Explanation:**
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    

**Example 2:**

**Input:** num = 30
**Output:** 14
**Explanation:**
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

 

**Constraints:**

	- `1 <= num <= 1000`

## Hints

<details>
<summary>Hint 1</summary>

Iterate through all integers from 1 to num.

</details>

<details>
<summary>Hint 2</summary>

For any integer, extract the individual digits to compute their sum and check if it is even.

</details>

## Solutions

```Python3
class Solution:
    def countEven(self, num: int) -> int:
        output = 0
        for i in range(1, num+1):
            digits = list(map(int, str(i)))
            if sum(digits) % 2 == 0:
                output += 1

        return output
```

## AI Review

### 1. Complexity
*   **Time Complexity**: $O(N \log N)$, where $N$ is `num`. The loop runs $N$ times, and for each number, converting it to a string and summing digits takes $O(\log N)$ time (proportional to the number of digits).
*   **Space Complexity**: $O(\log N)$ to store the string and list representation of the digits.

### 2. Correctness
The code is **correct** for the given constraints ($1 \le num \le 1000$). It accurately iterates through the range and checks the parity of each digit sum. No specific edge cases (like $num=1$) fail.

### 3. Concrete Optimization
You can solve this in **$O(\log N)$ time** using a mathematical property: roughly half of the numbers up to $num$ have an even digit sum. Specifically:
*   Calculate the digit sum of `num` itself.
*   If the sum is **even**, the count is `num // 2`.
*   If the sum is **odd**, the count is `(num - 1) // 2`.

**Optimized Code:**
```python
return (num - sum(int(d) for d in str(num)) % 2) // 2
```

### 4. Key Algorithmic Pattern
**Brute Force / Simulation**: The original code iterates through every element in the search space to verify a condition.
