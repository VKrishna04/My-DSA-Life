# Detect Cycle In An Undirected Graph

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-detect-cycle-in-an-undirected-graph` |
| Topics | DFS, Graph, union-find, Data Structures, Algorithms |
| Solved | 2026-06-24 |

## Problem Statement

Given an **undirected graph **with **V** vertices and** E **edges, represented as a 2D vector **edges[][]**, where each entry **edges[i] = [u, v]** denotes an edge between vertices **u** and **v**, determine whether the graph contains a **cycle **or not. 

**Note:** The graph can have multiple component.

**Examples:**

**Input: **V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
**Output: **true
**Explanation:** 
 
1 -> 2 -> 0 -> 1 is a cycle.

**Input: **V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
**Output: **false
**Explanation: 
** 
No cycle in the graph.

**Constraints:
**1 &le; V, E &le; 105
0 &le; edges[i][0], edges[i][1] < V
