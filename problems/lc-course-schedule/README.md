# Course Schedule

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-course-schedule` |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Solved | 2026-05-19 |
| Solve Time | 50s |
| Runtime | 3 ms (beats 87.338%) |
| Memory | 21.5 MB (beats 15.1222%) |

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

	- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

 

**Example 1:**

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** true
**Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

**Example 2:**

**Input:** numCourses = 2, prerequisites = [[1,0],[0,1]]
**Output:** false
**Explanation:** There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

**Constraints:**

	- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= 5000`

	- `prerequisites[i].length == 2`

	- `0 <= ai, bi < numCourses`

	- All the pairs prerequisites[i] are **unique**.

## Solutions

```Python3
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for courses, pre in prerequisites:
            adj[pre].append(courses)
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            
            path.remove(node)
            visited.add(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
```

## AI Review

**1. Complexity**
*   **Time:** $O(V + E)$, where $V$ is the number of courses and $E$ is the number of prerequisites. Each node and edge is traversed once.
*   **Space:** $O(V + E)$ to store the adjacency list, plus $O(V)$ for the recursion stack and tracking sets.

**2. Correctness**
The solution is **correct**. It properly implements DFS-based cycle detection in a directed graph.
*   **`path`** (recursion stack) identifies back-edges (cycles).
*   **`visited`** prevents redundant processing of previously verified subgraphs.
*   **Edge cases:** Handles disconnected components, self-loops, and empty prerequisites correctly.

**3. Concrete Optimization**
Replace the two sets (`visited`, `path`) with a single **state array** (e.g., `states = [0] * numCourses`).
*   `0`: Unvisited
*   `1`: Visiting (currently in recursion stack)
*   `2`: Visited (fully processed)
This avoids the overhead of hashing and multiple set lookups/modifications, improving cache locality and performance.

**4. Key Algorithmic Pattern**
**DFS Cycle Detection** (or the DFS-based approach to **Topological Sort**). The graph is a Directed Acyclic Graph (DAG) if and only if no back-edges exist.
