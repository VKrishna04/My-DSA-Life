# Happy Number

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-happy-number` |
| Topics | Hash Table, Math, Two Pointers |
| Solved | 2024-10-20 |
| Runtime | 1 ms (beats 52%) |
| Memory | 16.4 MB (beats 100%) |

## Problem Statement

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

	- Starting with any positive integer, replace the number by the sum of the squares of its digits.

	- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.

	- Those numbers for which this process **ends in 1** are happy.

Return `true` _if_ `n` _is a happy number, and_ `false` _if not_.

 

**Example 1:**

**Input:** n = 19
**Output:** true
**Explanation:**
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

**Example 2:**

**Input:** n = 2
**Output:** false

 

**Constraints:**

	- `1 <= n <= 231 - 1`

## Solutions

```Python3
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(_) ** 2 for _ in str(n))

        # while n > 9: n = sum(int(d) ** 2 for d in str(n))
        if n == 1:
            return True
        return False
```

## AI Review

### Review of "Happy Number" Solution

**1. Complexity**
*   **Time Complexity:** $O(\log n)$. For any number, the sum of the squares of its digits drops rapidly (e.g., $999 \to 243$). The number of digits in $n$ is $\lfloor \log_{10} n \rfloor + 1$.
*   **Space Complexity:** $O(\log n)$. In the worst case, the `seen` set stores all unique values encountered before a cycle or 1 is reached.

**2. Correctness**
*   **Correct.** The logic effectively handles the two possible outcomes: reaching 1 (Happy) or entering an infinite loop (Unhappy).
*   **Edge Cases:** Handles $n=1$ immediately. It also works for very large integers as the sum of squares of digits shrinks them quickly into a manageable range.

**3. Optimization**
*   **Mathematical Extraction:** Replace `sum(int(_) ** 2 for _ in str(n))` with a `while` loop using `divmod(n, 10)`. String conversion is relatively expensive due to object allocation.
*   **Space Optimization:** Use **Floyd’s Cycle-Finding Algorithm** (Tortoise and Hare) to detect the cycle with $O(1)$ auxiliary space instead of a hash set.

**4. Key Algorithmic Pattern**
*   **Cycle Detection** (using a Hash Set).
