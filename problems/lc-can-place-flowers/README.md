# Can Place Flowers

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-can-place-flowers` |
| Topics | Array, Greedy |
| Solved | 2026-06-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.7 MB (beats 10.427999999999994%) |

## Problem Statement

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` _if_ `n` _new flowers can be planted in the_ `flowerbed` _without violating the no-adjacent-flowers rule and_ `false` _otherwise_.

 

**Example 1:**

**Input:** flowerbed = [1,0,0,0,1], n = 1
**Output:** true
**Example 2:**

**Input:** flowerbed = [1,0,0,0,1], n = 2
**Output:** false

 

**Constraints:**

	- `1 <= flowerbed.length <= 2 * 104`

	- `flowerbed[i]` is `0` or `1`.

	- There are no two adjacent flowers in `flowerbed`.

	- `0 <= n <= flowerbed.length`

## Solutions

```Python3
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        if flowerbed == [0] and n == 1:
            return True
        i = 0
        l = len(flowerbed)
        while i < l:
            if flowerbed[i] == 1:
                i += 2
            elif i == l - 1 or flowerbed[i+1] == 0:
                n -= 1
                if n == 0:
                    return True
                i += 2
            else:
                i += 3
        return n <= 0

```

## AI Review

Here's a review of your solution:

1.  **Time Complexity**: O(L), where L is the length of `flowerbed`. The loop iterates through the array, and `i` increments by at least 2 in each step.
    **Space Complexity**: O(1). Only a few constant-space variables are used.

2.  **Correctness**: Correct. The logic skillfully uses `i` increments (`i += 2`, `i += 3`) to implicitly handle the left-neighbor condition (`flowerbed[i-1] == 0`) when considering planting at `i`. If `flowerbed[i-1]` contained a flower, `i` would have already skipped past `i`. The initial check for `flowerbed == [0] and n == 1` is redundant as the main loop covers it, but it doesn't cause failure.

3.  **One concrete optimisation**: Remove the redundant check `if flowerbed == [0] and n == 1:`. The rest of the code already handles this case correctly.

4.  **Key algorithmic pattern used**: Greedy approach. The solution iterates through the flowerbed, making the locally optimal choice (planting a flower whenever possible) which leads to a globally optimal solution (maximizing placed flowers).
