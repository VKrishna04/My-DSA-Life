class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        output = float('inf')
        for i in range(n - 2):
            for j in range(i+1, n-1):
                if nums[i] < nums[j]:
                    for k in range(j+1,n):
                        if nums[k] < nums[j]:
                            output = min(output, nums[i]+nums[j]+nums[k])
        return output if output != float('inf') else -1