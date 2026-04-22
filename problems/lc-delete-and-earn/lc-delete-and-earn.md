# Delete and Earn

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-delete-and-earn` |
| Topics | Array, Hash Table, Dynamic Programming |
| Solved | 2026-04-22 |
| Runtime | 0 ms (beats 100%) |
| Memory | 20.4 MB (beats 92.89920000000001%) |

## Problem Statement

You are given an integer array `nums`. You want to maximize the number of points you get by performing the following operation any number of times:

	- Pick any `nums[i]` and delete it to earn `nums[i]` points. Afterwards, you must delete **every** element equal to `nums[i] - 1` and **every** element equal to `nums[i] + 1`.

Return _the **maximum number of points** you can earn by applying the above operation some number of times_.

 

**Example 1:**

**Input:** nums = [3,4,2]
**Output:** 6
**Explanation:** You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

**Example 2:**

**Input:** nums = [2,2,3,3,3,4]
**Output:** 9
**Explanation:** You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

 

**Constraints:**

	- `1 <= nums.length <= 2 * 104`

	- `1 <= nums[i] <= 104`

## Solutions

```Python3
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        dp = [0]*(m+1)

        for num in nums:
            dp[num] += num

        prev, curr = 0, 0

        for p in dp:
            prev, curr = curr, max(curr, prev + p)

        return curr
```

## AI Review

### Review
**1. Complexity**
*   **Time:** $O(N + M)$, where $N$ is the number of elements in `nums` and $M$ is the maximum value in `nums`. We iterate through `nums` once and then through the `dp` array of size $M$.
*   **Space:** $O(M)$ to store the frequency/sum array.

**2. Correctness**
The logic is **correct**. It successfully transforms the problem into the "House Robber" variant: you cannot take adjacent values ($i$ and $i+1$).
*   **Edge Cases:** Handles single elements, duplicate elements, and gaps between numbers (e.g., `[1, 10]`) correctly by initializing `dp` with zeros.
*   **Potential Fail:** If $M$ (max value) is extremely large (e.g., $10^9$) while $N$ is small, the $O(M)$ space will cause a `MemoryError`.

**3. Optimization**
**Use a Hash Map with Sorting:** Instead of a fixed-size array, use a dictionary to store `num: total_points`. Sort the unique keys and iterate through them. If the current key is not consecutive to the previous one, you can take its full value regardless of the previous choice. This reduces space to $O(N)$.

**4. Key Algorithmic Pattern**
**Dynamic Programming** (specifically the **House Robber** pattern). It reduces a selection problem with adjacency constraints into a linear state transition: `dp[i] = max(dp[i-1], dp[i-2] + current_val)`.
