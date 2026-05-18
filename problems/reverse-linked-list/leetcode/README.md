# Reverse Linked List

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-reverse-linked-list` |
| Topics | Linked List, Recursion |
| Solved | 2026-04-12 |
| Runtime | 3 ms (beats 7.476800000000001%) |
| Memory | 20.4 MB (beats 91.822%) |

## Problem Statement

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

 

**Example 1:**

**Input:** head = [1,2,3,4,5]
**Output:** [5,4,3,2,1]

**Example 2:**

**Input:** head = [1,2]
**Output:** [2,1]

**Example 3:**

**Input:** head = []
**Output:** []

 

**Constraints:**

	- The number of nodes in the list is the range `[0, 5000]`.

	- `-5000 <= Node.val <= 5000`

 

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solutions

```Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev = None
        while head != None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
```

## AI Review

### 1. Complexity
*   **Time:** $O(N)$, where $N$ is the number of nodes; the list is traversed exactly once.
*   **Space:** $O(1)$, as the reversal is done in-place using only a few pointer variables.

### 2. Correctness
The solution is fully correct. It successfully handles all primary scenarios:
*   **Empty list:** Returns `None`.
*   **Single node:** Returns the node as-is.
*   **Standard list:** Correctly reassigns pointers without losing the rest of the list.
The initial `if` statement is logically correct but technically redundant, as the `while` loop naturally handles empty and single-node lists.

### 3. Optimization
Use **Pythonic tuple unpacking** to eliminate the explicit `temp` variable and the redundant base-case check. This makes the logic more concise and idiomatic:

```python
curr, prev = head, None
while curr:
    curr.next, prev, curr = prev, curr, curr.next
return prev
```

### 4. Key Algorithmic Pattern
**Iterative In-place Reversal** (a specific application of the **Two-Pointer** technique).
