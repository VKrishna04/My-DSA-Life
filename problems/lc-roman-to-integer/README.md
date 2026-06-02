# Roman to Integer

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-roman-to-integer` |
| Topics | Hash Table, Math, String |
| Solved | 2024-08-12 |
| Runtime | 56 ms (beats 5.097099999999985%) |
| Memory | 16.6 MB (beats 100%) |

## Problem Statement

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

**Symbol**       **Value**
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

	- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 

	- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 

	- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 

**Example 1:**

**Input:** s = "III"
**Output:** 3
**Explanation:** III = 3.

**Example 2:**

**Input:** s = "LVIII"
**Output:** 58
**Explanation:** L = 50, V= 5, III = 3.

**Example 3:**

**Input:** s = "MCMXCIV"
**Output:** 1994
**Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.

 

**Constraints:**

	- `1 <= s.length <= 15`

	- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.

	- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## Hints

<details>
<summary>Hint 1</summary>

Problem is simpler to solve by working the string from back to front and using a map.

</details>

## Solutions

```Python3
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        resp = 0
        i = 0
        for element in s:

            current = roman[element]

            if i + 1 == len(s):
                resp = resp + current

            elif element == 'C' and (s[i+1] == 'M' or  s[i+1] == 'D'):
                resp = resp - 100

            elif element == 'X' and (s[i+1] == 'L' or  s[i+1] == 'C'):
                resp = resp - 10

            elif element == 'I' and (s[i+1] == 'V' or  s[i+1] == 'X'):
                resp = resp - 1

            else:
                resp = resp + current

            i += 1

        return resp
```

## AI Review

**1. Complexity**
*   **Time Complexity:** $O(n)$, where $n$ is the length of the string. We traverse the string exactly once.
*   **Space Complexity:** $O(1)$. The hash map size is constant (7 symbols), and we use a few integer variables.

**2. Correctness**
The logic is **correct**. It accurately handles the six subtraction instances (IV, IX, XL, XC, CD, CM) and the trailing character edge case. It assumes valid Roman numeral input per LeetCode constraints.

**3. Concrete Optimization**
Simplify the logic by using the general rule: **If a value is followed by a larger value, subtract it; otherwise, add it.** This replaces specific character checks (`element == 'C'`, etc.) with a single comparison.

*Optimized Loop:*
```python
for i in range(len(s)):
    if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
        resp -= roman[s[i]]
    else:
        resp += roman[s[i]]
```

**4. Key Algorithmic Pattern**
*   **Linear Scan with Look-ahead:** Iterating through a sequence while comparing the current element to the next one to determine the operation.
*   **Hash Map Lookup:** Using a dictionary for $O(1)$ mapping of symbols to values.
