# First Day Where You Have Been in All the Rooms

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-first-day-where-you-have-been-in-all-the-rooms` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-09-17 |
| Runtime | 3516 ms (beats 5.6600000000000605%) |
| Memory | 687.7 MB (beats 5.660100000000032%) |

## Problem Statement

There are `n` rooms you need to visit, labeled from `0` to `n - 1`. Each day is labeled, starting from `0`. You will go in and visit one room a day.

Initially on day `0`, you visit room `0`. The **order** you visit the rooms for the coming days is determined by the following **rules** and a given **0-indexed** array `nextVisit` of length `n`:

	- Assuming that on a day, you visit room `i`,

	- if you have been in room `i` an **odd** number of times (**including** the current visit), on the **next** day you will visit a room with a **lower or equal room number** specified by `nextVisit[i]` where `0 <= nextVisit[i] <= i`;

	- if you have been in room `i` an **even** number of times (**including** the current visit), on the **next** day you will visit room `(i + 1) mod n`.

Return _the label of the **first** day where you have been in **all** the rooms_. It can be shown that such a day exists. Since the answer may be very large, return it **modulo** `109 + 7`.

 

**Example 1:**

**Input:** nextVisit = [0,0]
**Output:** 2
**Explanation:**
- On day 0, you visit room 0. The total times you have been in room 0 is 1, which is odd.
  On the next day you will visit room nextVisit[0] = 0
- On day 1, you visit room 0, The total times you have been in room 0 is 2, which is even.
  On the next day you will visit room (0 + 1) mod 2 = 1
- On day 2, you visit room 1. This is the first day where you have been in all the rooms.

**Example 2:**

**Input:** nextVisit = [0,0,2]
**Output:** 6
**Explanation:**
Your room visiting order for each day is: [0,0,1,0,0,1,2,...].
Day 6 is the first day where you have been in all the rooms.

**Example 3:**

**Input:** nextVisit = [0,1,2,0]
**Output:** 6
**Explanation:**
Your room visiting order for each day is: [0,0,1,1,2,2,3,...].
Day 6 is the first day where you have been in all the rooms.

 

**Constraints:**

	- `n == nextVisit.length`

	- `2 <= n <= 105`

	- `0 <= nextVisit[i] <= i`

## Solutions

```Python3
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0]*n
        for i in range(1, n):
            dp[i] = 2*dp[i-1] - dp[nextVisit[i-1]] + 2
        return dp[-1] % (10 ** 9 + 7)
```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(n)$ — The solution iterates through the rooms once. (Note: Without modular arithmetic inside the loop, Python handles growing integers, but arithmetic becomes $O(n)$ per operation, potentially making it $O(n^2)$).
*   **Space Complexity:** $O(n)$ — Uses a DP array of size $n$.

**2. Correctness**
The mathematical logic is correct. However, applying the modulo only at the end is dangerous. In Python, integers have arbitrary precision, but as `dp[i]` grows exponentially ($2^n$), the memory and time required for arithmetic will spike. Always apply modulo **inside** the loop to maintain $O(1)$ arithmetic and prevent TLE.

**3. Optimization**
Apply the modulo within the loop:
```python
dp[i] = (2 * dp[i-1] - dp[nextVisit[i-1]] + 2) % 1_000_000_007
```
Given your history with **Array** resubmits, remember that modular arithmetic in transitions prevents "hidden" complexity issues and potential logic errors with negative results in other languages.

**4. Key Algorithmic Pattern**
**Dynamic Programming**: The state `dp[i]` represents the first day you arrive at room `i`. Each transition calculates the "round trip" time from `i-1` back to `nextVisit[i-1]` and back to `i-1` again.
