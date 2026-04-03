# Greatest Common Divisor of Strings

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-greatest-common-divisor-of-strings::1967576641` |
| Topics | Math, String |
| Solved | 2026-04-03 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 32.667100000000005%) |

## Problem Statement

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return _the largest string _`x`_ such that _`x`_ divides both _`str1`_ and _`str2`.

 

**Example 1:**

**Input:** str1 = "ABCABC", str2 = "ABC"

**Output:** "ABC"

**Example 2:**

**Input:** str1 = "ABABAB", str2 = "ABAB"

**Output:** "AB"

**Example 3:**

**Input:** str1 = "LEET", str2 = "CODE"

**Output:** ""

**Example 4:**

**Input:** str1 = "AAAAAB", str2 = "AAA"

**Output:** ""​​​​​​​

 

**Constraints:**

	- `1 <= str1.length, str2.length <= 1000`

	- `str1` and `str2` consist of English uppercase letters.

## Solutions

```Python3
from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1), len(str2))]
        else:
            return ""
```
