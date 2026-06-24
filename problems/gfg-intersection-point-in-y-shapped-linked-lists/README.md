# Intersection Point In Y Shapped Linked Lists

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-intersection-point-in-y-shapped-linked-lists` |
| Topics | Linked List, Data Structures |
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
