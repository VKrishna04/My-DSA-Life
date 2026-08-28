# Maximum Depth of Binary Tree

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-maximum-depth-of-binary-tree` |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Solved | 2025-07-22 |
| Runtime | 3 ms (beats 22.307900000000004%) |
| Memory | 18.9 MB (beats 100%) |

## Problem Statement

Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

**Example 1:**

**Input:** root = [3,9,20,null,null,15,7]
**Output:** 3

**Example 2:**

**Input:** root = [1,null,2]
**Output:** 2

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 104]`.

	- `-100 <= Node.val <= 100`

## Solutions

```Python3
# import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return math.log2(len(root)+1)
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

## AI Review

### 1. Complexity
*   **Time:** $O(N)$, where $N$ is the number of nodes, as each node is visited exactly once.
*   **Space:** $O(H)$, where $H$ is the height of the tree. In the worst case (a skewed tree), this is $O(N)$; in a balanced tree, it is $O(\log N)$ due to the recursive call stack.

### 2. Correctness
The code is **correct**. It properly handles:
*   **Empty Tree:** Returns 0 via the `if not root` check.
*   **Single Node:** Returns $1 + \max(0, 0) = 1$.
*   **Skewed/Balanced Trees:** Correctly propagates the maximum height upwards.

### 3. Optimization
To avoid a `RecursionError` on extremely deep trees (Python's default limit is 1000), use an **Iterative Breadth-First Search (BFS)** using a queue. This manages memory on the heap rather than the stack and can be safer for production-scale constraints.

### 4. Key Algorithmic Pattern
**Recursive Depth-First Search (DFS)** (specifically, a Post-order Traversal) utilizing the **Divide and Conquer** strategy.
