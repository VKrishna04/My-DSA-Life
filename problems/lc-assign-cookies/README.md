# Assign Cookies

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-assign-cookies` |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Solved | 2026-04-07 |
| Runtime | 23 ms (beats 58%) |
| Memory | 22.2 MB (beats 9%) |

## Problem Statement

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

**Example 1:**

**Input:** g = [1,2,3], s = [1,1]
**Output:** 1
**Explanation:** You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

**Example 2:**

**Input:** g = [1,2], s = [1,2,3]
**Output:** 2
**Explanation:** You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

 

**Constraints:**

	- `1 <= g.length <= 3 * 104`

	- `0 <= s.length <= 3 * 104`

	- `1 <= g[i], s[j] <= 231 - 1`

 

**Note:** This question is the same as  2410: Maximum Matching of Players With Trainers.

## Solutions

```Python3
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l = 0
        r = 0
        g.sort()
        s.sort()

        while l < len(s) and r < len(g):
            if g[r] <= s[l]:
                r += 1
            l += 1
        
        return r
```

## AI Review

### Analysis

**1. Complexity**
*   **Time Complexity:** $O(N \log N + M \log M)$, where $N$ is the number of children and $M$ is the number of cookies. Sorting both arrays dominates the $O(N + M)$ two-pointer traversal.
*   **Space Complexity:** $O(N + M)$ in Python, as `list.sort()` (Timsort) requires auxiliary space proportional to the input size.

**2. Correctness**
The solution is **correct**. It optimally pairs the smallest available cookie that meets the minimum greed factor of the current child.
*   **Edge Cases:** If `s` is empty, it returns `0`. If all cookies are smaller than the smallest greed factor, it returns `0`. Both are handled correctly by the `while` loop condition.

**3. Concrete Optimization**
Use a `for` loop for the cookies to remove manual index management for `l`, making the code more "Pythonic" and slightly cleaner:
```python
for cookie in s:
    if r < len(g) and cookie >= g[r]:
        r += 1
```
Additionally, you could add an early exit if `r == len(g)` (all children satisfied).

**4. Key Algorithmic Pattern**
**Greedy Strategy** combined with **Two Pointers**. Sorting allows the greedy choice of using the smallest possible cookie to satisfy the least greedy child.
