class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max([num for num, count in Counter(nums).items() if count > len(nums)/2])