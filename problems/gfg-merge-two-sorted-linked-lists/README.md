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

## AI Review

1. **Complexity**: Time **$O(N + M)$**, Space **$O(1)$**. You successfully avoided creating a new list, instead modifying existing pointers in-place. This addresses your recurring profile flag regarding unnecessary space complexity.
2. **Correctness**: The logic is sound and handles null/empty inputs effectively—another area where you have previously faced challenges. The loop terminates correctly when one list is exhausted, and the remaining nodes are appended safely.
3. **Optimization**: The implementation is already optimal. A minor Pythonic improvement to the final cleanup is: `tail.next = head1 or head2`. This utilizes the short-circuiting nature of `or` to attach whichever list remains without using multiple `if` statements.
4. **Key Pattern**: **Dummy Node**. By initializing with a sentinel `Node(0)`, you avoid writing special logic to handle the initial assignment of the result head, ensuring the `tail` pointer logic remains consistent throughout the merge.
