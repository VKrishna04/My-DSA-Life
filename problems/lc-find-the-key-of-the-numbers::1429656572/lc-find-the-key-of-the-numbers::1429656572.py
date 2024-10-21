class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> str:
        nums = [str(num).zfill(4) for num in [num1, num2, num3]]
        key = ''.join(min(num[i] for num in nums) for i in range(4))
        return int(key)
