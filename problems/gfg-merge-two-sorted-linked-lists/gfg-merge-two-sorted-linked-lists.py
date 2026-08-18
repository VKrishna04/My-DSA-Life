'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        dummy = Node(0)
        tail = dummy
        
        while head1 and head2:
            if head1.data > head2.data:
                tail.next = head2
                head2 = head2.next
            else:
                tail.next = head1
                head1 = head1.next
            
            tail = tail.next
            
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next
                