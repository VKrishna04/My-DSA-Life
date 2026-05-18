class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        output = float('inf')
        left = [0]*n
        right = [0]*n

        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1,n):
            left[i] = min(left[i-1], nums[i])
        for i in range(n-2,-1,-1):
            right[i] = min(right[i+1], nums[i])
        
        for i in range(n-1):
            if left[i] < nums[i] and right[i] < nums[i]:
                output = min(output, left[i]+nums[i]+right[i])
        
        return output if output != float('inf') else -1