class Solution(object):
    def isPossibleToSplit(self, nums):
        return len(nums) % 2 == 0 and max(Counter(nums).values()) < 3
