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