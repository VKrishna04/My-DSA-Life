# Make Array Zero by Subtracting Equal Amounts

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-make-array-zero-by-subtracting-equal-amounts` |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Simulation |
| Solved | 2025-06-02 |
| Runtime | 3 ms (beats 21.767000000000003%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

You are given a non-negative integer array `nums`. In one operation, you must:

	- Choose a positive integer `x` such that `x` is less than or equal to the **smallest non-zero** element in `nums`.

	- Subtract `x` from every **positive** element in `nums`.

Return _the **minimum** number of operations to make every element in _`nums`_ equal to _`0`.

 

**Example 1:**

**Input:** nums = [1,5,0,3,5]
**Output:** 3
**Explanation:**
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

**Example 2:**

**Input:** nums = [0]
**Output:** 0
**Explanation:** Each element in nums is already 0 so no operations are needed.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`

## Hints

<details>
<summary>Hint 1</summary>

It is always best to set x as the smallest non-zero element in nums.

</details>

<details>
<summary>Hint 2</summary>

Elements with the same value will always take the same number of operations to become 0. Contrarily, elements with different values will always take a different number of operations to become 0.

</details>

<details>
<summary>Hint 3</summary>

The answer is the number of unique non-zero numbers in nums.

</details>

## Solutions

```Python3
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        try:
            nums.remove(0)
        finally:
            return len(nums)

```

## AI Review

### Review of "Make Array Zero by Subtracting Equal Amounts" Solution

1. **Complexity**
   - **Time:** $O(n)$, where $n$ is the length of `nums`. Converting the list to a set takes linear time.
   - **Space:** $O(n)$ in the worst case to store unique elements in the set.

2. **Correctness**
   The logic is **correct**. The number of operations required equals the number of unique non-zero integers in the array. Each operation removes the current smallest non-zero value, effectively collapsing one "level" of unique values.
   - **Edge Case:** `nums = [0, 0, 0]` correctly returns `0`.
   - **Edge Case:** `nums = [1, 2, 3]` correctly returns `3`.

3. **Optimization**
   While functional, using `try...finally` for control flow is non-idiomatic. You can achieve the same result more cleanly using a set comprehension or set subtraction:
   ```python
   return len({x for x in nums if x > 0})
   # OR
   return len(set(nums) - {0})
   ```
   This avoids the overhead of exception handling when `0` is missing.

4. **Key Algorithmic Pattern**
   **Hashing / Set Properties**: Leveraging the property that only unique non-zero values determine the total number of subtractions needed.
