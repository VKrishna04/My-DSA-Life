#User function Template for python3
class Solution:
    # Complete the below function
    def twoSum(self,arr, target):
        seen = {}
        
        for i , x in enumerate(arr):
            if target - x in seen:
                return [x, target - x]
            seen[x] = i
        return []