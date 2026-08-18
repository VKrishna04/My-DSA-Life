# Merge Two Sorted Linked Lists

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-merge-two-sorted-linked-lists` |
| Topics | Linked List |
| Solved | 2026-06-24 |

## Problem Statement

Given the **head** of two **sorted linked lists **consisting of nodes respectively. **Merge** both lists and return the **head **of the **sorted merged list**.

**Examples:**

**Input:
**  
**Output: **2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40**
Explanation:
**   
**Input**:
  
**Output: **1 -> 1 -> 2 -> 4**
Explanation:
  
**
**Constraints:**
1 &le; list1.size, list2.size &le; 103
0 &le; node->data &le; 105

## Solutions

```python3
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
                
```
