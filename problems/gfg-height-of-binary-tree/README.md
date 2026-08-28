# Height Of Binary Tree

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-height-of-binary-tree` |
| Topics | Tree |
| Solved | 2026-06-24 |

## Problem Statement

Given the **root **of a binary tree, your task is to find the **maximum depth **of the tree.

**Note: **The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.

**Examples:**

**Input: **root = [12, 8, 18, 5, 11]

**Output:** 2
**Explanation: **One of the longest path from the root(node 12) goes through node 8 to node 5, which has 2 edges.
**Input: **root = [1, 2, 3, 4, N, 10, 5, N, N, N, N, 6, 7]

**Output:** 3
**Explanation: **The longest path from the root(node 1) to a leaf node 6 with 3 edges.
**Constraints:**
1 &le; number of nodes &le; 3*104
0 &le; node->data &le; 105

## AI Review

1.  **Time complexity**: O(N), where N is the number of nodes. Each node is visited exactly once.
2.  **Space complexity**: O(H), where H is the height of the tree. This is due to the recursion stack. In the worst case (a skewed tree), H can be N, leading to O(N) space. (This addresses your recurring flag regarding space complexity).
3.  **Correctness**: The core logic is a standard recursive approach for tree height. However, the solution returns a height that is off by one from typical definitions. For an empty tree, it returns -1. For a single-node tree, it returns 0 (e.g., `max(-1,-1)+1`). GeeksForGeeks generally defines the height of a single node tree as 1 and an empty tree as 0. To align with this common definition, the base case `if root is None: return -1` should be `return 0`. This is a common "edge cases" issue related to differing problem definitions.
4.  **Optimization**: This recursive Depth-First Search (DFS) approach is optimal in terms of time complexity (O(N)). No significant algorithmic optimization is applicable.
5.  **Key algorithmic pattern**: Depth-First Search (DFS) using recursion.
