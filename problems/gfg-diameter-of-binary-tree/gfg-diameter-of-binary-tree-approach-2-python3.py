'''
# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    
    def height(self, root, maxi):
        if not root:
            return 0
        sum1 = 0
        lheight = self.height(root.left, maxi)
        rheight = self.height(root.right, maxi)
        
        sum1 = lheight + rheight
        maxi[0] = max(maxi[0], sum1)
        
        return 1 + max(lheight, rheight)
    
    
    def diameter(self, root):
        maxi = [0]
        self.height(root, maxi)
        return maxi[0]