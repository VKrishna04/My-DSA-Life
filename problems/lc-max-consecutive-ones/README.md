# Max Consecutive Ones

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-max-consecutive-ones` |
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

## Hints

<details>
<summary>Hint 1</summary>

You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window.

How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

</details>

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
