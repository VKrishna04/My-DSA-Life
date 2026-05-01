class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        m = 2 * 32

        dp = [0]*(target+1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i < num:
                    continue
                dp[i] += dp[i-num]
        return dp[-1]