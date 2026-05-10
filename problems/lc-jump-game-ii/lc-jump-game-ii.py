class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currjump = 0
        right = 0

        for i in range(len(nums) - 1):
            right = max(right, i + nums[i])

            if i == currjump:
                jumps += 1
                currjump = right
        
        return jumps