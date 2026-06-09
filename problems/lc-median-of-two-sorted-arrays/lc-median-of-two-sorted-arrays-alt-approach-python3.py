class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))
        # p1 = nums1
        # if num1 is not None or nums2 us not None:
