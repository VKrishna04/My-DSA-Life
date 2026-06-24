# 2 Sum Find A Pair With Given Sum

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-2-sum-find-a-pair-with-given-sum` |
| Topics | Sorting, two-pointer-algorithm, Arrays, Hash |
| Solved | 2026-06-24 |

## Problem Statement

Given an array arr[] and an integer target, return the pair of elements whose sum equals target. An element cannot be used twice unless it appears multiple times in the array.

**Note:**  If no pair exist, return an empty array.

**Examples:**

**Input: **arr[] = [2, 9, 10, 4, 15], target = 12
**Output: **[2, 10]**
Explanation: **Pair with sum equal to 12 is (2, 10).
**Input: **arr[] = [3, 2, 4], target = 8
**Output: **[]**
Explanation: **No pair exists with sum equal to 8.
**Input: **arr[] = [1, 4, 5, 6, 1], target = 2
**Output: **[1, 1]**
Explanation: **Pair with sum equal to 2 is (1, 1).
**Constraints:
**1 &le; arr.size() &le; 105**
**0 &le; arr[i] &le; 104
1 &le; target &le; 104
