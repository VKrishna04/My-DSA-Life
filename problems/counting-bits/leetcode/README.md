# Counting Bits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-counting-bits` |
| Topics | Dynamic Programming, Bit Manipulation |
| Solved | 2025-06-01 |
| Runtime | 11 ms (beats 29.637399999999992%) |
| Memory | 18.5 MB (beats 100%) |

## Problem Statement

Given an integer `n`, return _an array _`ans`_ of length _`n + 1`_ such that for each _`i`_ _(`0 <= i <= n`)_, _`ans[i]`_ is the **number of **_`1`_**'s** in the binary representation of _`i`.

 

**Example 1:**

**Input:** n = 2
**Output:** [0,1,1]
**Explanation:**
0 --> 0
1 --> 1
2 --> 10

**Example 2:**

**Input:** n = 5
**Output:** [0,1,1,2,1,2]
**Explanation:**
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

 

**Constraints:**

	- `0 <= n <= 105`

 

**Follow up:**

	- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?

	- Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?

## Hints

<details>
<summary>Hint 1</summary>

You should make use of what you have produced already.

</details>

<details>
<summary>Hint 2</summary>

Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.

</details>

<details>
<summary>Hint 3</summary>

Or does the odd/even status of the number help you in calculating the number of 1s?

</details>

## Solutions

```Python3
class Solution:
    def countBits(self, n: int) -> List[int]:     

        return [bin(i).count('1') for i in range(n+1)]
```

## AI Review

### Analysis

1.  **Complexity**
    *   **Time Complexity:** $O(n \log n)$. For each number $i$ up to $n$, the `bin(i)` and `count('1')` operations take $O(\text{number of bits})$, which is $O(\log i)$. Summing this over $n$ yields $O(n \log n)$.
    *   **Space Complexity:** $O(1)$ extra space (excluding the $O(n)$ space required for the output list).

2.  **Correctness**
    The solution is **correct** for all valid inputs ($n \ge 0$). It handles the edge case $n=0$ correctly, returning `[0]`.

3.  **Optimization**
    Improve time complexity to **$O(n)$** using **Dynamic Programming**. Instead of recomputing bits, use the relation that the number of bits in $i$ is the number of bits in $i // 2$ plus the last bit:
    ```python
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res
    ```

4.  **Key Algorithmic Pattern**
    *   **Current Code:** Brute Force / Built-in Bit Manipulation.
    *   **Optimal Approach:** Dynamic Programming (using the "Most Significant Bit" or "Least Significant Bit" transition).
