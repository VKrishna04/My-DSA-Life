from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter([num for num in nums if num % 2 == 0])
        
        most_frequent_even = -1
        max_count = 0

        for num, count in counts.items():
            if count > max_count or (count == max_count and num < most_frequent_even):
                most_frequent_even = num
                max_count = count

        return most_frequent_even
