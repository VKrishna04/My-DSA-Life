# Score of a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-score-of-a-string` |
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

## Hints

<details>
<summary>Hint 1</summary>

Sum the difference between all the adjacent characters by just taking the absolute difference of their ASCII values.

</details>

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

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N)$, where $N$ is the length of the string. The algorithm performs a single pass through the string.
*   **Space Complexity:** $O(1)$, as it uses a constant amount of extra space regardless of input size.

### 2. Correctness
The code is **correct**. 
*   **Edge Cases:** The problem constraints specify $2 \le s.length \le 100$, so the loop `i < s.length() - 1` will always execute at least once, avoiding index issues.
*   **Overflow:** Since the maximum ASCII difference is 25 ('z' - 'a') and the max length is 100, the maximum score is $\approx 2,475$, which fits safely within a standard 32-bit `int`.

### 3. Optimization
While the current solution is efficient, you can slightly improve performance by converting the string to a character array using **`s.toCharArray()`** before the loop. This avoids the overhead of repeated `charAt()` method calls and the internal bounds checking performed by the `String` class.

### 4. Key Algorithmic Pattern
**Linear Scan (Adjacent Element Traversal):** The pattern involves iterating through a sequence once while comparing or calculating values between neighboring elements.
