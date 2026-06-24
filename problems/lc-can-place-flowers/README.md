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

### 1. Complexity
*   **Time Complexity**: $O(N)$, where $N$ is the length of the flowerbed. The algorithm traverses the list at most once.
*   **Space Complexity**: $O(1)$. No additional data structures are used; the input is processed in place.

### 2. Correctness
The logic is correct. The "jump" strategy (`i += 2` or `i += 3`) correctly maintains the non-adjacency rule by skipping indices that are guaranteed to be invalid for planting. 
*   **Edge Cases**: The code handles single-element lists, boundary conditions (start/end of list), and `n=0` correctly. The `if flowerbed == [0]` check is actually redundant as the `while` loop handles it naturally, but it doesn't break correctness.

### 3. Optimization
**Simplify the logic**: You can remove the special `if` for `[0]` and unify the boundary checks. Use a "virtual" zero at the boundaries to handle `i-1` and `i+1` without special `if` branches:
```python
# Check: (i==0 or f[i-1]==0) and (f[i]==0) and (i==l-1 or f[i+1]==0)
```
This reduces the number of conditional branches inside the loop.

### 4. Key Algorithmic Pattern
**Greedy Algorithm**: The solution makes the locally optimal choice of planting a flower at the first available valid spot, which leads to the global maximum number of flowers.
