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