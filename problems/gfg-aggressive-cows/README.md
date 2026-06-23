# Aggressive Cows

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-aggressive-cows` |
| Topics | Binary Search, Algorithms |
| Solved | 2026-06-24 |

## Problem Statement

You are given an array with unique elements of **stalls[]**,** **which denote the positions of **stalls**. You are also given an integer **k** which denotes the number of aggressive cows. The task is to assign **stalls **to **k** cows such that the **minimum distance** between any two of them is the **maximum** possible.

**Examples:**

**Input: **stalls[] = [1, 2, 4, 8, 9], k = 3
**Output: **3
**Explanation: **The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows in this case is 3, which is the largest among all possible ways.

**Input: **stalls[] = [10, 1, 2, 7, 5], k = 3
**Output: **4
**Explanation: **The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows in this case is 4, which is the largest among all possible ways.
**Input: **stalls[] = [2, 12, 11, 3, 26, 7], k = 5
**Output: **1
**Explanation: **There are 6 stalls and only 5 cows, we try to place the cows such that the minimum distance between any two cows is as large as possible.
The minimum distance between cows in this case is 1, which is the largest among all possible ways.
**Constraints:**
2 &le; stalls.size() &le; 106
0 &le; stalls[i] &le; 108
2 &le; k &le; stalls.size()

## Solutions

```Python3
class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)
        
        # Helper function to check if we can place k cows with 'dist' distance
        def canPlace(dist):
            count = 1  # Place the first cow in the first stall
            last_pos = stalls[0]
            
            for i in range(1, n):
                if stalls[i] - last_pos >= dist:
                    count += 1
                    last_pos = stalls[i]
                if count >= k:
                    return True
            return False

        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                ans = mid  # This distance is possible, try for a larger one
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
```

## AI Review

**1. Complexity**
*   **Time:** $O(N \log N + N \log D)$, where $N$ is the number of stalls and $D$ is the distance range (`stalls[-1] - stalls[0]`). Sorting takes $O(N \log N)$ and the binary search performs $\log D$ checks of $O(N)$ each.
*   **Space:** $O(1)$ (or $O(N)$ if considering the space used by Python's Timsort).

**2. Correctness**
The solution is correct. It uses a greedy approach to verify distance feasibility and binary search to find the maximum possible minimum distance. It handles the basic constraints well.

**3. Optimization**
*   **Refine Search Space:** Instead of `low = 1`, initialize `low` to `min(stalls[i+1] - stalls[i] for i in range(n-1))`. This provides a tighter lower bound for the binary search.
*   **Early Exit:** In `canPlace`, if the remaining stalls are fewer than the remaining cows needed, you can return `False` immediately.

**4. Key Algorithmic Pattern**
**Binary Search on Answer:** This pattern is used when the search space is monotonic (if a distance $d$ is possible, any distance $< d$ is also possible) and you need to find an optimal boundary value.
