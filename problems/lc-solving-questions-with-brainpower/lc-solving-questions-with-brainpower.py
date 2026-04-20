class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        l = len(questions)
        dp = [0]*(l+1)
        for i in range(l-1,-1,-1):
            skip = dp[min(l-1,i+1)]
            nexti = i + questions[i][1] + 1
            solve = questions[i][0] + dp[min(l, nexti)]
            dp[i] = max(skip,solve)
        return dp[0]