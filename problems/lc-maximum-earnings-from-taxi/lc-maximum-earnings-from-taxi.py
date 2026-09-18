class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        rides_by_end = [[] for _ in range(n + 1)]
        for start, end, tip in rides:
            rides_by_end[end].append((start, tip))

        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            
            for start, tip in rides_by_end[i]:
                earnings = dp[start] + (i - start + tip)
                dp[i] = max(dp[i], earnings)
                
        return dp[n]