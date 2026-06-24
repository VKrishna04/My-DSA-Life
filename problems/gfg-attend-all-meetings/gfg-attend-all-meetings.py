class Solution:
    def canAttend(self, arr):
        sor_i = sorted(range(len(arr)), key= lambda i: arr[i][1])
        
        arr[:] = [arr[i] for i in sor_i]
        
        free = 0
        
        for time in arr:
            if time[0] < free:
                return False
            free = time[1]
        return True