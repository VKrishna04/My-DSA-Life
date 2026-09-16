class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf') 
        
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            i = k + 1
            j = len(nums) - 1
            
            while i < j:
                temp = nums[k] + nums[i] + nums[j]
                
                if temp == target:
                    return temp
                
                if abs(target - temp) < abs(target - closest_sum):
                    closest_sum = temp
                
                if temp < target:
                    i += 1
                else:
                    j -= 1
                    
        return closest_sum