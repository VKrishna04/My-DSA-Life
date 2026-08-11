# Bheem Wants Ladoos

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-bheem-wants-ladoos102404` |
| Topics | Tree |
| Solved | 2026-06-24 |

## Problem Statement

Given the root of a binary tree, a **target **node value, and an integer **k**, return the **sum **of all nodes that are within a distance of **k** from the target node.

The distance between two nodes is defined as the number of edges in the shortest path connecting them.

The target node itself should also be included in the sum.

**Examples:**

**Input: **K = 1, target = 3, root[] = [1, 2, 3, 4, N, 5, 7, 8, 19, N, N, 20, 11, 30, N, 40, 50]

           
          
**Output: **16
**Explanation: **Nodes within distance 1 from 3 are : 1, 5, 7, and 3 itself. So, 1 + 5 + 7 + 3 = 16.
**Input:** k = 2, target = 40, root[] = [1, 2, 3, 4, N, 5, 7, 8, 19, N, N, 20, 11, 30, N, 40, 50]
           
          
**Output: **113
**Explanation: **Nodes within distance 2 from 40 are: 4, 19, 50, and 40 itself. So, 4 + 19 + 50 + 40 = 113

**Constraints:**
1 &le; n &le; 103, where n is the number of nodes.
1 &le; data in nodes, target &le; 105
1 &le; k &le; 20
All the values in the tree are unique.
target is the value of a node that exists in the tree.
