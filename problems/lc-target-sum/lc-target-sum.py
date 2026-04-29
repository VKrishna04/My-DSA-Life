class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totsum = sum(nums)
        if abs(target) > totsum:
            return 0
        if (totsum + target) %2 != 0:
            return 0
        
        P = (totsum + target) // 2
        dp = [0]*(P+1)
        dp[0]=1
        
        for num in nums:
            for w in range(P, num-1, -1):
                dp[w] = dp[w] + dp[w-num]
        return dp[-1]