# Intersection Point In Y Shapped Linked Lists

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-intersection-point-in-y-shapped-linked-lists` |
| Topics | Linked List, Two Pointers |
| Solved | 2026-06-24 |

## Problem Statement

You are given the heads of two non-empty singly linked lists, **head1** and **head2**, that intersect at a certain point. Return that **Node **where these two linked lists **intersect**.

**Note:** It is guaranteed that the intersected node always exists.

In the custom input you have to give input for CommonList which pointed at the end of both head1 and head2 to form a Y-shaped linked list.
**Examples:**

**Input: **head1: 10 -> 15 -> 30, head2: 3 -> 6 -> 9 -> 15 -> 30
**Output:** 15
**Explanation: **From the above image, it is clearly seen that the common part is 15 -> 30, whose starting point is 15.
    

**Input: **head1: 4 -> 1 -> 8 -> 5, head2: 5 -> 6 -> 1 -> 8 -> 5
**Output: **1
**Explanation: **From the above image, it is clearly seen that the common part is 1 -> 8 -> 5, whose starting point is 1.
    
**Constraints:
**2 &le; total number of nodes &le; 2*105
-104 &le; node->data &le; 104

## Solutions

```python3
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
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(N + M)$ in the corrected version; currently, it can result in an infinite loop if lengths differ.
*   **Space Complexity:** $O(1)$ as only two pointers are used.

**2. Correctness**
The code is **incorrect**.
*   **Logic Error:** When `temp1` reaches the end, it resets to `head1` instead of `head2`. To synchronize the distance traveled, a pointer must switch to the **opposite** list's head.
*   **Edge Case:** If the lists have different lengths and an intersection exists, the current logic will never align the pointers, causing an infinite loop.
*   **Termination:** It does not handle cases where no intersection exists (it should eventually return `None`).

**3. Optimization**
Apply the **Two-Pointer Switching Technique**: When `temp1` reaches `None`, reassign it to `head2`. When `temp2` reaches `None`, reassign it to `head1`. They will meet at the intersection node or `None` in exactly $N+M$ steps.

**4. Key Algorithmic Pattern**
Two Pointers (specifically the "Length Synchronization" variant).
