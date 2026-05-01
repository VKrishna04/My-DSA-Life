class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(len(strs)):
            strs[i] = [strs[i], strs[i].count('0'), strs[i].count('1')]

        for s in strs:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i < s[1] or j < s[2]:
                        continue
                    dp[i][j] = max(dp[i][j], dp[i-s[1]][j-s[2]] + 1)
        
        return dp[-1][-1]