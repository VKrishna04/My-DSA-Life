# Split the Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-split-the-array::1448742291` |
| Topics | Array, Hash Table, Counting |
| Solved | 2024-11-10 |
| Runtime | 2 ms (beats 60.125%) |
| Memory | 42.6 MB (beats 100%) |

## Problem Statement

You are given an integer array `nums` of **even** length. You have to split the array into two parts `nums1` and `nums2` such that:

	- `nums1.length == nums2.length == nums.length / 2`.

	- `nums1` should contain **distinct **elements.

	- `nums2` should also contain **distinct** elements.

Return `true`_ if it is possible to split the array, and _`false` _otherwise__._

 

**Example 1:**

**Input:** nums = [1,1,2,2,3,4]
**Output:** true
**Explanation:** One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

**Example 2:**

**Input:** nums = [1,1,1,1]
**Output:** false
**Explanation:** The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.

 

**Constraints:**

	- `1 <= nums.length <= 100`

	- `nums.length % 2 == 0 `

	- `1 <= nums[i] <= 100`

## Solutions

```Java
class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        // Count occurrences of each number
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Check if any number has a frequency higher than 2
        for (int frequency : frequencyMap.values()) {
            if (frequency > 2) {
                return false;
            }
        }

        return true;
    }
}
```
