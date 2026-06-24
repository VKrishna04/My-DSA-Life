# Serialize And Deserialize A Binary Tree

| Field | Value |
|-------|-------|
| Difficulty | Hard |
| Platform | Geeksforgeeks |
| Problem ID | `gfg-serialize-and-deserialize-a-binary-tree` |
| Topics | Tree, Data Structures |
| Solved | 2026-06-24 |

## Problem Statement

You are given the **root** of a binary tree. You have to perform **Serialization** and **Deserialization**. Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions:

- **serialize() :** stores the tree into an array and returns the array.

- **deSerialize() :** deserializes the array to the tree and returns the root of the tree.

**Note: **Multiple nodes can have the same data and the node values are** **always positive integers. Your code will be correct if the tree returned by **deSerialize(serialize(input_tree))** is same as the input tree. Driver code will print the level order traversal of the tree returned by deSerialize(serialize(input_tree)).

**Examples :**

**Input: **root = [1, 2, 3]       

**Output: **[1, 2, 3]

**Input:** root = [10, 20, 30, 40, 60, N, N] 

**Output: **[10, 20, 30, 40, 60]
**Constraints:**
1 &le; number of nodes &le; 104
1 &le; node->data &le; 109
