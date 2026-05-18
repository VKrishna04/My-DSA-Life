# Binary Tree Maximum Path Sum

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Leetcode |
| Problem ID | `lc-binary-tree-maximum-path-sum` |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Solved | 2026-05-09 |
| Runtime | 7 ms (beats 78.2943%) |
| Memory | 23.9 MB (beats 61.6619%) |

## Problem Statement

A **path** in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence **at most once**. Note that the path does not need to pass through the root.

The **path sum** of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return _the maximum **path sum** of any **non-empty** path_.

 

**Example 1:**

**Input:** root = [1,2,3]
**Output:** 6
**Explanation:** The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

**Example 2:**

**Input:** root = [-10,9,20,null,null,15,7]
**Output:** 42
**Explanation:** The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 3 * 104]`.

	- `-1000 <= Node.val <= 1000`

## Solutions

```Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            if not node: return 0
            nonlocal res

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            res = max(res, left + node.val + right)

            return node.val + max(left, right)
        
        dfs(root)
        return res
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the number of nodes. Each node is visited exactly once.
*   **Space:** $O(H)$, where $H$ is the tree height, representing the recursion stack depth. In the worst case (skewed tree), this is $O(N)$.

**2. Correctness**
The solution is **correct**. It properly handles:
*   **Negative values:** Using `max(0, dfs(...))` effectively "ignores" paths that decrease the total sum.
*   **Global Maximum:** The `res` variable correctly tracks paths that peak at the current node but aren't returned to the parent.
*   **Single Node:** Correctly returns the node's value if it's the only element.

**3. Optimization**
The logic is already highly efficient. A concrete improvement for production environments or extremely deep trees (where $N > 1000$) is to use an **iterative DFS** using a stack to avoid `RecursionError` (Python's default recursion limit). 

Alternatively, to avoid the `nonlocal` keyword for better encapsulation, you can return a tuple `(max_with_root, max_global)` from the DFS function.

**4. Key Algorithmic Pattern**
*   **Post-order Traversal (Bottom-up DFS):** Information is gathered from children and passed up to the parent to make a local decision.
*   **Dynamic Programming on Trees:** Using sub-problem results (max path from child) to solve the larger problem.
