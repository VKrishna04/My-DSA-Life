# Course Schedule II

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-course-schedule-ii` |
| Topics | Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Solved | 2026-05-19 |
| Runtime | 0 ms (beats 100%) |
| Memory | 21 MB (beats 30.63790000000003%) |

## Problem Statement

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course `bi` first if you want to take course `ai`.

	- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return _the ordering of courses you should take to finish all courses_. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

 

**Example 1:**

**Input:** numCourses = 2, prerequisites = [[1,0]]
**Output:** [0,1]
**Explanation:** There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

**Example 2:**

**Input:** numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
**Output:** [0,2,1,3]
**Explanation:** There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

**Example 3:**

**Input:** numCourses = 1, prerequisites = []
**Output:** [0]

 

**Constraints:**

	- `1 <= numCourses <= 2000`

	- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`

	- `prerequisites[i].length == 2`

	- `0 <= ai, bi < numCourses`

	- `ai != bi`

	- All the pairs `[ai, bi]` are **distinct**.

## Solutions

```Python3
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course) 
            
        visited = set()
        path = set()
        order = []
        
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
            
            order.append(node)
            
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return [] 
                
        return order[::-1]
```

## AI Review

### 1. Complexity
*   **Time:** $O(V + E)$, where $V$ is the number of courses and $E$ is the number of prerequisites. Every node and edge is processed exactly once.
*   **Space:** $O(V + E)$. The adjacency list consumes $O(V + E)$, while the recursion stack and sets (`visited`, `path`) consume $O(V)$.

### 2. Correctness
The logic is **correct**. 
*   It successfully detects cycles using the `path` set (back-edges).
*   It handles disconnected components by iterating through all nodes in the main loop.
*   **Edge Cases:** Handles $E=0$ (no prerequisites), self-loops, and large $V$ correctly.

### 3. Optimization
Replace the two sets (`visited`, `path`) with a single **state array** (e.g., `state = [0] * numCourses`). 
*   `0`: Unvisited
*   `1`: Visiting (currently in recursion stack)
*   `2`: Visited (fully processed)

This reduces hashing overhead and improves constant-time performance by using direct index access instead of set lookups.

### 4. Key Algorithmic Pattern
**Topological Sort** using **DFS (Post-order Traversal)** and **Cycle Detection**.
