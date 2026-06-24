# Rotate A Linked List

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-rotate-a-linked-list` |
| Topics | Linked List, Data Structures |
| Solved | 2026-06-24 |

## Problem Statement

You are given the **head** of a singly linked list, you have to **left rotate** the linked list **k** times. Return the head of the modified linked list.

**Examples:**

**Input: **k = 4,
   
**Output: **50 -> 10 -> 20 -> 30 -> 40**
Explanation:
**Rotate 1:** **20 -> 30 -> 40 -> 50 -> 10
Rotate 2:** **30 -> 40 -> 50 -> 10 -> 20
Rotate 3:** **40 -> 50 -> 10 -> 20 -> 30
Rotate 4:** **50 -> 10 -> 20 -> 30 -> 40
   
**Input: **k = 6,
   
**Output: **30 -> 40 -> 10 -> 20 
   

**Constraints:
**1 &le; number of nodes &le; 105
0 &le; k &le; 109
0 &le; node.data &le; 109
