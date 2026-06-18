class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        if flowerbed == [0] and n == 1:
            return True
        i = 0
        l = len(flowerbed)
        while i < l:
            if flowerbed[i] == 1:
                i += 2
            elif i == l - 1 or flowerbed[i+1] == 0:
                n -= 1
                if n == 0:
                    return True
                i += 2
            else:
                i += 3
        return n <= 0
