class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minsum = float('inf')
        
        for start in range(n):
            currsum = 0
            for end in range(start, n):
                currsum += nums[end]
                length = end - start + 1
                if l <= length <= r and currsum > 0:
                    minsum = min(minsum, currsum)
        
        return minsum if minsum != float('inf') else -1