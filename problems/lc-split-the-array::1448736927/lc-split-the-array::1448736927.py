class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for num in counter.values():
            if num > 2:
                return False
        return True