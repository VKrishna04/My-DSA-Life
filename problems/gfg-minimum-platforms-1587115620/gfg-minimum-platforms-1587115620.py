import heapq
class Solution:    
    def minPlatform(self, arr, dep):
        sor_i = sorted(range(len(arr)), key=lambda i: arr[i])
        dep[:] = [dep[i] for i in sor_i]
        arr[:] = [arr[i] for i in sor_i]
        
        platforms = [dep[0]]
        heapq.heapify(platforms)
        
        for i in range(1,len(arr)):
            if arr[i] > platforms[0]:
                heapq.heappop(platforms)
            heapq.heappush(platforms, dep[i])
        return len(platforms)    