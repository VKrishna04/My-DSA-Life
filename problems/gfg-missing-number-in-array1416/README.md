# Missing Number In Array

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-missing-number-in-array1416` |
| Topics | Array, Searching, Bit Manipulation |
| Solved | 2026-06-24 |

## Problem Statement

You are given an array **arr[]** of size **n - 1** that contains** distinct integers **in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with **one element missing**. Your task is to identify and return the **missing element**.

**Examples:**

**Input: **arr[] = [1, 2, 3, 5]
**Output: **4
**Explanation: **All the numbers from 1 to 5 are present except 4.

**Input: **arr[] = [8, 2, 4, 5, 3, 7, 1]
**Output:** 6
**Explanation: **All the numbers from 1 to 8 are present except 6.
**Input: **arr[] = [1]
**Output: **2
**Explanation: **Only 1 is present so the missing element is 2.

**Constraints:**
1 &le; arr.size() &le; 106
1 &le; arr[i] &le; arr.size() + 1

## Solutions

```python3
#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        sum1 = sum(arr)
        expected = (n)*(n+1)/2
        
        return int(expected - sum1)


```
