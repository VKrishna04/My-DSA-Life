# Count Number of Pairs With Absolute Difference K

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-count-number-of-pairs-with-absolute-difference-k` |
| Topics | Array, Hash Table, Counting |
| Solved | 2025-09-09 |
| Runtime | 115 ms (beats 5.330000000000007%) |
| Memory | 17.7 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` and an integer `k`, return _the number of pairs_ `(i, j)` _where_ `i < j` _such that_ `|nums[i] - nums[j]| == k`.

The value of `|x|` is defined as:

	- `x` if `x >= 0`.

	- `-x` if `x < 0`.

 

**Example 1:**

**Input:** nums = [1,2,2,1], k = 1
**Output:** 4
**Explanation:** The pairs with an absolute difference of 1 are:
- [**1**,**2**,2,1]
- [**1**,2,**2**,1]
- [1,**2**,2,**1**]
- [1,2,**2**,**1**]

**Example 2:**

**Input:** nums = [1,3], k = 3
**Output:** 0
**Explanation:** There are no pairs with an absolute difference of 3.

**Example 3:**

**Input:** nums = [3,2,1,5,4], k = 2
**Output:** 3
**Explanation:** The pairs with an absolute difference of 2 are:
- [**3**,2,**1**,5,4]
- [**3**,2,1,**5**,4]
- [3,**2**,1,5,**4**]

 

**Constraints:**

	- `1 <= nums.length <= 200`

	- `1 <= nums[i] <= 100`

	- `1 <= k <= 99`

## Hints

<details>
<summary>Hint 1</summary>

Can we check every possible pair?

</details>

<details>
<summary>Hint 2</summary>

Can we use a nested for loop to solve this problem?

</details>

## Solutions

```Python3
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        sorted(nums)
        for i in range(len(nums)):
            count += len([j for j in range(len(nums)) if (nums[i]-k)==nums[j]])
        return count
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n^2)$. The code uses a nested structure: an outer loop ($n$ iterations) and a list comprehension that scans the entire list again ($n$ iterations).
*   **Space Complexity:** $O(n)$ due to the creation of temporary lists within the list comprehension.

### 2. Correctness
*   **Logical Flaw:** `sorted(nums)` returns a new list and does not sort in place; since the result isn't assigned, this line does nothing.
*   **Pair Counting:** The logic `nums[i] - k == nums[j]` correctly identifies pairs where the difference is $k$. Since $k \ge 1$ (per LeetCode constraints), this effectively counts each unique pair $\{i, j\}$ exactly once (specifically when the larger element is at index $i$).
*   **Edge Case:** If $k=0$, it would count $i=j$ as a pair, but the problem constraints usually specify $k \ge 1$ and $i < j$.

### 3. Optimization
Use a **Hash Map (Frequency Counter)** to achieve **$O(n)$ time** and **$O(1)$ auxiliary space** (since the range of numbers is limited to 1–100):
```python
counts = {}
ans = 0
for x in nums:
    ans += counts.get(x - k, 0) + counts.get(x + k, 0)
    counts[x] = counts.get(x, 0) + 1
```

### 4. Key Algorithmic Pattern
**Frequency Counting (Hash Map)**. This transforms a search problem into a constant-time lookup.
