# Max Consecutive Ones

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-max-consecutive-ones::1171315976` |
| Topics | Array |
| Solved | 2024-02-10 |
| Runtime | 3 ms (beats 60.4658%) |
| Memory | 44.9 MB (beats 100%) |

## Problem Statement

Given a binary array `nums`, return _the maximum number of consecutive _`1`_'s in the array_.

 

**Example 1:**

**Input:** nums = [1,1,0,1,1,1]
**Output:** 3
**Explanation:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

**Example 2:**

**Input:** nums = [1,0,1,1,0,1]
**Output:** 2

 

**Constraints:**

	- `1 <= nums.length <= 105`

	- `nums[i]` is either `0` or `1`.

## Solutions

```Java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int j = 0, result = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                j = 0;
                continue;
            }
            j++;
            result = Math.max(j, result);
        }
        return result;
    }
}
```
