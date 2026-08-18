# Mirror Tree

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-mirror-tree` |
| Topics | Tree |
| Solved | 2026-06-24 |

## Problem Statement

Given the **root **of a binary tree, convert the binary tree to its **Mirror tree. **

**Note:** Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.

**Examples:**

**Input: **root = [1, 2, 3, N, N, 4]
**Output: **[1, 3, 2, N, 4]**
Explanation: **

In the inverted tree, every non-leaf node has its left and right child interchanged.
**Input: **root = [1, 2, 3, 4, 5]
**Output: **[1, 3, 2, N, N, 5, 4]**
Explanation:
**
In the inverted tree, every non-leaf node has its left and right child interchanged.
**Constraints:**
1 &le; number of nodes &le; 104
1 &le; node->data &le; 105

## Solutions

```python3
from collections import deque
'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def mirror(self, root):
        if root is None:
            return

        root.left, root.right = root.right, root.left
        
        self.mirror(root.left)
        self.mirror(root.right)
```
