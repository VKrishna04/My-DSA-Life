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
