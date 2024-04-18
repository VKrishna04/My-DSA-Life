# Score of a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-score-of-a-string::1235831135` |
| Topics | String |
| Solved | 2024-04-18 |
| Runtime | 1 ms (beats 99.8053%) |
| Memory | 42.5 MB (beats 99.80510000000001%) |

## Problem Statement

You are given a string `s`. The **score** of a string is defined as the sum of the absolute difference between the **ASCII** values of adjacent characters.

Return the **score** of_ _`s`.

 

**Example 1:**

**Input:** s = "hello"

**Output:** 13

**Explanation:**

The **ASCII** values of the characters in `s` are: `'h' = 104`, `'e' = 101`, `'l' = 108`, `'o' = 111`. So, the score of `s` would be `|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13`.

**Example 2:**

**Input:** s = "zaz"

**Output:** 50

**Explanation:**

The **ASCII** values of the characters in `s` are: `'z' = 122`, `'a' = 97`. So, the score of `s` would be `|122 - 97| + |97 - 122| = 25 + 25 = 50`.

 

**Constraints:**

	- `2 <= s.length <= 100`

	- `s` consists only of lowercase English letters.

## Solutions

```Java
class Solution {
    public int scoreOfString(String s) {
        int score = 0;
        for (int i = 0; i < s.length()-1; i++){
            score += Math.abs((int)s.charAt(i)-(int)s.charAt(i+1));
        }
        return score;
    }
}
```
