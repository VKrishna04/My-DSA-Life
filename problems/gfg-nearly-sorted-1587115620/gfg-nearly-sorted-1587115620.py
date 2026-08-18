from heapq import heapify, heappush, heappop

class Solution:
    def nearlySorted(self, arr, k):  
        heap = arr[:k]
        heapify(heap)
        index = 0
        for i in range(k,len(arr)):
            heappush(heap,arr[i])
            arr[index] = heappop(heap)
            index += 1
        
        for j in range(k):
            arr[index] = heappop(heap)
            index += 1
            
        return arr