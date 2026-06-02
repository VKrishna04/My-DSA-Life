# Single Number III

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-single-number-iii` |
| Topics | Array, Bit Manipulation |
| Solved | 2024-10-19 |
| Runtime | 2 ms (beats 74%) |
| Memory | 18.8 MB (beats 100%) |

## Problem Statement

Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in **any order**.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

**Example 1:**

**Input:** nums = [1,2,1,3,2,5]
**Output:** [3,5]
**Explanation: ** [5, 3] is also a valid answer.

**Example 2:**

**Input:** nums = [-1,0]
**Output:** [-1,0]

**Example 3:**

**Input:** nums = [0,1]
**Output:** [1,0]

 

**Constraints:**

	- `2 <= nums.length <= 3 * 104`

	- `-231 <= nums[i] <= 231 - 1`

	- Each integer in `nums` will appear twice, only two integers will appear once.

## Solutions

```Python3
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        key_items = []
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 0
        print(frequency)
        for key, value in frequency.items():
            if value == 0:
                key_items.append(key)
        return key_items
```

## AI Review

### 1. Complexity
*   **Time Complexity**: $O(n)$ — The algorithm iterates through the input list once to build the map and once through the map to find the result.
*   **Space Complexity**: $O(n)$ — In the worst case, the hash map stores approximately $n/2$ entries.

### 2. Correctness
The code is **correct** given the problem's constraints (exactly two numbers appear once, all others appear twice). However, the initialization `frequency[num] = 0` is unconventional; if a number appeared three times, it would no longer have a value of `0` and would be excluded, which is fragile logic for general frequency counting.

### 3. Optimization
The optimal approach uses **Bit Manipulation (XOR)** to achieve **$O(1)$ space**:
1.  XOR all numbers to get `xor_sum = a ^ b`.
2.  Find the rightmost set bit: `diff = xor_sum & -xor_sum`.
3.  Partition all numbers into two groups based on whether they have this bit set and XOR each group separately.
4.  The two results are the unique numbers.

### 4. Key Algorithmic Pattern
**Frequency Counting** (using a Hash Map/Dictionary).
