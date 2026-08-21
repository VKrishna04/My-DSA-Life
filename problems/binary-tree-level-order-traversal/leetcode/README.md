# Binary Tree Level Order Traversal

| Field | Value |
|-------|-------|
| Difficulty | Medium |
| Platform | Leetcode |
| Problem ID | `lc-binary-tree-level-order-traversal` |
| Topics | Tree, Breadth-First Search, Binary Tree |
| Solved | 2025-07-22 |
| Runtime | 558 ms (beats 1.324300000000001%) |
| Memory | 19.9 MB (beats 60.85600000000002%) |

## Problem Statement

Given the `root` of a binary tree, return _the level order traversal of its nodes' values_. (i.e., from left to right, level by level).

 

**Example 1:**

**Input:** root = [3,9,20,null,null,15,7]
**Output:** [[3],[9,20],[15,7]]

**Example 2:**

**Input:** root = [1]
**Output:** [[1]]

**Example 3:**

**Input:** root = []
**Output:** []

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 2000]`.

	- `-1000 <= Node.val <= 1000`

## Hints

<details>
<summary>Hint 1</summary>

Use a queue to perform BFS.

</details>

## Solutions

```Python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        print(q)
        while q:
            val = []
            
            for _ in range(len(q)):
                node = q.popleft()
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
```

## AI Review

### Review
**1. Complexity**
*   **Time:** $O(N)$, where $N$ is the number of nodes. Each node is enqueued and dequeued exactly once.
*   **Space:** $O(N)$. In a perfect binary tree, the queue holds up to $N/2$ nodes at the leaf level. The result list also stores $N$ values.

**2. Correctness**
The solution is **correct** and handles all standard cases:
*   **Empty Tree:** Correctly returns `[]` due to the `if root` check.
*   **Single Node:** Returns `[[val]]`.
*   **Skewed Trees:** Correctly processes nodes level by level regardless of balance.

**3. Concrete Optimization**
Remove the `print(q)` statement. In LeetCode or production environments, I/O operations are extremely slow relative to memory operations and will significantly inflate the runtime (latency) for large trees. 

Additionally, using a list comprehension or `map` inside the level loop can slightly improve execution speed, though it reduces readability:
```python
val = [node.val for node in q] # Get values before popping
# Followed by standard child appending logic
```

**4. Key Algorithmic Pattern**
**Breadth-First Search (BFS)** using a **Queue** with a nested loop for **Level-by-Level Processing**.
