class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        l = len(stones)
        dp = [[0]*(l) for _ in range(l)]
        psum = [0]
        for stone in stones:
            psum.append(psum[-1]+stone)
        for i in range(l-1, -1,-1):
            for j in range(i+1,l):
                dp[i][j] = max(psum[j+1]-psum[i+1]-dp[i+1][j], psum[j]-psum[i]-dp[i][j-1])
        return dp[0][-1]
