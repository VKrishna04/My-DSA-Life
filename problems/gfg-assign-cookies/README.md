# Assign Cookies

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-assign-cookies` |
| Topics | Arrays, Sorting, Data Structures, Algorithms |
| Solved | 2026-06-24 |

## Problem Statement

You are given an array **greed[]**, where **greed[i]** represents the minimum size of cookie required to satisfy the i-th child, and an array **cookie[]**,** **where **cookie[j] **represents the size of the j-th cookie. Each child can receive at most one cookie. A child i will be satisfied if they receive a cookie j such that **cookie[j] >= greed[i]**. Your task is to determine the **maximum** number of children that can be satisfied.

**Examples:**

**Input : **greed[] = [1, 10, 3], cookie = [1, 2, 3]
**Output: **2
**Explanation: **We can only assign cookie to the first and third child.
**Input : **greed[] = [10, 100], cookie = [1, 2]
**Output: **0
**Explanation: **We can not assign cookies to any child.
**Constraints:**
1 &le; greed.size() &le;  105
1 &le; cookie.size() &le;  105
1 &le; greed[i] , cookie[i] &le; 109
