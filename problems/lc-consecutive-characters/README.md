# Consecutive Characters

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-consecutive-characters` |
| Topics | String |
| Solved | 2025-09-06 |
| Runtime | 2 ms (beats 87.2789%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

The **power** of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string `s`, return _the **power** of_ `s`.

 

**Example 1:**

**Input:** s = "leetcode"
**Output:** 2
**Explanation:** The substring "ee" is of length 2 with the character 'e' only.

**Example 2:**

**Input:** s = "abbcccddddeeeeedcba"
**Output:** 5
**Explanation:** The substring "eeeee" is of length 5 with the character 'e' only.

 

**Constraints:**

	- `1 <= s.length <= 500`

	- `s` consists of only lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Keep an array power where power[i] is the maximum power of the i-th character.

</details>

<details>
<summary>Hint 2</summary>

The answer is max(power[i]).

</details>

## Solutions

```Python3
class Solution:
    def maxPower(self, s: str) -> int:
        mc = c = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                c+= 1
                mc = max(mc,c)
            else:
                c = 1
        return mc
```

## AI Review

**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the length of the string, as we traverse the input once.
*   **Space:** $O(1)$, as we only store two integer variables.

**2. Correctness**
The logic is correct for the given LeetCode constraints ($1 \le s.length$). 
*   **Single character:** Loop doesn't run; returns 1. Correct.
*   **All same characters:** `mc` updates correctly. Correct.
*   **Edge Case:** If the input were an empty string, it would incorrectly return 1. However, the problem guarantees a minimum length of 1.

**3. Optimization**
Replace the `max()` function call with a manual `if` check inside the `else` block and one final check after the loop. 
```python
if s[i] == s[i-1]:
    c += 1
else:
    if c > mc: mc = c
    c = 1
return max(mc, c)
```
Calling `max()` on every identical character iteration is less efficient in Python than updating only when a streak ends.

**4. Key Pattern**
**Single-pass (One-pass) iteration** with a **Greedy** tracking of the current streak.
