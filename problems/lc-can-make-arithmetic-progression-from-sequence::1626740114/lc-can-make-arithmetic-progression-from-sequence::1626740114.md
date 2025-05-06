# Can Make Arithmetic Progression From Sequence

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-can-make-arithmetic-progression-from-sequence::1626740114` |
| Topics | Array, Sorting |
| Solved | 2025-05-06 |
| Runtime | 0 ms (beats 100%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.

Given an array of numbers `arr`, return `true` _if the array can be rearranged to form an **arithmetic progression**. Otherwise, return_ `false`.

 

**Example 1:**

**Input:** arr = [3,5,1]
**Output:** true
**Explanation: **We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

**Example 2:**

**Input:** arr = [1,2,4]
**Output:** false
**Explanation: **There is no way to reorder the elements to obtain an arithmetic progression.

 

**Constraints:**

	- `2 <= arr.length <= 1000`

	- `-106 <= arr[i] <= 106`

## Solutions

```Python3
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                diff = arr[1] - arr[0]
            if (i != 0) and (i != len(arr)-1):
                if arr[i] - arr[i-1] != arr[i+1] - arr[i] != diff:
                    return False
        return True
```
