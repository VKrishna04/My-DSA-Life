class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = float('-inf')
        while left < right:
            currArea = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, currArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea