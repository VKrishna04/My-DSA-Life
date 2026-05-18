class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        n = len(res)
        return (res[n//2] + res[(n-1)//2]) / 2