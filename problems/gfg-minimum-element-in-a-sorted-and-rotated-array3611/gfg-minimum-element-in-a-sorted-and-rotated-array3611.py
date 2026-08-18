class Solution:
    def findMin(self, arr):
        l, r = 0, len(arr)-1
        
        while l < r:
            mid = (l + r) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                r = mid
        
        return arr[l]