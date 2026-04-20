class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                for step in [k-1, k, k+1]:
                    if step > 0:
                        landing = stone + step
                        if landing in dp:
                            dp[landing].add(step)
        return len(dp[stones[-1]]) > 0