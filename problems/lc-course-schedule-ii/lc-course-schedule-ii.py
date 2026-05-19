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