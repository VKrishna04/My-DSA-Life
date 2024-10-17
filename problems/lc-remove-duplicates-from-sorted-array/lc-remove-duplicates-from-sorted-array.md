# Remove Duplicates from Sorted Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-remove-duplicates-from-sorted-array` |
| Topics | Array, Two Pointers |
| Solved | 2024-10-17 |
| Runtime | 58 ms (beats 5.525299999999998%) |
| Memory | 18 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of _unique elements_ in `nums` to be `k**​​​​​​​**`​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

**Custom Judge:**

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be **accepted**.

 

**Example 1:**

**Input:** nums = [1,1,2]
**Output:** 2, nums = [1,2,_]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

**Input:** nums = [0,0,1,1,1,2,2,3,3,4]
**Output:** 5, nums = [0,1,2,3,4,_,_,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

 

**Constraints:**

	- `1 <= nums.length <= 3 * 104`

	- `-100 <= nums[i] <= 100`

	- `nums` is sorted in **non-decreasing** order.

## Solutions

```Python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
```

## AI Review

### Review

1. **Complexity**
   * **Time:** $O(n^2)$. While the loop runs $n$ times, `nums.pop(i)` is an $O(n)$ operation because it requires shifting all subsequent elements.
   * **Space:** $O(1)$. It modifies the input list in-place.

2. **Correctness**
   * **Correct.** The logic handles multiple consecutive duplicates and edge cases (like empty lists or lists with no duplicates) correctly by only incrementing `i` when no deletion occurs.

3. **Optimization**
   Use a **Two-Pointer Overwrite** strategy to achieve **$O(n)$ time**. Instead of popping (which shifts elements), use one pointer to track the unique "write" position and another to scan the array.
   ```python
   k = 1
   for i in range(1, len(nums)):
       if nums[i] != nums[i-1]:
           nums[k] = nums[i]
           k += 1
   return k
   ```

4. **Key Algorithmic Pattern**
   **Two Pointers.** The current solution uses one pointer with an $O(n)$ deletion; the optimal version uses two pointers (slow and fast) to filter data in a single pass.
