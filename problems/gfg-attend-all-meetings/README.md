# Attend All Meetings

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-attend-all-meetings` |
| Topics | Sorting, Greedy, Array |
| Solved | 2026-06-24 |

## Problem Statement

Given a 2D array **arr[][],** where **arr[i][0] **is the **starting time **of ith meeting and **arr[i][1] **is the **ending time **of ith meeting, the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a particular time.

**Note:** A person can attend a meeting if its starting time is greater than or equal to the previous meeting's ending time.

**Examples:**

**Input: **arr[][] = [[1, 4], [10, 15], [7, 10]]
**Output:** true
**Explanation: **Since all the meetings are held at different times, it is possible to attend all the meetings.
**Input: **arr[][] = [[2, 4], [9, 12], [6, 10]]
**Output:** false
**Explanation:** Since the second and third meeting overlap, a person cannot attend all the meetings.

**Constraints:**
1 &le; arr.size() &le; 105
0 &le; arr[i] &le; 2*106

## Solutions

```python3
class Solution:
    def canAttend(self, arr):
        sor_i = sorted(range(len(arr)), key= lambda i: arr[i][1])
        
        arr[:] = [arr[i] for i in sor_i]
        
        free = 0
        
        for time in arr:
            if time[0] < free:
                return False
            free = time[1]
        return True
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N \log N)$ due to the `sorted()` function. The list comprehension and the loop are both $O(N)$.
*   **Space:** $O(N)$. The code creates an auxiliary index list `sor_i` and a temporary list during the `arr[:]` slice assignment.

**2. Correctness**
The logic is sound for detecting overlaps. It correctly handles back-to-back meetings (e.g., `[5, 10]` and `[10, 15]`) as non-overlapping. One minor edge case: if meetings occur at negative timestamps, `free = 0` might return `False` incorrectly for a valid meeting like `[-5, -2]`.

**3. Optimisation**
Sort by **start time** in-place to achieve $O(1)$ auxiliary space and cleaner logic. This avoids creating extra lists and the "free" variable initialization risk:
```python3
arr.sort() # Sorts by start time by default
for i in range(len(arr) - 1):
    if arr[i][1] > arr[i+1][0]:
        return False
return True
```

**4. Key Algorithmic Pattern**
**Sorting:** The core of interval problems is ordering the data (usually by start or end time) to reduce the problem to a single-pass linear comparison.
