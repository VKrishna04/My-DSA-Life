class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # l = len(nums)
        # if nums[0] > 0 or nums[-1] < 0:
        #     return l

        # pos = 0
        # neg = 0
        # for i in range(l):
        #     if nums[i] < 0:
        #         continue
        #     neg = i
        #     if neg > l/2:
        #         return neg

        #     break
        
        # for i in range(neg+1, l):
        #     if nums[i] == 0:
        #         continue
        # pos = l - i
        # return max(neg, pos)

        neg_count = sum(1 for num in nums if num < 0)
        pos_count = sum(1 for num in nums if num > 0)

        return max(neg_count, pos_count)