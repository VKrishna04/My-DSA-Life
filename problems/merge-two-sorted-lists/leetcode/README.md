# Merge Two Sorted Lists

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-merge-two-sorted-lists` |
| Topics | Linked List, Recursion |
| Solved | 2025-07-30 |
| Runtime | 1 ms (beats 18.977900000000005%) |
| Memory | 17.6 MB (beats 100%) |

## Problem Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

 

**Example 1:**

**Input:** list1 = [1,2,4], list2 = [1,3,4]
**Output:** [1,1,2,3,4,4]

**Example 2:**

**Input:** list1 = [], list2 = []
**Output:** []

**Example 3:**

**Input:** list1 = [], list2 = [0]
**Output:** [0]

 

**Constraints:**

	- The number of nodes in both lists is in the range `[0, 50]`.

	- `-100 <= Node.val <= 100`

	- Both `list1` and `list2` are sorted in **non-decreasing** order.

## Solutions

```Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
```

## AI Review

### Review

**1. Complexity**
*   **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the lengths of the two lists. Each node is visited exactly once.
*   **Space Complexity:** $O(1)$. The merge is performed in-place by reusing existing nodes; only a constant amount of extra space (dummy and pointers) is used.

**2. Correctness**
The implementation is correct and handles all edge cases:
*   **Both lists empty:** Returns `None` via `dummy.next`.
*   **One list empty:** Correctly returns the non-empty list.
*   **Lists of different lengths:** The final `if` block successfully appends the remainder of the longer list.

**3. Optimization**
While the logic is efficient, you can simplify the final conditional attachment using Python’s short-circuiting:
```python
# Replace the final if-statement with:
cur.next = list1 or list2
```
This removes the explicit `if/else` check and makes the code more idiomatic.

**4. Key Algorithmic Pattern**
*   **Dummy Node:** Used to simplify edge cases (like initializing the head of the result list).
*   **Two Pointers:** Iterating through two sequences simultaneously to build a single sorted result.
