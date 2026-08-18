class Solution:
    def minCoins(self, coins, sum):
        coins.sort()
        dp = [0] * (sum + 1)
        
        for i in range(1, sum+1):
            dp[i] = float('inf')
            
            for coin in coins:
                diff = i  - coin
                if diff < 0:
                    break
                dp[i] = min(dp[i], dp[diff] + 1)
        
        if dp[sum] != float('inf'):
            return dp[sum]
        return -1