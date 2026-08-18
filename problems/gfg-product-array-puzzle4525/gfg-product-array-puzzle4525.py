class Solution:
    def productExceptSelf(self, arr):
        ans = []
        prod = 1
        zero = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                prod *= arr[i]
            else:
                zero += 1
                
        for i in range(len(arr)):
            if zero > 1:
                return [0]* len(arr)
            elif arr[i] == 0 and zero == 1:
                ans.append(prod)
            elif arr[i] != 0 and zero == 1:
                ans.append(0)
            elif zero == 0:
                ans.append(prod//arr[i])
                
        # print(ans)
        return ans