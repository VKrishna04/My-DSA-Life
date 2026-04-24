# Furthest Point From Origin

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-furthest-point-from-origin` |
| Topics | String, Counting |
| Solved | 2026-04-24 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 18.12810000000001%) |

## Problem Statement

You are given a string `moves` of length `n` consisting only of characters `'L'`, `'R'`, and `'_'`. The string represents your movement on a number line starting from the origin `0`.

In the `ith` move, you can choose one of the following directions:

	- move to the left if `moves[i] = 'L'` or `moves[i] = '_'`

	- move to the right if `moves[i] = 'R'` or `moves[i] = '_'`

Return _the **distance from the origin** of the **furthest** point you can get to after _`n`_ moves_.

 

**Example 1:**

**Input:** moves = "L_RL__R"
**Output:** 3
**Explanation:** The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".

**Example 2:**

**Input:** moves = "_R__LL_"
**Output:** 5
**Explanation:** The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".

**Example 3:**

**Input:** moves = "_______"
**Output:** 7
**Explanation:** The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".

 

**Constraints:**

	- `1 <= moves.length == n <= 50`

	- `moves` consists only of characters `'L'`, `'R'` and `'_'`.

## Solutions

```Python3
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        points = 0
        left = 0
        right = 0
        dash = 0
        for move in moves:
            if move == 'L':
                left += 1
            if move == 'R':
                right += 1
            if move == '_':
                dash += 1
        return abs(right - left) + dash
```

## AI Review

### Analysis

1.  **Complexity**
    *   **Time Complexity:** $O(n)$, where $n$ is the length of the string. We iterate through the moves exactly once.
    *   **Space Complexity:** $O(1)$, as we only store four integer counters regardless of input size.

2.  **Correctness**
    *   The logic is **correct**. To maximize distance, all underscores (`_`) must be treated as the direction that already has the higher frequency (or either, if equal). The formula `abs(right - left) + dash` perfectly captures this logic. It handles edge cases like empty strings or strings containing only `_` correctly.

3.  **Concrete Optimization**
    *   Use Python's built-in `count()` method. While still $O(n)$, it is more idiomatic and often faster due to C-level implementation:
        ```python
        return abs(moves.count('L') - moves.count('R')) + moves.count('_')
        ```
    *   Alternatively, using `if-elif-else` instead of three separate `if` statements avoids unnecessary comparisons after a match is found.

4.  **Key Algorithmic Pattern**
    *   **Greedy Strategy:** At every underscore, we make the optimal choice to move further away from the origin by aligning all flexible moves with the dominant direction.
