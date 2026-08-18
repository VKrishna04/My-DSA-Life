class Solution:
    def maxChildren(self, greed, cookie):
        l = 0
        r = 0
        greed.sort()
        cookie.sort()
        
        while r < len(greed) and l < len(cookie):
            if greed[r] <= cookie[l]:
                r += 1
            l += 1
        
        return r