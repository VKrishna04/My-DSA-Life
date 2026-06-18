# Can Place Flowers

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-can-place-flowers` |
| Topics | Array, Greedy |
| Solved | 2026-06-18 |
| Runtime | N/A |
| Memory | N/A |

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
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            elif flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                if n == 0:
                    return True
                i += 2
            elif flowerbed[i] == 0 and flowerbed[i+1] == 1:
                i += 3
        return n <= 0

```

## AI Review

Here's a review of your solution:

1.  **Time Complexity:** O(N), where N is the length of `flowerbed`, as it involves a single pass through the array.
    **Space Complexity:** O(1), as only a few constant extra variables are used.

2.  **Correctness:**
    *   **Edge Case Failure (IndexError):** The primary flaw is accessing `flowerbed[i+1]` without checking if `i+1` is within bounds. This will cause an `IndexError` when `i` is `len(flowerbed) - 1`. For example, `flowerbed = [0]`, `n = 0` (after `if n == 0` check, the special case fails too), or `flowerbed = [1]`, `n = 0`.
    *   **Logic Flaw:** `elif flowerbed[i] == 0 and flowerbed[i+1] == 1: i += 3` is problematic. If `flowerbed = [0, 1, 0]` and `n = 1`, it will skip the last `0` (where a flower *could* be placed) and return `False` instead of `True`. The logic for advancing `i` needs to be more precise based on local conditions.
    *   The special case `if flowerbed == [0] and n == 1:` is technically correct for that specific input but is an ad-hoc fix.

3.  **One Concrete Optimization:**
    Pad the `flowerbed` array with zeros at both ends (e.g., `flowerbed = [0] + flowerbed + [0]`). This simplifies boundary checks significantly, allowing uniform `flowerbed[i-1]`, `flowerbed[i]`, `flowerbed[i+1]` access within the main loop without `IndexError` concerns.

4.  **Key Algorithmic Pattern:**
    Greedy Approach combined with a One-Pass Iteration.
