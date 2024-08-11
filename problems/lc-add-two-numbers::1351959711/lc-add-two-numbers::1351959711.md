# Add Two Numbers

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-add-two-numbers::1351959711` |
| Topics | Linked List, Math, Recursion |
| Solved | 2024-08-11 |
| Runtime | 50 ms (beats 6.975000000000002%) |
| Memory | 16.5 MB (beats 100%) |

## Problem Statement

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

**Example 1:**

**Input:** l1 = [2,4,3], l2 = [5,6,4]
**Output:** [7,0,8]
**Explanation:** 342 + 465 = 807.

**Example 2:**

**Input:** l1 = [0], l2 = [0]
**Output:** [0]

**Example 3:**

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**Output:** [8,9,9,9,0,0,0,1]

 

**Constraints:**

	- The number of nodes in each linked list is in the range `[1, 100]`.

	- `0 <= Node.val <= 9`

	- It is guaranteed that the list represents a number that does not have leading zeros.

## Solutions

```Python3
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        

        p1 = l1
        p2 = l2
        

        while p1 is not None or p2 is not None or carry:

            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            

            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            

            current.next = ListNode(new_digit)
            current = current.next
            

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        

        return dummy_head.next

```
