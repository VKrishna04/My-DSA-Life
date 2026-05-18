# Target Sum

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-target-sum` |
| Topics | Array, Dynamic Programming, Backtracking |
| Solved | 2026-04-29 |
| Runtime | 15 ms (beats 97.8274%) |
| Memory | 19.3 MB (beats 74.35379999999999%) |

## Problem Statement

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

	- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

 

**Example 1:**

**Input:** nums = [1,1,1,1,1], target = 3
**Output:** 5
**Explanation:** There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

**Example 2:**

**Input:** nums = [1], target = 1
**Output:** 1

 

**Constraints:**

	- `1 <= nums.length <= 20`

	- `0 <= nums[i] <= 1000`

	- `0 <= sum(nums[i]) <= 1000`

	- `-1000 <= target <= 1000`

## Solutions

```Python3
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totsum = sum(nums)
        if abs(target) > totsum:
            return 0
        if (totsum + target) %2 != 0:
            return 0
        
        P = (totsum + target) // 2
        dp = [0]*(P+1)
        dp[0]=1
        
        for num in nums:
            for w in range(P, num-1, -1):
                dp[w] = dp[w] + dp[w-num]
        return dp[-1]
```

## AI Review

**1. Complexity**
*   **Time:** $O(N \cdot S)$, where $N$ is the number of elements and $S$ is the calculated subset sum $P$. Since $P \approx \frac{\text{total\_sum} + \text{target}}{2}$, this is effectively $O(N \cdot \text{sum(nums)})$.
*   **Space:** $O(S)$ to store the DP array.

**2. Correctness**
The solution is **correct**. It successfully transforms the "Target Sum" problem into the "Subset Sum" problem using the derivation: $P - (Sum - P) = Target \implies 2P = Sum + Target$.
*   **Edge Cases:** It correctly handles cases where `target` is unreachable (`abs(target) > totsum`) or where no integer partition exists (`(totsum + target) % 2 != 0`).
*   **Zeros:** By iterating the inner loop backwards (`range(P, num-1, -1)`), it correctly handles zeros in `nums` by doubling the ways for each zero encountered.

**3. Optimization**
While the 1D DP is already space-efficient, you can skip `0` values during the DP loop and multiply the final result by $2^z$ (where $z$ is the count of zeros). This reduces the number of inner-loop iterations.

**4. Key Algorithmic Pattern**
**Dynamic Programming** (specifically the **0/1 Knapsack / Subset Sum** variation with space optimization).
