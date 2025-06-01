# Pascal's Triangle

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-pascals-triangle::1650929295` |
| Topics | Array, Dynamic Programming |
| Solved | 2025-06-01 |
| Runtime | 0 ms (beats 100%) |
| Memory | 18 MB (beats 100%) |

## Problem Statement

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

 

**Example 1:**

**Input:** numRows = 5
**Output:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
**Example 2:**

**Input:** numRows = 1
**Output:** [[1]]

 

**Constraints:**

	- `1 <= numRows <= 30`

## Solutions

```Python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # new = [[0], [1], [0]]
        
        # for i in range(numRows):
        #     new.append(list(new[i-1] + new[i]) for i in range(len(new)))
        
        
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows-1)
        pre = prev[-1]
        cur = [1]

        for i in range(1, numRows-1):
            cur.append(pre[i-1] + pre[i])
        
        cur.append(1)
        prev.append(cur)

        return prev


        return ans


```
