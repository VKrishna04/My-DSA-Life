class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        m = (10 ** 9) + 7
        if n*k < target:
            return 0
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(1, target+1):
                for f in range(1, k+1):
                    if j - f < 0:
                        continue
                    dp[i][j] = (dp[i-1][j-f] + dp[i][j]) % m
        return dp[-1][-1]