# Minimum Platforms

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-minimum-platforms-1587115620` |
| Topics | Array, Greedy, Sorting, Binary Search |
| Solved | 2026-06-24 |

## Problem Statement

Given arrival **arr[] **and departure **dep[] **times of trains on the same day, find the minimum number of platforms needed so that no train waits. A platform cannot serve two trains at the same time; if a train arrives before another departs, an extra platform is needed.

**Note:** Time intervals are in the 24-hour format **(****HHMM)** , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

**Examples:**

**Input**: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
**Output**: 3
**Explanation**: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.
**Input**: arr[] = [900, 1235, 1100], dep[] = [1000, 1240, 1200]
**Output**: 1
**Explanation**: All train times are mutually exclusive. So we need only one platform.

**Input**: arr[] = [1000, 935, 1100], dep[] = [1200, 1240, 1130]
**Output**: 3
**Explanation**: All 3 trains have to be there from 11:00 to 11:30
**Constraints:
**1 &le; number of trains &le; 105
0000 &le; arr[i] &le; dep[i] &le; 2359

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N \log N)$ due to sorting the indices and the heap operations (each of $N$ elements is pushed/popped in $O(\log N)$).
*   **Space Complexity:** $O(N)$. You are storing a sorted index array and a heap that can grow to size $N$ in the worst case (all overlapping intervals).

### 2. Correctness & Edge Cases
*   **Empty Input:** The code will raise an `IndexError` at `dep[0]` if `arr` or `dep` are empty. You should handle $N=0$ as a guard clause.
*   **Same Time Arrival/Departure:** The condition `arr[i] > platforms[0]` correctly handles the GeeksForGeeks requirement that if a train arrives at the same time another leaves, they cannot share a platform (it only pops if arrival is strictly later).

### 3. Optimization: Two-Pointer Approach
Instead of maintaining a heap and keeping departures tied to specific arrivals, **sort `arr` and `dep` independently**.
When you sort them separately, you simply track how many trains have arrived vs. how many have departed at any point in time. This removes the need for $O(N)$ auxiliary space for the heap and index mapping, allowing for an $O(1)$ extra space solution (excluding the space for sorting).

### 4. Key Algorithmic Pattern
**Greedy with a Min-Heap** (Processing intervals by start time and using a heap to track the earliest end time).
