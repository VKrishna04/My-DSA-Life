# Happy Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-happy-number::1428234006` |
| Topics | Hash Table, Math, Two Pointers |
| Solved | 2024-10-20 |
| Runtime | 1 ms (beats 52%) |
| Memory | 16.4 MB (beats 100%) |

## Problem Statement

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

	- Starting with any positive integer, replace the number by the sum of the squares of its digits.

	- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.

	- Those numbers for which this process **ends in 1** are happy.

Return `true` _if_ `n` _is a happy number, and_ `false` _if not_.

 

**Example 1:**

**Input:** n = 19
**Output:** true
**Explanation:**
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

**Example 2:**

**Input:** n = 2
**Output:** false

 

**Constraints:**

	- `1 <= n <= 231 - 1`

## Solutions

```Python3
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(_) ** 2 for _ in str(n))

        # while n > 9: n = sum(int(d) ** 2 for d in str(n))
        if n == 1:
            return True
        return False
```
