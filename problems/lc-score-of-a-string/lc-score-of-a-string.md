# Score of a String

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-score-of-a-string` |
| Topics | String |
| Solved | 2024-04-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 5.7 MB (beats 100%) |

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

```C
#include <stdlib.h>

int scoreOfString(char* s) {
    int len=strlen(s);
    int score=0;
    for (int i = 0; i< len-1; i++){
        score+=abs((int)s[i]-(int)s[i+1]);
    }
    return score;
}
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N)$, where $N$ is the length of the string. `strlen` takes $O(N)$ and the loop runs $N-1$ times.
*   **Space Complexity:** $O(1)$, as it uses a constant amount of extra space.

### 2. Correctness
The solution is **correct** and follows the problem requirements.
*   **Edge Cases:**
    *   **Length = 2:** Smallest valid input per constraints; handles one subtraction correctly.
    *   **Length = 1:** If allowed, the loop condition (`i < len-1`) correctly skips execution and returns `0`.
    *   **Character Values:** ASCII values are within `0-127`, so `s[i] - s[i+1]` will never overflow a standard `int`.

### 3. Optimization
**Avoid `strlen`:** You can calculate the score in a single pass without pre-calculating the length. This avoids traversing the string twice.
```c
int scoreOfString(char* s) {
    int score = 0;
    for (int i = 0; s[i] && s[i+1]; i++) {
        score += abs(s[i] - s[i+1]);
    }
    return score;
}
```

### 4. Key Algorithmic Pattern
**Iterative Adjacent Traversal:** A variation of the **Sliding Window** (size 2), where you process pairs of neighboring elements sequentially.
