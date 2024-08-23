# Find Closest Number to Zero

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-find-closest-number-to-zero::1365719223` |
| Topics | Array |
| Solved | 2024-08-23 |
| Runtime | 21 ms (beats 5.960199999999995%) |
| Memory | 44.7 MB (beats 100%) |

## Problem Statement

Given an integer array `nums` of size `n`, return _the number with the value **closest** to _`0`_ in _`nums`. If there are multiple answers, return _the number with the **largest** value_.

 

**Example 1:**

**Input:** nums = [-4,-2,1,4,8]
**Output:** 1
**Explanation:**
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

**Example 2:**

**Input:** nums = [2,-1,1]
**Output:** 1
**Explanation:** 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

 

**Constraints:**

	- `1 <= n <= 1000`

	- `-105 <= nums[i] <= 105`

## Solutions

```Java
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int findClosestNumber(int[] nums) {
        ArrayList<Integer> negative_list = new ArrayList<Integer>();
        ArrayList<Integer> positive_list = new ArrayList<Integer>();

        for (Integer integer : nums) {
            if (integer < 0) {
                negative_list.add(integer);
            } else {
                positive_list.add(integer);
            }
        }

        Collections.sort(negative_list, Collections.reverseOrder());
        Collections.sort(positive_list);

        if (negative_list.isEmpty() && positive_list.isEmpty()) {
            return 0;
        }

        if (negative_list.isEmpty()) {
            return positive_list.get(0);
        }
        if (positive_list.isEmpty()) {
            return negative_list.get(0);
        }

        int closestNegative = negative_list.get(0);
        int closestPositive = positive_list.get(0);

        if (Math.abs(closestNegative) < closestPositive) {
            return closestNegative;
        } else {
            return closestPositive;
        }
    }
}
```
