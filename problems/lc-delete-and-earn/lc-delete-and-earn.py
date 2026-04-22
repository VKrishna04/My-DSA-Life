class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        dp = [0]*(m+1)

        for num in nums:
            dp[num] += num

        prev, curr = 0, 0

        for p in dp:
            prev, curr = curr, max(curr, prev + p)

        return curr