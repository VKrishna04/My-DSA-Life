class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 and max(Counter(nums).values()) < 3
