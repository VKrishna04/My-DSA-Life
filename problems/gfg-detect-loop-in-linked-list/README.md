# Detect Loop In Linked List

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-detect-loop-in-linked-list` |
| Topics | Linked List, two-pointer-algorithm, Data Structures, Algorithms |
| Solved | 2026-06-24 |

## Problem Statement

You are given the **head **of a singly linked list. You have to determine whether the given linked list contains a **loop **or **not**.** **A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

**Note: **Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null. Note that pos is not passed as a parameter.

**Examples:**

**Input: **pos = 2,
   
**Output: **true**
Explanation: **There exists a loop as last node is connected back to the second node.

**Input: **pos = 0,
   
**Output: **false**
Explanation: **There exists no loop in given linked list.

**Input: **pos = 1,
   
**Output: **true**
Explanation: **There exists a loop as last node is connected back to the first node.
**Constraints:**
1 &le; number of nodes &le; 105
1 &le; node->data &le; 103       
0 &le; pos &le; number of nodes
