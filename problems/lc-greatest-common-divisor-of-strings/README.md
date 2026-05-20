# Greatest Common Divisor of Strings

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-greatest-common-divisor-of-strings` |
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

## Hints

<details>
<summary>Hint 1</summary>

The greatest common divisor must be a prefix of each string, so we can try all prefixes.

</details>

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

## AI Review

### 1. Complexity
*   **Time:** $O(N + M)$, where $N$ and $M$ are the lengths of `str1` and `str2`. String concatenation and comparison both take linear time. The GCD calculation is $O(\log(\min(N, M)))$.
*   **Space:** $O(N + M)$ to store the concatenated strings `str1 + str2` and `str2 + str1`.

### 2. Correctness
The solution is **correct**. The condition `str1 + str2 == str2 + str1` is a known mathematical property: two strings $S$ and $T$ commute if and only if they are powers of the same base string. If they commute, the length of the greatest common divisor string must be `gcd(len(str1), len(str2))`.

### 3. Optimization
To improve **space complexity** from $O(N+M)$ to $O(GCD)$, you can avoid full concatenation. Instead, verify if the prefix of length $g = \gcd(len_1, len_2)$ can construct both strings:
```python
g = gcd(len(str1), len(str2))
pattern = str1[:g]
if pattern * (len(str1) // g) == str1 and pattern * (len(str2) // g) == str2:
    return pattern
```
While this still uses memory for multiplication, it avoids creating the $N+M$ strings.

### 4. Key Algorithmic Pattern
**Mathematical Property of Strings / Number Theory.** It leverages the relationship between string periodicity and the greatest common divisor of their lengths.
