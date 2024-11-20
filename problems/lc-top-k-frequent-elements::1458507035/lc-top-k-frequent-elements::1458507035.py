from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        heap = [(-count,value) for value,count in map.items()]
        
        heapq.heapify(heap)
        result = []
        for i in range(k):
            element = heapq.heappop(heap)
            result.append(element[1])
        return result
        