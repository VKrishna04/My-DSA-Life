# Number Of Coins

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-number-of-coins1824` |
| Topics | Dynamic Programming, Algorithms |
| Solved | 2026-06-24 |

## Problem Statement

You are given an array **coins[]**, where each element represents a coin of a **different** denomination, and a target value **sum**. You have an **unlimited** supply of each coin type. Your task is to determine the **minimum** number of coins needed to obtain the target **sum**. If it is **not** possible to form the sum using the given coins, return **-1**.

**Examples:**

**Input:** coins[] = [25, 10, 5], sum = 30
**Output:** 2
**Explanation:** Minimum 2 coins needed, 25 and 5  
**Input:** coins[] = [9, 6, 5, 1], sum = 19
**Output: **3
**Explanation:** 19 = 9 + 9 + 1
**Input:** coins[] = [5, 1], sum = 0
**Output: **0
**Explanation:** For 0 sum, we do not need a coin
**Input:** coins[] = [4, 6, 2], sum = 5
**Output: **-1
**Explanation:** Not possible to make the given sum.
**Constraints:**
1 &le; sum * coins.size() &le; 106
0 &le; sum &le; 104
1 &le; coins[i] &le; 104
1 &le; coins.size() &le; 103
