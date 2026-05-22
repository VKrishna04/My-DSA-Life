# Network Delay Time

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-network-delay-time` |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path |
| Solved | 2026-05-22 |
| Runtime | 329 ms (beats 87.1329%) |
| Memory | 21.3 MB (beats 53.87319999999997%) |

## Problem Statement

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return _the **minimum** time it takes for all the_ `n` _nodes to receive the signal_. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

 

**Example 1:**

**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
**Output:** 2

**Example 2:**

**Input:** times = [[1,2,1]], n = 2, k = 1
**Output:** 1

**Example 3:**

**Input:** times = [[1,2,1]], n = 2, k = 2
**Output:** -1

 

**Constraints:**

	- `1 <= k <= n <= 100`

	- `1 <= times.length <= 6000`

	- `times[i].length == 3`

	- `1 <= ui, vi <= n`

	- `ui != vi`

	- `0 <= wi <= 100`

	- All the pairs `(ui, vi)` are **unique**. (i.e., no multiple edges.)

## Solutions

```Python3
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        t = 0
        heap = [(t, k)]
        visited = set()

        while heap:
            time_so_far, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = time_so_far
            
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heappush(heap, (t+weight, neighbor))

        return t if len(visited) == n else -1
```

## AI Review

### Analysis

**1. Complexity**
*   **Time:** $O(E \log E)$ (or $O(E \log V)$), where $E$ is the number of edges and $V$ is the number of nodes. Each edge is processed once via the min-heap.
*   **Space:** $O(V + E)$ to store the adjacency list, the `visited` set, and the heap.

**2. Correctness**
The logic is correct. It successfully implements **Dijkstra’s Algorithm**.
*   **Edge Cases:** It correctly handles disconnected graphs (returns `-1` via the `len(visited)` check) and cycles (via the `visited` set).
*   **Small Note:** The code assumes node labels are $1$ to $n$ (consistent with the problem description).

**3. Optimization**
Use a **distance array** `dist = [float('inf')] * (n + 1)` instead of just a `visited` set. Before pushing to the heap, check if `t + weight < dist[neighbor]`. This prevents pushing redundant, longer paths into the heap, significantly reducing the number of heap operations in dense graphs.

**4. Key Algorithmic Pattern**
**Dijkstra's Algorithm** (Breadth-First Search using a Priority Queue for weighted graphs).
