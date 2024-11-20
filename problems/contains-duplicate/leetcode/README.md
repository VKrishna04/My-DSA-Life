# Contains Duplicate

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-contains-duplicate` |
| Topics | Array, Hash Table, Sorting |
| Solved | 2025-06-02 |
| Runtime | 9 ms (beats 73.13409999999999%) |
| Memory | 31.5 MB (beats 53.13849999999995%) |

## Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

 

**Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** true

**Explanation:**

The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]

**Output:** false

**Explanation:**

All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]

**Output:** true

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `-109 <= nums[i] <= 109`

## Solutions

```Python3
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

## AI Review

### Review of "Contains Duplicate" Solution

1.  **Complexity**
    *   **Time:** $O(n)$ on average. Converting the list to a set requires one pass through the array, with $O(1)$ average-case insertions.
    *   **Space:** $O(n)$. In the worst case (all elements unique), the set stores $n$ elements.

2.  **Correctness**
    *   The solution is **correct** and handles all edge cases, including empty lists (returns `False`), single-element lists (returns `False`), and lists where all elements are identical (returns `True`).

3.  **Optimization**
    *   **Early Exit:** The current code always processes the entire list. For very large arrays where a duplicate might appear at the beginning, you can optimize by iterating manually:
        ```python
        seen = set()
        for n in nums:
            if n in seen: return True
            seen.add(n)
        return False
        ```
        This maintains $O(n)$ worst-case but achieves $O(1)$ best-case time complexity.

4.  **Key Algorithmic Pattern**
    *   **Hash Set / Hashing:** Utilizing the unique property and constant-time lookup of a hash-based data structure to detect collisions.
