class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        negative_list = []
        positive_list = []

        for num in nums:
            if num < 0:
                negative_list.append(num)
            else:
                positive_list.append(num)

        negative_list.sort(reverse = True)
        positive_list.sort()
        if not negative_list:
            return positive_list[0]
        if not positive_list:
            return negative_list[0]

        if positive_list[0] == -negative_list[0]:
            return positive_list[0]
        return positive_list[0] if positive_list[0] < -negative_list[0] else negative_list[0]