class Solution:
    def maxSubarraySum(self, arr):
        max_sum = float('-inf')
        curr = 0
        
        for num in arr:
            curr += num
            max_sum = max(max_sum, curr)
            
            if curr < 0: curr =  0
        return max_sum