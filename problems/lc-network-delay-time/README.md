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

Here's a review of your solution:

1.  **Time & Space Complexity:**
    *   **Time:** O(E log V), where V is the number of nodes (n) and E is the number of edges (`len(times)`). This accounts for building the adjacency list (O(E)) and Dijkstra's algorithm with a min-heap (V pops, E pushes, each O(log V) for heap operations).
    *   **Space:** O(V + E) for the adjacency list, `visited` set, and the priority queue (heap).

2.  **Correctness:**
    The solution correctly implements Dijkstra's algorithm, suitable for graphs with non-negative edge weights. It accurately finds the maximum shortest path time to all reachable nodes from `k` and correctly returns -1 if not all `n` nodes are reachable. It handles edge cases like `n=1` or disconnected graphs well.

3.  **Concrete Optimisation:**
    Instead of just using `visited`, maintain a `dist` array (e.g., `dist = [float('inf')] * (n + 1)`) initialized to infinity, with `dist[k] = 0`. When iterating neighbors, only `heappush((new_time, neighbor))` if `new_time < dist[neighbor]`, and then update `dist[neighbor] = new_time`. This prevents redundant, longer paths from being added to the heap, potentially reducing heap size and operations.

4.  **Key Algorithmic Pattern:**
    Dijkstra's Algorithm (a priority queue-based variant of Breadth-First Search for finding shortest paths in weighted graphs with non-negative edges).
