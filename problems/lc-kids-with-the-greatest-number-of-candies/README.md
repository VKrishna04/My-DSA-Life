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

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the number of kids. We traverse the list once to find the maximum and once more to build the result.
*   **Space Complexity:** $O(n)$ for the output list. If excluding the output, it is $O(1)$ auxiliary space.

### 2. Correctness
The logic is **correct**. It accurately identifies if a kid can reach or exceed the current maximum.
*   **Edge Cases:** The code handles cases where all kids have the same amount or `extraCandies` is 0. 
*   **Empty Input:** If `candies` were empty, `max()` would raise a `ValueError`. However, LeetCode constraints guarantee $n \ge 2$.

### 3. Optimization
While $O(n)$ is optimal, you can slightly improve performance by calculating a **threshold** once:
```python
threshold = max_candies - extraCandies
results = [i >= threshold for i in candies]
```
This replaces $n$ additions with $n$ comparisons, which is marginally faster in some environments.

### 4. Key Algorithmic Pattern
**Greedy / Linear Scan:** You find a global property (the maximum) in one pass and then use it to make local decisions for each element in a second pass.
