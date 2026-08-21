# Mirror Tree

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-mirror-tree` |
| Topics | Tree, Recursion, Depth-First Search |
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

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the number of nodes, as every node is visited exactly once.
*   **Space:** $O(H)$, where $H$ is the height of the tree, due to the recursion stack. In the worst case (a skewed tree), this is $O(N)$. Note that while no auxiliary data structures are used, the hidden stack cost is a frequent oversight in your previous submissions.

**2. Correctness**
The logic is sound. It correctly handles the "empty tree" edge case (`root is None`) and leaf nodes (swapping two `None` children does no harm).

**3. Optimization**
To protect against stack overflow on extremely deep trees, convert this to an **iterative BFS** using a queue (`collections.deque`). This replaces the implicit recursion stack with explicit heap memory.

**4. Key Algorithmic Pattern**
**Recursion (Depth-First Search)**: Specifically, a pre-order traversal where the swap operation is performed before recursing into children.
