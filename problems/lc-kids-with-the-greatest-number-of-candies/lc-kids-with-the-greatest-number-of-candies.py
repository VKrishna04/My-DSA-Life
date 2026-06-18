class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        results = [ (i+extraCandies) >= max_candies for i in candies ]
        return results