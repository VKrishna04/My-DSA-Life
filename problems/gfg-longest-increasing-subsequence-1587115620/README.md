# Longest Increasing Subsequence

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-longest-increasing-subsequence-1587115620` |
| Topics | Dynamic Programming, Binary Search, Algorithms |
| Solved | 2026-06-24 |

## Problem Statement

Given an array **`arr[]`** of non-negative integers, the task is to find the **length** of the **Longest Strictly Increasing Subsequence (LIS)**.
A subsequence is **strictly increasing** if each element in the subsequence is strictly less than the next element.

**Examples:**

**Input: **arr[] = [5, 8, 3, 7, 9, 1]
**Output: **3**
Explanation: **The longest strictly increasing subsequence could be `[5, 7, 9]`, which has a length of 3.
**Input: **arr[] = [10, 6, 3, 11, 7, 15]
**Output: **3**
Explanation: **One of the possible longest strictly increasing subsequences is `[10, 11, 15]`, which has a length of 3.
**Input: **arr[] = [3, 10, 2, 1, 20]
**Output: **3**
Explanation: **The longest strictly increasing subsequence could be `[3, 10, 20]`, which has a length of 3.
**Constraints:**
1 &le; arr.size() &le; 103
0 &le; arr[i] &le; 106
