class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for a in range(m):
            if obstacleGrid[a][0] == 1:
                break
            dp[a][0] = 1
        for b in range(n):
            if obstacleGrid[0][b] == 1:
                break
            dp[0][b] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]