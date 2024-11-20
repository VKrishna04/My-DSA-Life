# Maximum Number of Operations With the Same Score I

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-maximum-number-of-operations-with-the-same-score-i` |
| Topics | Array, Simulation |
| Solved | 2025-08-10 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.9 MB (beats 100%) |

## Problem Statement

You are given an array of integers `nums`. Consider the following operation:

	- Delete the first two elements `nums` and define the _score_ of the operation as the sum of these two elements.

You can perform this operation until `nums` contains fewer than two elements. Additionally, the **same** _score_ must be achieved in **all** operations.

Return the **maximum** number of operations you can perform.

 

**Example 1:**

**Input:** nums = [3,2,1,4,5]

**Output:** 2

**Explanation:**

	- We can perform the first operation with the score `3 + 2 = 5`. After this operation, `nums = [1,4,5]`.

	- We can perform the second operation as its score is `4 + 1 = 5`, the same as the previous operation. After this operation, `nums = [5]`.

	- As there are fewer than two elements, we can't perform more operations.

**Example 2:**

**Input:** nums = [1,5,3,3,4,1,3,2,2,3]

**Output:** 2

**Explanation:**

	- We can perform the first operation with the score `1 + 5 = 6`. After this operation, `nums = [3,3,4,1,3,2,2,3]`.

	- We can perform the second operation as its score is `3 + 3 = 6`, the same as the previous operation. After this operation, `nums = [4,1,3,2,2,3]`.

	- We cannot perform the next operation as its score is `4 + 1 = 5`, which is different from the previous scores.

**Example 3:**

**Input:** nums = [5,3]

**Output:** 1

 

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 <= nums[i] <= 1000`

## Solutions

```Python3
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0]+nums[1]
        count = 1
        for i in range(2,len(nums)-1,2):
            if nums[i] + nums[i+1] == score:
                count += 1
            else:
                break
        return count
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. The loop processes pairs of elements once.
*   **Space Complexity:** $O(1)$. It uses a constant amount of extra space regardless of input size.

**2. Correctness**
The logic is correct. It establishes the target score from the first pair and iterates through subsequent pairs as long as the sum matches. 
*   **Edge Cases:** The constraint $n \ge 2$ ensures `nums[0] + nums[1]` is safe. The loop bound `len(nums) - 1` correctly prevents an `IndexError` on arrays with an odd number of elements (it stops before the lone trailing element).

**3. Optimization**
The current solution is already optimal in terms of complexity. However, for readability and slight overhead reduction in Python, you could use a `while` loop to avoid calculating `len(nums)` repeatedly or use `zip` with slicing:
```python
for a, b in zip(nums[2::2], nums[3::2]):
    if a + b == score: count += 1
    else: break
```
*Note: Slicing creates copies, so for very large $n$, the current index-based approach is more memory-efficient.*

**4. Key Algorithmic Pattern**
**Greedy / Simulation**: The algorithm greedily performs operations from the start of the array as long as the condition is met, stopping at the first mismatch.
