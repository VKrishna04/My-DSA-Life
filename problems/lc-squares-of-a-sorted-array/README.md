# Squares of a Sorted Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-squares-of-a-sorted-array` |
| Topics | Array, Two Pointers, Sorting |
| Solved | 2024-02-17 |
| Runtime | 8 ms (beats 38.82350000000001%) |
| Memory | 47.3 MB (beats 62.78620000000006%) |

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing** order, return _an array of **the squares of each number** sorted in non-decreasing order_.

 

**Example 1:**

**Input:** nums = [-4,-1,0,3,10]
**Output:** [0,1,9,16,100]
**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

**Example 2:**

**Input:** nums = [-7,-3,2,3,11]
**Output:** [4,9,9,49,121]

 

**Constraints:**

	- `1 <= nums.length <= 104`

	- `-104 <= nums[i] <= 104`

	- `nums` is sorted in **non-decreasing** order.

 

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

## Solutions

```Java
import java.util.Arrays;
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] result = nums;
        for (int i = 0; i < nums.length; i++) {
            nums[i] = Math.abs(nums[i]);
        }
        for (int i = 0; i < result.length; i++) {
            result[i] = (int) Math.pow(nums[i], 2);
        }
        Arrays.sort(nums);
        return result;
    }
}
```

## AI Review

### Review

**1. Complexity**
*   **Time:** $O(N \log N)$ due to `Arrays.sort()`. The two linear passes are $O(N)$.
*   **Space:** $O(\log N)$ or $O(1)$ auxiliary space, depending on the implementation of `Arrays.sort()` (Dual-Pivot Quicksort). Note: The code modifies the input array in place.

**2. Correctness**
*   **Logic:** The logic is correct; squaring and then sorting yields the right result. 
*   **Edge Cases:** Handles empty arrays, all negative numbers, and zeros correctly. 
*   **Issues:** `Math.pow` is computationally expensive for simple squaring; `nums[i] * nums[i]` is preferred. `Math.abs` is redundant as squaring naturally removes negative signs.

**3. Optimization**
Use a **Two-Pointer** approach to achieve **$O(N)$ time complexity**. Since the input is sorted, the largest squares are at the boundaries (far left or far right). Compare the absolute values at both ends, place the larger square at the end of a new array, and move the corresponding pointer inward.

**4. Key Algorithmic Pattern**
**Two Pointers** (specifically "Converging Pointers" from the outside in).
