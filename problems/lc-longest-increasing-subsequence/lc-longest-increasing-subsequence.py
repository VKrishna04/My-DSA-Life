class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [] 

        for num in nums: 
            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                low = 0
                high = len(sub) - 1
                while low < high:
                    mid = (low + high) // 2
                    if sub[mid] >= num:
                        high = mid
                    else:
                        low = mid + 1
                
                sub[low] = num
                
        return len(sub)