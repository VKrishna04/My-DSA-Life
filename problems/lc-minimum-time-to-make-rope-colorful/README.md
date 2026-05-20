# Minimum Time to Make Rope Colorful

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-minimum-time-to-make-rope-colorful` |
| Topics | Array, String, Dynamic Programming, Greedy |
| Solved | 2026-04-11 |
| Runtime | 95 ms (beats 38%) |
| Memory | 27.6 MB (beats 100%) |

## Problem Statement

Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string `colors` where `colors[i]` is the color of the `ith` balloon.

Alice wants the rope to be **colorful**. She does not want **two consecutive balloons** to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it **colorful**. You are given a **0-indexed** integer array `neededTime` where `neededTime[i]` is the time (in seconds) that Bob needs to remove the `ith` balloon from the rope.

Return _the **minimum time** Bob needs to make the rope **colorful**_.

 

**Example 1:**

**Input:** colors = "abaac", neededTime = [1,2,3,4,5]
**Output:** 3
**Explanation:** In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

**Example 2:**

**Input:** colors = "abc", neededTime = [1,2,3]
**Output:** 0
**Explanation:** The rope is already colorful. Bob does not need to remove any balloons from the rope.

**Example 3:**

**Input:** colors = "aabaa", neededTime = [1,2,3,4,1]
**Output:** 2
**Explanation:** Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

 

**Constraints:**

	- `n == colors.length == neededTime.length`

	- `1 <= n <= 105`

	- `1 <= neededTime[i] <= 104`

	- `colors` contains only lowercase English letters.

## Hints

<details>
<summary>Hint 1</summary>

Maintain the running sum and max value for repeated letters.

</details>

## Solutions

```Python3
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n, s = len(colors), 0
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                s += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
        return s 
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the length of the string. The algorithm performs a single pass.
*   **Space Complexity:** $O(1)$, as it uses a constant amount of extra space (modifying the input array in-place).

### 2. Correctness
The logic is **correct**. By updating `neededTime[i]` to the maximum of the duplicate pair, the code ensures that for any contiguous block of the same color, only the single largest `neededTime` is preserved, while all others are added to the sum `s`. It handles edge cases like single-balloon ropes or ropes with no repeating colors correctly.

### 3. Concrete Optimization
**Avoid Input Mutation:** Modifying the input `neededTime` is generally discouraged. You can optimize by tracking the `max_cost` of the current color group in a separate variable.

```python3
# Optimized loop logic
max_cost = neededTime[0]
for i in range(1, n):
    if colors[i] == colors[i-1]:
        s += min(max_cost, neededTime[i])
        max_cost = max(max_cost, neededTime[i])
    else:
        max_cost = neededTime[i]
```

### 4. Key Algorithmic Pattern
**Greedy:** For every group of identical adjacent balloons, we greedily keep the one that costs the most to remove and sum the costs of the others.

## Notes

[ Time taken: 13m 26s ]
