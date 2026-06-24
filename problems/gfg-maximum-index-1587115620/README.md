# Maximum Index

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-maximum-index-1587115620` |
| Topics | Arrays, Data Structures, two-pointer-algorithm |
| Solved | 2026-06-24 |

## Problem Statement

Given an array **arr[]** of positive integers, return the maximum difference between two indices **j** and **i **(i.e., **j - i**)** **such that **arr[i] &le; arr[j] **and **i ****&le;** **j**.

**Examples:**

**Input: **arr[] = [1, 10]
**Output: **1**
Explanation: **arr[0] &le; arr[1] so (j-i) is 1-0 = 1.

**Input: **arr[] = [5, 4, 3]
**Output: **0**
Explanation:** There is no pair that satisfies the given condition.
**Input: **arr[] = [34, 8, 10, 3, 2, 80, 30, 33, 1]
**Output: **6**
Explanation: **In the given array arr[1] < arr[7] satisfying the required condition(arr[i] &le; arr[j]) thus giving the maximum difference of j - i which is 6(7-1).

**Constraints:**
1 &le; arr.size &le; 105
0 &le; arr[i] &le; 109
