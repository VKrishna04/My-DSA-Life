class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totsum = sum(stones)
        target = totsum // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for w in range(target, stone - 1, -1):
                if dp[w] or dp[w-stone]:
                    dp[w] = True
         
        for i in range(len(dp)-1,-1,-1):
            if dp[i]:
                return totsum - 2*i