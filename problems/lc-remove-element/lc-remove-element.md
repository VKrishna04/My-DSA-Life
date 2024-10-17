# Remove Element

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-remove-element` |
| Topics | Array, Two Pointers |
| Solved | 2024-10-17 |
| Runtime | 0 ms (beats 100%) |
| Memory | 16.7 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return _the number of elements in _`nums`_ which are not equal to _`val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

	- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.

	- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be **accepted**.

 

**Example 1:**

**Input:** nums = [3,2,2,3], val = 3
**Output:** 2, nums = [2,2,_,_]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

**Input:** nums = [0,1,2,2,3,0,4,2], val = 2
**Output:** 5, nums = [0,1,4,0,3,_,_,_]
**Explanation:** Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

 

**Constraints:**

	- `0 <= nums.length <= 100`

	- `0 <= nums[i] <= 50`

	- `0 <= val <= 100`

## Solutions

```Python3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)        
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n^2)$. While the `while` loop runs $n$ times, `nums.pop(i)` is an $O(n)$ operation because it requires shifting all subsequent elements to the left.
*   **Space Complexity:** $O(1)$. Modifications are made in-place.

### 2. Correctness
The code is **correct**. It avoids the common mistake of skipping elements after a deletion by only incrementing `i` when no element is popped. It handles edge cases like empty lists, lists where all elements match `val`, or no elements match `val`.

### 3. Optimization
Replace the $O(n^2)$ `pop()` method with an $O(n)$ **Two-Pointer** overwrite strategy. Instead of deleting, overwrite elements that should be kept:

```python
def removeElement(self, nums: List[int], val: int) -> int:
    k = 0  # Write pointer
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
```
This reduces time complexity to $O(n)$ by eliminating expensive array shifts.

### 4. Key Algorithmic Pattern
**Two Pointers** (specifically the "Read/Write" pointer technique). One pointer iterates through the array, while the other tracks the position for the next valid element.
