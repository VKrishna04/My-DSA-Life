# Power of Four

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-power-of-four` |
| Topics | Math, Bit Manipulation, Recursion |
| Solved | 2025-06-02 |
| Runtime | 2 ms (beats 17.511499999999998%) |
| Memory | 17.8 MB (beats 100%) |

## Problem Statement

Given an integer `n`, return _`true` if it is a power of four. Otherwise, return `false`_.

An integer `n` is a power of four, if there exists an integer `x` such that `n == 4x`.

 

**Example 1:**

**Input:** n = 16
**Output:** true
**Example 2:**

**Input:** n = 5
**Output:** false
**Example 3:**

**Input:** n = 1
**Output:** true

 

**Constraints:**

	- `-231 <= n <= 231 - 1`

 

**Follow up:** Could you solve it without loops/recursion?

## Solutions

```Python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
       
        if n not in [4**i for i in range(int(math.log(2**31,4))+1)]:
            return False
        return True

        # return n>0 and (n & (n-1)==0) and (n % 3 == 1)
```

## AI Review

### Review of "Power of Four" Solution

1.  **Complexity**
    *   **Time:** $O(1)$. The loop runs a fixed number of times (~16 iterations) regardless of the input $n$.
    *   **Space:** $O(1)$. A small list of constant size is created.

2.  **Correctness**
    *   **Runtime Error:** The code will fail because `math` is not imported.
    *   **Logic:** Once imported, it is correct. It handles $n \le 0$ and non-powers correctly by exclusion from the precomputed list.
    *   **Constraint Note:** Since $n$ is a 32-bit signed integer, the maximum power is $4^{15}$. Your range `range(16)` covers this.

3.  **Optimization**
    Use the commented-out **Bit Manipulation** approach. It avoids list creation and log calculations entirely:
    ```python
    return n > 0 and (n & (n - 1) == 0) and (n % 3 == 1)
    ```
    *   `n & (n - 1) == 0` checks if $n$ is a power of two.
    *   `n % 3 == 1` distinguishes powers of four from other powers of two.

4.  **Key Algorithmic Pattern**
    **Precomputation / Lookup Table.** The solution generates all possible valid answers within the problem's constraints and performs a membership check.
