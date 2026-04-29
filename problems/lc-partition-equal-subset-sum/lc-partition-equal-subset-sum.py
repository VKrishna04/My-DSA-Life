class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totsum = sum(nums)
        if totsum % 2 != 0:
            return False
        
        target = totsum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for w in range(target, num-1, -1):
                if dp[w] or dp[w-num]:
                    dp[w] = True
        return dp[-1]