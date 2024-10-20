# Add Digits

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-add-digits` |
| Topics | Math, Simulation, Number Theory |
| Solved | 2024-10-20 |
| Runtime | 0 ms |
| Memory | 16.6 MB |

## Problem Statement

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

 

**Example 1:**

**Input:** num = 38
**Output:** 2
**Explanation:** The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

**Example 2:**

**Input:** num = 0
**Output:** 0

 

**Constraints:**

	- `0 <= num <= 231 - 1`

 

**Follow up:** Could you do it without any loop/recursion in `O(1)` runtime?
