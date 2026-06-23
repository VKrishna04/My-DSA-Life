class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)
        
        # Helper function to check if we can place k cows with 'dist' distance
        def canPlace(dist):
            count = 1  # Place the first cow in the first stall
            last_pos = stalls[0]
            
            for i in range(1, n):
                if stalls[i] - last_pos >= dist:
                    count += 1
                    last_pos = stalls[i]
                if count >= k:
                    return True
            return False

        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlace(mid):
                ans = mid  # This distance is possible, try for a larger one
                low = mid + 1
            else:
                high = mid - 1
                
        return ans