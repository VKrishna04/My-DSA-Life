class Solution:
    def maxProfit(self, prices):
        minp = prices[0]
        ans = 0
        
        for i in range(len(prices)):
            minp = min(minp, prices[i])
            ans = max(ans, prices[i]-minp)
            
        return ans