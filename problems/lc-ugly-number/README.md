# Ugly Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-ugly-number` |
| Topics | Math |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

An **ugly number** is a _positive_ integer which does not have a prime factor other than 2, 3, and 5.

Given an integer `n`, return `true` _if_ `n` _is an **ugly number**_.

 

**Example 1:**

**Input:** n = 6
**Output:** true
**Explanation:** 6 = 2 &times; 3

**Example 2:**

**Input:** n = 1
**Output:** true
**Explanation:** 1 has no prime factors.

**Example 3:**

**Input:** n = 14
**Output:** false
**Explanation:** 14 is not ugly since it includes the prime factor 7.

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

## Solutions

```Python3
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        while n>0:
            if n%2==0:
                n//=2
            elif n%3==0:
                n//=3
            elif n%5==0:
                n//=5
            else:
                break
        return n==1
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(\log n)$. Each division step significantly reduces $n$. The number of iterations is proportional to the sum of the exponents in the prime factorization of $n$ for bases 2, 3, and 5.
*   **Space Complexity:** $O(1)$. No additional data structures are used.

### 2. Correctness
The solution is **correct**. 
*   **Edge Cases:** Non-positive integers ($n \le 0$) are correctly identified as `False`. The base case $n=1$ is correctly identified as `True`. 
*   **Logic:** It effectively strips all prime factors of 2, 3, and 5. If any prime factor $> 5$ exists, $n$ will terminate at a value $> 1$, returning `False`.

### 3. Concrete Optimization
Use a loop to iterate over the prime factors to make the code more DRY (Don't Repeat Yourself) and slightly more efficient if additional factors were needed:
```python
for p in [2, 3, 5]:
    while n % p == 0:
        n //= p
```
This avoids redundant checks once a factor is exhausted.

### 4. Key Algorithmic Pattern
**Greedy Reduction / Prime Factorization.** The algorithm repeatedly reduces the problem size by removing specific allowed prime factors until it reaches an irreducible state.
