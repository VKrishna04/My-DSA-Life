class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l = len(piles)
        dp = [[0]*(l) for _ in range(l)]

        psum = [0]
        for pile in piles:
            psum.append(psum[-1]+pile)

        for i in range(l-1, -1, -1):
            for j in range(i+1, l):
                dp[i][j] = max(psum[j+1]-psum[i+1] - dp[i+1][j], psum[j]-psum[i] - dp[i][j-1])
        return True if dp[0][-1] > 0 else False