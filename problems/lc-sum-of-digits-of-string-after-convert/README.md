# Sum of Digits of String After Convert

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-sum-of-digits-of-string-after-convert` |
| Topics | String, Simulation |
| Solved | 2024-10-20 |
| Runtime | 3 ms (beats 58%) |
| Memory | 16.6 MB (beats 100%) |

## Problem Statement

You are given a string `s` consisting of lowercase English letters, and an integer `k`. Your task is to _convert_ the string into an integer by a special process, and then _transform_ it by summing its digits repeatedly `k` times. More specifically, perform the following steps:

	- **Convert** `s` into an integer by replacing each letter with its position in the alphabet (i.e. replace `'a'` with `1`, `'b'` with `2`, ..., `'z'` with `26`).

	- **T****ransform** the integer by replacing it with the **sum of its digits**.

	- Repeat the **transform** operation (step 2) `k`** times** in total.

For example, if `s = "zbax"` and `k = 2`, then the resulting integer would be `8` by the following operations:

	- **Convert**: `"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124`

	- **Transform #1**: `262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17`

	- **Transform #2**: `17 ➝ 1 + 7 ➝ 8`

Return the **resulting** **integer** after performing the **operations** described above.

 

**Example 1:**

**Input:** s = "iiii", k = 1

**Output:** 36

**Explanation:**

The operations are as follows:

- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999

- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36

Thus the resulting integer is 36.

**Example 2:**

**Input:** s = "leetcode", k = 2

**Output:** 6

**Explanation:**

The operations are as follows:

- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545

- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33

- Transform #2: 33 ➝ 3 + 3 ➝ 6

Thus the resulting integer is 6.

**Example 3:**

**Input:** s = "zbax", k = 2

**Output:** 8

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `1 <= k <= 10`

	- `s` consists of lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

First, let's note that after the first transform the value will be at most 100 * 10 which is not much

</details>

<details>
<summary>Hint 2</summary>

After The first transform, we can just do the rest of the transforms by brute force

</details>

## Solutions

```Python3
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = int(''.join(str(ord(c) - ord('a') + 1) for c in s))
        for i in range(k):
            num = sum(int(digit) for digit in str(num))
        return num
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n + k \log n)$, where $n$ is the length of $s$. The first transformation takes $O(n)$. Each subsequent $k$ iteration processes $O(\log n)$ digits.
*   **Space Complexity:** $O(n)$ to store the concatenated numeric string before the first summation.

### 2. Correctness
*   **Edge Cases:** The code is logically correct. However, for extremely long strings (length $> 4300$), Python's `int()` conversion would raise a `ValueError` due to the `sys.set_int_max_str_digits` limit. For LeetCode's constraints ($n \le 100$), it works fine.

### 3. Optimization
Instead of creating a massive integer in the first step, calculate the **initial sum of digits** directly. This avoids large integer overhead and potential conversion errors.

```python
# Direct sum for the first pass
num = sum(int(d) for c in s for d in str(ord(c) - ord('a') + 1))
for _ in range(k - 1): # k-1 because we already did the first sum
    num = sum(int(digit) for digit in str(num))
```

### 4. Key Algorithmic Pattern
**Simulation / Digit Manipulation:** The problem requires following a specific sequence of string-to-integer transformations and iterative digit processing.
