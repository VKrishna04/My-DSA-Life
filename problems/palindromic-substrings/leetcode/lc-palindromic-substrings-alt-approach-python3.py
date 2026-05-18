class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        count = 0

        for i in range(l-1,-1,-1):
            dp[i][i] = 1
            count += 1
            for j in range(i+1,l):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    count += 1
                else:
                    dp[i][j] = False
        return count