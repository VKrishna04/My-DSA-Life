# Ugly Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-ugly-number::1626696575` |
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
