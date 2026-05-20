# Find Minimum in Rotated Sorted Array

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-find-minimum-in-rotated-sorted-array` |
| Topics | Array, Binary Search |
| Solved | 2025-12-31 |
| Runtime | 2 ms (beats 3.5203999999999938%) |
| Memory | 17.4 MB (beats 100%) |

## Problem Statement

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

	- `[4,5,6,7,0,1,2]` if it was rotated `4` times.

	- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return _the minimum element of this array_.

You must write an algorithm that runs in `O(log n) time`.

 

**Example 1:**

**Input:** nums = [3,4,5,1,2]
**Output:** 1
**Explanation:** The original array was [1,2,3,4,5] rotated 3 times.

**Example 2:**

**Input:** nums = [4,5,6,7,0,1,2]
**Output:** 0
**Explanation:** The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

**Example 3:**

**Input:** nums = [11,13,15,17]
**Output:** 11
**Explanation:** The original array was [11,13,15,17] and it was rotated 4 times. 

 

**Constraints:**

	- `n == nums.length`

	- `1 <= n <= 5000`

	- `-5000 <= nums[i] <= 5000`

	- All the integers of `nums` are **unique**.

	- `nums` is sorted and rotated between `1` and `n` times.

## Hints

<details>
<summary>Hint 1</summary>

Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].

</details>

<details>
<summary>Hint 2</summary>

You can divide the search space into two and see which direction to go.
Can you think of an algorithm which has O(logN) search complexity?

</details>

<details>
<summary>Hint 3</summary>

- All the elements to the left of inflection point > first element of the array.

- All the elements to the right of inflection point < first element of the array.

</details>

## Solutions

```Python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        for i in range(len(nums)):
            if nums[0] > nums[i]:
                               
                return nums[i]

```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(N)$. In the worst case, the loop iterates through the entire list to find the pivot point.
*   **Space Complexity:** $O(1)$. It uses a constant amount of extra space regardless of input size.

### 2. Correctness
The solution is **correct** for the problem constraints (unique elements).
*   **Edge Cases:** It correctly handles single-element arrays and already-sorted arrays via the initial `if nums[0] <= nums[-1]` check.
*   **Failure:** While correct, it fails the typical LeetCode follow-up requirement for an $O(\log N)$ solution.

### 3. Optimization
The optimal approach is **Binary Search** to achieve **$O(\log N)$** time. 
*   **Logic:** Compare `nums[mid]` with `nums[high]`. If `nums[mid] > nums[high]`, the minimum must be in the right half (`low = mid + 1`). Otherwise, it is in the left half including `mid` (`high = mid`).

### 4. Key Algorithmic Pattern
The current solution uses **Linear Search**. The intended pattern for this "Medium" problem is **Binary Search on a rotated sorted property**.
