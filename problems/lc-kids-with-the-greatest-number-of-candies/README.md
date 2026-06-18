# Kids With the Greatest Number of Candies

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-kids-with-the-greatest-number-of-candies` |
| Topics | Array |
| Solved | 2026-06-18 |
| Runtime | 0 ms (beats 100%) |
| Memory | 19.3 MB (beats 22.357200000000013%) |

## Problem Statement

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `ith` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return _a boolean array _`result`_ of length _`n`_, where _`result[i]`_ is _`true`_ if, after giving the _`ith`_ kid all the _`extraCandies`_, they will have the **greatest** number of candies among all the kids__, or _`false`_ otherwise_.

Note that **multiple** kids can have the **greatest** number of candies.

 

**Example 1:**

**Input:** candies = [2,3,5,1,3], extraCandies = 3
**Output:** [true,true,true,false,true] 
**Explanation:** If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

**Example 2:**

**Input:** candies = [4,2,1,1,2], extraCandies = 1
**Output:** [true,false,false,false,false] 
**Explanation:** There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

**Example 3:**

**Input:** candies = [12,1,12], extraCandies = 10
**Output:** [true,false,true]

 

**Constraints:**

	- `n == candies.length`

	- `2 <= n <= 100`

	- `1 <= candies[i] <= 100`

	- `1 <= extraCandies <= 50`

## Solutions

```Python3
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        results = [ (i+extraCandies) >= max_candies for i in candies ]
        return results
```

## AI Review

Here's a review of your solution:

1.  **Time Complexity:** O(N), where N is the number of kids. It takes one pass to find `max_candies` and another pass (via list comprehension) to generate the `results` list.
    **Space Complexity:** O(N) to store the `results` boolean list.

2.  **Correctness:** The solution is **correct**. It accurately implements the problem logic: first finding the greatest number of candies, then iterating to check if each kid *could* reach that maximum. Edge cases like a single kid, all kids having equal candies, or `extraCandies = 0` are handled correctly. LeetCode constraints typically guarantee non-empty input, preventing `max()` errors.

3.  **Optimisation:** No significant algorithmic optimization is applicable. The current solution is already optimal, requiring O(N) time (to find the max and generate N results) and O(N) space (to store N boolean results).

4.  **Key Algorithmic Pattern:** This solution primarily uses a **Max/Min finding** pattern (to determine the target value) followed by a **Map/Transform** operation (to apply a condition to each element and create a new list).
