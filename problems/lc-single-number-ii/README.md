# Single Number II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-single-number-ii` |
| Topics | Array, Bit Manipulation |
| Solved | 2024-10-19 |
| Runtime | 0 ms (beats 100%) |
| Memory | 18.7 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. _Find the single element and return it_.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

**Example 1:**

**Input:** nums = [2,2,3,2]
**Output:** 3
**Example 2:**

**Input:** nums = [0,1,0,1,0,1,99]
**Output:** 99

 

**Constraints:**

	- `1 <= nums.length <= 3 * 104`

	- `-231 <= nums[i] <= 231 - 1`

	- Each element in `nums` appears exactly **three times** except for one element which appears **once**.

## Solutions

```Python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 0
        print(frequency)
        for key, value in frequency.items():
            if value == 0:
                return key
```

## AI Review

### 1. Complexity
*   **Time:** $O(N)$ — You iterate through the list once and then through the dictionary keys.
*   **Space:** $O(N)$ — In the worst case, you store $N/3 + 1$ unique elements in the dictionary.

### 2. Correctness
*   **Logic:** The code is logically correct for this specific constraint (exactly one element appears once, others appear thrice). By initializing at `0`, the unique element remains at `0` while others reach `2`. 
*   **Edge Cases:** It handles negative numbers and single-element arrays correctly. It would only fail if the constraints changed (e.g., if an element appeared twice instead of thrice).

### 3. Optimization
To achieve the **$O(1)$ space complexity** usually required for this problem, use **Bit Manipulation**:
```python
ones, twos = 0, 0
for num in nums:
    ones = (ones ^ num) & ~twos
    twos = (twos ^ num) & ~ones
return ones
```
This tracks bits that appear once and twice without storing every element.

### 4. Key Algorithmic Pattern
*   **Current Code:** Frequency Counting (Hash Map).
*   **Optimal Approach:** Bit Manipulation (specifically, a Finite State Machine logic).
