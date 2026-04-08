'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        if root is None:
            return -1
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        return max(lheight, rheight) + 1