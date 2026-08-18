#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        sum1 = sum(arr)
        expected = (n)*(n+1)/2
        
        return int(expected - sum1)

