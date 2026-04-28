class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[float('inf')]*len(arr) for _ in range(len(arr))]

        for i in range(len(arr)):
            dp[i][i] = 0
        
        for i in range(len(arr)-1, -1, -1):

            for j in range(i+1, len(arr)):

                for k in range(i, j):
                    rcost = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    tcost = rcost + dp[i][k] + dp[k+1][j]
                    dp[i][j] = min(dp[i][j], tcost)
        return dp[0][-1]