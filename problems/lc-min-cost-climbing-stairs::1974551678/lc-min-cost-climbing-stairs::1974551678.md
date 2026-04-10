# Min Cost Climbing Stairs

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-min-cost-climbing-stairs::1974551678` |
| Topics | Array, Dynamic Programming |
| Solved | 2026-04-10 |
| Runtime | 1 ms (beats 73%) |
| Memory | 19.2 MB (beats 80%) |

## Problem Statement

You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return _the minimum cost to reach the top of the floor_.

 

**Example 1:**

**Input:** cost = [10,15,20]
**Output:** 15
**Explanation:** You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

**Example 2:**

**Input:** cost = [1,100,1,1,1,100,1,1,100,1]
**Output:** 6
**Explanation:** You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

 

**Constraints:**

	- `2 <= cost.length <= 1000`

	- `0 <= cost[i] <= 999`

## Solutions

```Python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = 0
        curr = 0
        for i in range(2, len(cost) + 1):
            prev , curr = curr, min(prev + cost[i-2], curr + cost[i-1])
        return curr
```
