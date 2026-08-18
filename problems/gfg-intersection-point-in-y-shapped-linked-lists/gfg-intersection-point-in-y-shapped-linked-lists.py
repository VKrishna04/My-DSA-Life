'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        temp1 = head1
        temp2 = head2
        while temp1 != temp2:
            
            if temp1.next == None:
                temp1 = head1
            else:
                temp1 = temp1.next
            if temp2.next == None:
                temp2 = head2
            else:
                temp2 = temp2.next
            
        return temp1