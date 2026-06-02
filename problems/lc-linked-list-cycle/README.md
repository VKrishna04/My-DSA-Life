# Linked List Cycle

| Field | Value |
|-------|-------|
| Difficulty | Easy |
| Platform | Leetcode |
| Problem ID | `lc-linked-list-cycle` |
| Topics | Hash Table, Linked List, Two Pointers |
| Solved | 2024-10-20 |
| Runtime | 50 ms (beats 78%) |
| Memory | 19.1 MB (beats 100%) |

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true`_ if there is a cycle in the linked list_. Otherwise, return `false`.

 

**Example 1:**

**Input:** head = [3,2,0,-4], pos = 1
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

**Input:** head = [1,2], pos = 0
**Output:** true
**Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

**Example 3:**

**Input:** head = [1], pos = -1
**Output:** false
**Explanation:** There is no cycle in the linked list.

 

**Constraints:**

	- The number of the nodes in the list is in the range `[0, 104]`.

	- `-105 <= Node.val <= 105`

	- `pos` is `-1` or a **valid index** in the linked-list.

 

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

## Solutions

```Python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
```

## AI Review

### 1. Complexity
*   **Time Complexity:** $O(n)$, where $n$ is the number of nodes. In the worst case (a cycle), the fast pointer catches the slow pointer in linear time.
*   **Space Complexity:** $O(1)$. No additional data structures are used; only two pointers are maintained.

### 2. Correctness
The implementation is correct and robust. 
*   **Empty list:** Handled (returns `False`).
*   **Single node (no cycle):** Handled (loop doesn't execute, returns `False`).
*   **Single node (cycle to itself):** Handled (pointers will meet).
*   **Large cycles:** Handled by the mathematical certainty of the "Tortoise and Hare" logic.

### 3. Optimization
**Redundancy removal:** The initial `if head is None` check is redundant. The `while f and f.next` condition naturally handles a `None` head, as `f` would be `None` immediately, skipping the loop and returning `False`. Removing this simplifies the code without changing functionality.

### 4. Key Algorithmic Pattern
**Two Pointers (Floyd’s Cycle-Finding Algorithm / Tortoise and Hare).** By moving one pointer twice as fast as the other, they are guaranteed to meet if a cycle exists.
