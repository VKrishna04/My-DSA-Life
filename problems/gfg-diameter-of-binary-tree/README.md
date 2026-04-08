# Diameter of a Binary Tree

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-diameter-of-binary-tree` |
| Topics | Tree |
| Solved | 2026-04-08 |

## Problem Statement

My Submissions__Refresh

 Time (IST)StatusMarksLangTest CasesCode2026-04-08 23:06:36Correct0python31111 / 1111View Sync2026-04-08 22:32:57Correct4python31111 / 1111View Sync2026-04-08 20:39:05Wrong0python32 / 1111View

## Solutions

### Approach 1 (python3)

Synced from submissions table — 2026-04-08 22:32:57

```Python3
'''
# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    
    def height(self, root, maxi):
        if not root:
            return 0

        lheight = self.height(root.left, maxi)
        rheight = self.height(root.right, maxi)
        
        sum1 = lheight + rheight
        maxi[0] = max(maxi[0], sum1)
        
        return 1 + max(lheight, rheight)
    
    
    def diameter(self, root):
        maxi = [0]
        self.height(root, maxi)
        return maxi[0]
```
